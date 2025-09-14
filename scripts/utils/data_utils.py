import os
import json

# Assuming the script is run from the DATA directory or a subdirectory
DATA_BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def get_problem_path(problem_id):
    return os.path.join(DATA_BASE_PATH, "data", "problems", problem_id)

def get_submission_path(submission_id):
    return os.path.join(DATA_BASE_PATH, "data", "submissions", submission_id)

def get_solution_path(problem_id):
    return os.path.join(DATA_BASE_PATH, "data", "solutions", problem_id)

def get_all_problem_ids():
    index_file_path = os.path.join(DATA_BASE_PATH, "data", "problems", "index.json")
    if not os.path.exists(index_file_path):
        return []
    with open(index_file_path, 'r') as f:
        index_data = json.load(f)
    return list(index_data.keys())

def get_user_path(user_id):
    return os.path.join(DATA_BASE_PATH, "data", "users", user_id)

def get_all_user_ids():
    index_file_path = os.path.join(DATA_BASE_PATH, "data", "users", "index.json")
    if not os.path.exists(index_file_path):
        return []
    with open(index_file_path, 'r') as f:
        index_data = json.load(f)
    return list(index_data.keys())
