import os
import argparse
import re
from pymongo import MongoClient
from dotenv import load_dotenv
import json

def is_valid_contest_id(contest_id):
    return re.match(r'^C\d+$', contest_id)

def is_valid_problem_id(problem_id):
    return re.match(r'^C\d+[A-Z]+$', problem_id)

def main():
    # Load environment variables from the .env file in the DATA directory
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    load_dotenv(dotenv_path=dotenv_path)

    MONGO_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    DB_NAME = "data"

    client = MongoClient(
        host=MONGO_HOST,
        port=MONGO_PORT,
        username=MONGO_USERNAME,
        password=MONGO_PASSWORD,
        authSource='admin'
    )
    db = client[DB_NAME]
    contests_collection = db["contests"]

    parser = argparse.ArgumentParser(description='Update a contest in the database.')
    parser.add_argument('--id', required=True, help='The contest ID.')
    parser.add_argument('--name', help='The new name of the contest.')
    parser.add_argument('--authors', nargs='+', help='The new list of authors.')
    parser.add_argument('--add-problems', nargs='+', help='A list of problem IDs to add.')
    parser.add_argument('--remove-problems', nargs='+', help='A list of problem IDs to remove.')
    args = parser.parse_args()

    if not is_valid_contest_id(args.id):
        print("Invalid contest ID format. It must be in the format C<number> (e.g., C1, C100).")
        return

    # Validate problems to add
    if args.add_problems:
        for problem_id in args.add_problems:
            if not is_valid_problem_id(problem_id):
                print(f"Error: Invalid problem ID format for '{problem_id}'. It must be in the format C<contest_id><problem_letter> (e.g., C1A, C100AA).")
                return
            
            match = re.match(r'^(C\d+)([A-Z]+)$', problem_id)
            problem_contest_id = match.group(1)
            problem_letter = match.group(2)

            if problem_contest_id != args.id:
                print(f"Error: Problem '{problem_id}' belongs to contest '{problem_contest_id}', but is being added to contest '{args.id}'.")
                return

            problem_dir_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'contests', problem_contest_id, 'problems', problem_letter)
            meta_file_path = os.path.join(problem_dir_path, 'meta.json')

            if not os.path.isdir(problem_dir_path):
                print(f"Error: Problem directory not found for '{problem_id}' at '{problem_dir_path}'.")
                return
            
            if not os.path.isfile(meta_file_path):
                print(f"Error: meta.json file not found for '{meta_file_path}'.")
                return
            
            try:
                with open(meta_file_path, 'r') as f:
                    meta_data = json.load(f)
                    if meta_data.get("id") != problem_id:
                        print(f"Error: Problem ID in meta.json ('{meta_data.get("id")}') does not match expected ID ('{problem_id}') for problem at '{meta_file_path}'.")
                        return
            except json.JSONDecodeError:
                print(f"Error: Could not decode meta.json for '{problem_id}' at '{meta_file_path}'.")
                return
            except Exception as e:
                print(f"Error reading meta.json for '{problem_id}': {e}")
                return

    # Validate problems to remove (only format check needed) and ensure they belong to the current contest
    if args.remove_problems:
        for problem_id in args.remove_problems:
            if not is_valid_problem_id(problem_id):
                print(f"Error: Invalid problem ID format for '{problem_id}'. It must be in the format C<contest_id><problem_letter> (e.g., C1A, C100AA).")
                return
            
            match = re.match(r'^(C\d+)([A-Z]+)$', problem_id)
            problem_contest_id = match.group(1)

            if problem_contest_id != args.id:
                print(f"Error: Problem '{problem_id}' belongs to contest '{problem_contest_id}', but is being removed from contest '{args.id}'.")
                return

    update_query = {}
    update_fields = {}
    if args.name:
        update_fields['name'] = args.name
    if args.authors:
        update_fields['authors'] = args.authors
    
    if update_fields:
        update_query['$set'] = update_fields

    if args.add_problems:
        update_query['$addToSet'] = {'problems': {'$each': args.add_problems}}
    
    if args.remove_problems:
        update_query['$pullAll'] = {'problems': args.remove_problems}


    if not update_query:
        print("No fields to update.")
        return

    try:
        result = contests_collection.update_one(
            {"id": args.id},
            update_query
        )
        if result.matched_count > 0:
            print(f"Contest with id '{args.id}' updated successfully.")
        else:
            print(f"Contest with id '{args.id}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()