# Define the Submission data model

class Submission:
    def __init__(self, submission_id, user_id, problem_id, timestamp, status, language, test_results):
        self.submission_id = submission_id
        self.user_id = user_id
        self.problem_id = problem_id
        self.timestamp = timestamp
        self.status = status
        self.language = language
        self.test_results = test_results

    # Add methods for validation or data manipulation here
