import unittest
import scout_ciphers


class TestScout(unittest.TestCase):
    def test_cesar(self):
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD', 1), 'BCDE')
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD', 5), 'FGHI')
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD'), 'NOPQ')
        self.assertRaises(ValueError, scout_ciphers.cesar, '')
        self.assertRaises(ValueError, scout_ciphers.cesar, None)
        self.assertRaises(ValueError, scout_ciphers.cesar, True)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'ab%cd')
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', None)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', True)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', 0)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', -1)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', 2.5)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', -2.5)
