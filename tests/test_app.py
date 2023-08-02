import os
import unittest
from myapp import create_app
from myapp.models.user import User
from myapp.models.book import Book

class MyAppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
    def test_registration_and_login(self):
        # register a user
        response = self.client.post('/register', json={
            'username': 'test',
            'password': 'test'
        })
        self.assertEqual(response.status_code, 201)

        # login the user
        response = self.client.post('/login', json={
            'username': 'test',
            'password': 'test'
        })
        self.assertEqual(response.status_code, 200)
        