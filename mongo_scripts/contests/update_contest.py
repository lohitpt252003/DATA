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

    parser = argparse.ArgumentParser(description='Update a contest in the database from its meta.json file.')
    parser.add_argument('--id', required=True, help='The contest ID.')
    args = parser.parse_args()

    if not is_valid_contest_id(args.id):
        print("Invalid contest ID format. It must be in the format C<number> (e.g., C1, C100).")
        return

    # Construct path to meta.json
    meta_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'contests', args.id, 'meta.json')

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
        "name": meta_data.get("name"),
        "authors": meta_data.get("authors", []),
        "problems": meta_data.get("problems", []),
    }

    try:
        result = contests_collection.update_one(
            {"id": args.id},
            {"$set": update_fields}
        )
        if result.matched_count > 0:
            print(f"Contest with id '{args.id}' updated successfully from meta.json.")
        else:
            print(f"Contest with id '{args.id}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()