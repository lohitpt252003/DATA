import os
import argparse
import re
from pymongo import MongoClient
from dotenv import load_dotenv

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
    problems_collection = db["problems"]

    parser = argparse.ArgumentParser(description='Update a problem in the database.')
    parser.add_argument('--id', required=True, help='The problem ID.')
    parser.add_argument('--title', help='The new title of the problem.')
    parser.add_argument('--difficulty', help='The new difficulty of the problem.')
    parser.add_argument('--tags', nargs='+', help='The new list of tags.')
    parser.add_argument('--authors', nargs='+', help='The new list of authors.')
    parser.add_argument('--description', help='The new problem description.')
    
    args = parser.parse_args()

    if not is_valid_problem_id(args.id):
        print("Invalid problem ID format. It must be in the format C<contest_id><problem_letter> (e.g., C1A, C100AA).")
        return

    update_fields = {}
    if args.title:
        update_fields['title'] = args.title
    if args.difficulty:
        update_fields['difficulty'] = args.difficulty
    if args.tags:
        update_fields['tags'] = args.tags
    if args.authors:
        update_fields['authors'] = args.authors
    if args.description:
        update_fields['description'] = args.description

    if not update_fields:
        print("No fields to update.")
        return

    try:
        result = problems_collection.update_one(
            {"id": args.id},
            {"$set": update_fields}
        )
        if result.matched_count > 0:
            print(f"Problem with id '{args.id}' updated successfully.")
        else:
            print(f"Problem with id '{args.id}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
