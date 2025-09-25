# Define the Solution data model

class Solution:
    def __init__(self, problem_id, language, code, markdown):
        self.problem_id = problem_id
        self.language = language
        self.code = code
        self.markdown = markdown

    # Add methods for validation or data manipulation here
