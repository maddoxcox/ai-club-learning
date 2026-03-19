# Day 20: Study Buddy CLI — Month 1 Capstone
# Combines: exceptions, libraries, testing, file I/O, regex, OOP, APIs

import json
import os
import re
import sys
from datetime import datetime

# TODO: pip install requests rich
# import requests
# from rich.console import Console


class Flashcard:
    """A single flashcard with question and answer."""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.times_shown = 0
        self.times_correct = 0

    def show(self):
        # TODO: Display question, get user answer
        pass

    def accuracy(self):
        # TODO: Return accuracy percentage
        pass

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        pass


class StudyTopic:
    """A topic with summary and flashcards."""
    def __init__(self, name, summary="", source_url=""):
        self.name = name
        self.summary = summary
        self.source_url = source_url
        self.flashcards = []
        self.date_added = datetime.now().isoformat()

    def add_flashcard(self, question, answer):
        pass

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        pass


class StudySession:
    """Manages study sessions, topics, and progress."""
    SAVE_FILE = "study_data.json"

    def __init__(self):
        self.topics = []
        self.load()

    def add_topic(self, name):
        """Validate topic name, fetch from Wikipedia, create flashcards."""
        # TODO: Validate with regex
        # TODO: Fetch from Wikipedia API
        # TODO: Generate flashcards
        pass

    def quiz(self, topic_name):
        """Quiz on a topic's flashcards."""
        pass

    def view_progress(self):
        """Show all topics and quiz scores."""
        pass

    def save(self):
        """Save all data to JSON."""
        pass

    def load(self):
        """Load data from JSON."""
        pass


def validate_topic(name):
    """Validate topic name with regex."""
    # TODO: 3-50 chars, alphanumeric + spaces
    pass


def fetch_wikipedia(topic):
    """Fetch topic summary from Wikipedia API."""
    # TODO: GET https://en.wikipedia.org/api/rest_v1/page/summary/{topic}
    # TODO: Handle errors
    pass


def main():
    session = StudySession()

    while True:
        print("\n=== Study Buddy ===")
        print("[1] Study a new topic")
        print("[2] Review saved topics")
        print("[3] Take a quiz")
        print("[4] View progress")
        print("[5] Quit")

        choice = input("\nChoice: ").strip()
        # TODO: Handle choices


if __name__ == "__main__":
    main()
