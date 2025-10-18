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

    parser = argparse.ArgumentParser(description='Delete a problem by its ID.')
    parser.add_argument('--id', required=True, help='The problem ID.')
    args = parser.parse_args()

    if not is_valid_problem_id(args.id):
        print("Invalid problem ID format. It must be in the format C<contest_id><problem_letter> (e.g., C1A, C100AA).")
        return

    try:
        result = problems_collection.delete_one({"id": args.id})
        if result.deleted_count > 0:
            print(f"Problem with id '{args.id}' deleted successfully.")
        else:
            print(f"Problem with id '{args.id}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
