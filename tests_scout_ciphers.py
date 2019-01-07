import unittest
import scout_ciphers


class TestScout(unittest.TestCase):
    def test_cesar(self):
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD', 1), 'BCDE')
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD', 5), 'FGHI')
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD'), 'NOPQ')
        self.assertRaises(ValueError, scout_ciphers.cesar, '')
        self.assertRaises(ValueError, scout_ciphers.cesar, list())
        self.assertRaises(ValueError, scout_ciphers.cesar, [])
        self.assertRaises(ValueError, scout_ciphers.cesar, None)
        self.assertRaises(ValueError, scout_ciphers.cesar, True)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'ab%cd')
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', None)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', True)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', 0)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', -1)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', 2.5)
        self.assertRaises(ValueError, scout_ciphers.cesar, 'abcd', -2.5)

    def test_fence(self):
        self.assertAlmostEqual(scout_ciphers.fence('kryptografia', 4), 'kgroraytaipf')
        self.assertAlmostEqual(scout_ciphers.fence('scoutciphers', 3), 'sthcucpesoir')
        self.assertRaises(ValueError, scout_ciphers.fence, '', 4)
        self.assertRaises(ValueError, scout_ciphers.fence, list(), 4)
        self.assertRaises(ValueError, scout_ciphers.fence, ['a', 'b', 'c'], 4)
        self.assertRaises(ValueError, scout_ciphers.fence, None, 4)
        self.assertRaises(ValueError, scout_ciphers.fence, True, 4)
        self.assertRaises(ValueError, scout_ciphers.fence, 'kryptografia', -4)
        self.assertRaises(ValueError, scout_ciphers.fence, 'kryptografia', 0)
        self.assertRaises(ValueError, scout_ciphers.fence, 'kryptografia', None)
        self.assertRaises(ValueError, scout_ciphers.fence, 'kryptografia', True)
        self.assertRaises(ValueError, scout_ciphers.fence, 'kryptografia', [])
        self.assertRaises(ValueError, scout_ciphers.fence, 'kryptografia', list())

    def test_gaderypoluki(self):
        self.assertAlmostEqual(
            scout_ciphers.gaderypoluki('Ala ma kota', 'GA-DE-RY-PO-LU-KI'), 'gug mg iptg')
        self.assertAlmostEqual(
            scout_ciphers.gaderypoluki('przez harcerzy', 'RE-GU-LA-MI-NO-WY'), 'pezrz hlecrezw')
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, '',
                          'GA-DE-RY-PO-LU-KI')
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, True,
                          'GA-DE-RY-PO-LU-KI')
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, 1,
                          'GA-DE-RY-PO-LU-KI')
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, None,
                          'GA-DE-RY-PO-LU-KI')
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, ['a', 'l', 'a'],
                          'GA-DE-RY-PO-LU-KI')
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, 'ala ma kota',
                          'A-DE-RY-PO-LU-KI')
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, 'ala ma kota',
                          '')
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, 'ala ma kota',
                          True)
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, 'ala ma kota',
                          None)
        self.assertRaises(ValueError, scout_ciphers.gaderypoluki, 'ala ma kota',
                          ['a', '-', 'b'])
