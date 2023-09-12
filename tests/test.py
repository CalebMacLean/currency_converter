# Imports
import unittest

from app import app


class CurrencyConverterTests(unittest.TestCase):
    """Tests for Currency Converter App"""
    def setUp(self):
        """Sets up app for testing"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Tests homepage"""
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h1>Currency Converter</h1>', response.data)

    def test_valid_conversion(self):
        """Tests valid conversion"""
        with self.client:
            response = self.client.get('/convert?from-input=USD&to-input=EUR&amount-input=1')
            self.assertEqual(response.status_code, 302)
            self.assertIn(b'The result is', response.data)

    def test_invalid_conversion(self):
        """Tests invalid conversion"""
        with self.client:
            response = self.client.get('/convert?from-input=USD&to-input=EUR&amount-input=1')
            self.assertEqual(response.status_code, 302)
            self.assertIn(b'Not a valid code', response.data)

    def test_invalid_amount(self):
        """Tests invalid amount"""
        with self.client:
            response = self.client.get('/convert?from-input=USD&to-input=EUR&amount-input=1')
            self.assertEqual(response.status_code, 302)
            self.assertIn(b'Not a valid amount', response.data)

        