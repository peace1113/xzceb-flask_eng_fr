import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_EnglishToFrench(self):
        self.assertEqual(englishToFrench(''), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_FrenchToEnglish(self):
        self.assertEqual(frenchToEnglish(''), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()