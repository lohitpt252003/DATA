import os
import argparse
import re
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime, timedelta
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

    parser = argparse.ArgumentParser(description='Add a new contest to the database.')
    parser.add_argument('--id', required=True, help='The contest ID.')
    parser.add_argument('--name', required=True, help='The name of the contest.')
    parser.add_argument('--authors', nargs='+', required=True, help='A list of authors.')
    parser.add_argument('--problems', nargs='+', help='A list of problem IDs for the contest.')
    args = parser.parse_args()

    if not is_valid_contest_id(args.id):
        print("Invalid contest ID format. It must be in the format C<number> (e.g., C1, C100).")
        return

    # Validate problems if provided
    if args.problems:
        for problem_id in args.problems:
            if not is_valid_problem_id(problem_id):
                print(f"Error: Invalid problem ID format for '{problem_id}'. It must be in the format C<contest_id><problem_letter> (e.g., C1A, C100AA).")
                return
            
            # Extract contest_id and problem_letter from the problem_id
            match = re.match(r'^(C\d+)([A-Z]+)$', problem_id)
            problem_contest_id = match.group(1)
            problem_letter = match.group(2)

            # Check if the problem's contest ID matches the current contest ID
            if problem_contest_id != args.id:
                print(f"Error: Problem '{problem_id}' belongs to contest '{problem_contest_id}', but is being added to contest '{args.id}'.")
                return

            # Check if the problem directory and meta.json exist in the local DATA repository
            problem_dir_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'contests', problem_contest_id, 'problems', problem_letter)
            meta_file_path = os.path.join(problem_dir_path, 'meta.json')

            if not os.path.isdir(problem_dir_path):
                print(f"Error: Problem directory not found for '{problem_id}' at '{problem_dir_path}'.")
                return
            
            if not os.path.isfile(meta_file_path):
                print(f"Error: meta.json file not found for '{meta_file_path}'.")
                return
            
            # Optionally, read and validate meta.json content if needed
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

    startTime = datetime.now() + timedelta(days=7)
    endTime = startTime + timedelta(hours=4)

    contest_document = {
        "id": args.id,
        "name": args.name,
        "authors": args.authors,
        "startTime": startTime.isoformat() + "Z",
        "endTime": endTime.isoformat() + "Z",
        "problems": args.problems if args.problems else [],
        "participants": []
    }

    try:
        contests_collection.insert_one(contest_document)
        print(f"Contest '{args.name}' added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
