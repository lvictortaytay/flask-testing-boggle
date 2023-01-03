from unittest import TestCase
from ..app import app #use dot dot when a module is in the same folder
from flask import session
from ..boggle import Boggle


class FlaskTests(TestCase):

# TODO -- write tests for every view function / feature!
    def start(self):
        """run this before every test starts"""
        self.client = app.test_client()
        app.config["TESTING"] = True

    def homepageTest(self):
        """make sure everything is working in the html and check the session """
        with self.client:
            response = self.client.get("/")
            self.assertIn("board", session)
            self.assertIn("score:" , response.data)

    def test_ok_word(self):
        """Test if word is valid by modifying the board in the session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = self.client.get('/check-word?word=cat')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test if word is in the dictionary"""

        self.client.get('/')
        response = self.client.get('/check-word?word=impossible')
        self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if word is on the board"""

        self.client.get('/')
        response = self.client.get('/check-word?word=fsjdakfkldsfjdslkfjdlksf')
        self.assertEqual(response.json['result'], 'not-word')
