"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    def __init__(self, path):
        file = open(path)
        # Use list comprehension to create a list with trailing spaces removed
        self.words = [w.strip() for w in file]
    
    def random(self):
        """return random word"""
        return choice(self.words)


    


