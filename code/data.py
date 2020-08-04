""" Author: Pascal Schlaak
    Python: 3.8.2
"""

import json
import spacy
from collections import Counter


PATH_TO_FILE = "/home/schlagoo/OneDrive/mld/semester_1/natural_language_processing/nlp_project_sose20/data/test.json"


class Data:

    def __init__(self, path):
        """Initialize instance
        """
        self.path = path

    def read_from_json(self):
        """Read data from JSON file
        """
        with open(self.path) as jf:
            self.data = json.load(jf)

    def read_from_db(self):
        """Read data from DB
        """
        pass

    def preprocess(self):
        nlp = spacy.load("en_core_web_sm")
        for movie in self.data:
            # Tokenization
            doc = nlp(self.data[movie]["synopsis"])
            # Lemmatization, remove stop words and punctuation
            words = [
                token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
            # Frequency
            frequencies = Counter(words)
            print(frequencies)
            # Entities
            entities = sorted(set([token.text for token in doc.ents]))
            print(entities)


d = Data(PATH_TO_FILE)
d.read_from_json()
d.preprocess()
