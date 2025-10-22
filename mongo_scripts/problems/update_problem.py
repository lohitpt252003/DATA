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

    parser = argparse.ArgumentParser(description='Update a problem in the database from its meta.json file.')
    parser.add_argument('--id', required=True, help='The problem ID.')
    args = parser.parse_args()

    if not is_valid_problem_id(args.id):
        print("Invalid problem ID format. It must be in the format C<contest_id><problem_letter> (e.g., C1A, C100AA).")
        return

    # Extract contest_id and problem_letter
    match = re.match(r'^(C\d+)([A-Z]+)$', args.id)
    contest_id = match.group(1)
    problem_letter = match.group(2)

    # Construct path to meta.json
    meta_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'contests', contest_id, 'problems', problem_letter, 'meta.json')

    if not os.path.isfile(meta_file_path):
        print(f"Error: meta.json file not found at '{meta_file_path}'.")
        return

    # Read and parse meta.json
    try:
        with open(meta_file_path, 'r') as f:
            meta_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not decode meta.json at '{meta_file_path}'.")
        return
    except Exception as e:
        print(f"Error reading meta.json: {e}")
        return

    update_fields = {
        "title": meta_data.get("title"),
        "difficulty": meta_data.get("difficulty"),
        "tags": meta_data.get("tags", []),
        "authors": meta_data.get("authors", []),
    }

    try:
        result = problems_collection.update_one(
            {"id": args.id},
            {"$set": update_fields}
        )
        if result.matched_count > 0:
            print(f"Problem with id '{args.id}' updated successfully from meta.json.")
        else:
            print(f"Problem with id '{args.id}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
