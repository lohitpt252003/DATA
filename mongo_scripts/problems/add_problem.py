import os
import argparse
import re
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import json

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
    contests_collection = db["contests"]

    parser = argparse.ArgumentParser(description='Add a new problem to the database.')
    parser.add_argument('--id', required=True, help='The problem ID.')
    
    args = parser.parse_args()

    if not is_valid_problem_id(args.id):
        print("Invalid problem ID format. It must be in the format C<contest_id><problem_letter> (e.g., C1A, C100AA).")
        return

    # Extract contest_id and problem_letter
    match = re.match(r'^(C\d+)([A-Z]+)$', args.id)
    contest_id = match.group(1)
    problem_letter = match.group(2)

    # 1. Verify that the problem's contest exists in the database.
    contest = contests_collection.find_one({"id": contest_id})
    if not contest:
        print(f"Error: Contest with id '{contest_id}' not found in the database.")
        return

    # 2. Ensure that the problem is listed in the `problems` array of that contest.
    if args.id not in contest.get("problems", []):
        print(f"Error: Problem '{args.id}' not found in the 'problems' list of contest '{contest_id}'.")
        return

    # 3. Confirm that a corresponding problem directory and meta.json file exist in the local DATA repository.
    problem_dir_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'contests', contest_id, 'problems', problem_letter)
    meta_file_path = os.path.join(problem_dir_path, 'meta.json')

    if not os.path.isdir(problem_dir_path):
        print(f"Error: Problem directory not found at '{problem_dir_path}'.")
        return
    
    if not os.path.isfile(meta_file_path):
        print(f"Error: meta.json file not found at '{meta_file_path}'.")
        return

    # Read metadata from meta.json
    try:
        with open(meta_file_path, 'r') as f:
            meta_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not decode meta.json at '{meta_file_path}'.")
        return

    problem_document = {
        "id": args.id,
        "title": meta_data.get("title"),
        "difficulty": meta_data.get("difficulty"),
        "tags": meta_data.get("tags", []),
        "authors": meta_data.get("authors", []),
        "created_timestamp": datetime.now().isoformat() + "Z"
    }

    try:
        problems_collection.insert_one(problem_document)
        print(f"Problem '{args.id}' added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()