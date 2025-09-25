# Define the Problem data model

class Problem:
    def __init__(self, id, title, timeLimit, memoryLimit, number_of_submissions, tags, authors, difficulty):
        self.id = id
        self.title = title
        self.timeLimit = timeLimit
        self.memoryLimit = memoryLimit
        self.number_of_submissions = number_of_submissions
        self.tags = tags
        self.authors = authors
        self.difficulty = difficulty

    # Add methods for validation or data manipulation here
