import unittest
from machinetranslation.translator import english_to_french, french_to_english

def test_english_to_french(self):
        # Test translation of 'Hello'
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

        # Test translation of 'Yes'
        result = english_to_french('Yes')
        self.assertEqual(result, 'Oui')

    def test_french_to_english(self):
        # Test translation of 'Bonjour'
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

        # Test translation of 'Merci'
        result = french_to_english('Merci')
        self.assertEqual(result, 'Thank you')

if __name__ == '__main__':
    unittest.main()