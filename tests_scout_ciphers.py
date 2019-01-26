import unittest
import scout_ciphers


class TestScout(unittest.TestCase):
    def test_cesar(self):
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD', 1), 'BCDE')
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD', 5), 'FGHI')
        self.assertAlmostEqual(scout_ciphers.cesar('aBcD'), 'NOPQ')
        self.check_exceptions(scout_ciphers.cesar)

    def test_fence(self):
        self.assertAlmostEqual(scout_ciphers.fence(
            'kryptografia', 4), 'kgroraytaipf')
        self.assertAlmostEqual(scout_ciphers.fence(
            'scoutciphers', 3), 'sthcucpesoir')
        self.check_exceptions(scout_ciphers.fence)

    def test_gaderypoluki(self):
        self.assertAlmostEqual(
            scout_ciphers.gaderypoluki('Ala ma kota', 'GA-DE-RY-PO-LU-KI'), 'gug mg iptg')
        self.assertAlmostEqual(
            scout_ciphers.gaderypoluki('przez harcerzy', 'RE-GU-LA-MI-NO-WY'), 'pezrz hlecrezw')
        self.check_exceptions(scout_ciphers.gaderypoluki)

    def test_vignere(self):
        self.assertAlmostEqual(scout_ciphers.vignere(
            'TO JEST BARDZO TAJNY TEKST', 'TAJNE'), 'MO SRWM BJEHSO CNNGY CROLT')
        self.assertAlmostEqual(scout_ciphers.vignere(
            'TO JEST BARDZO TAJNY TEKST', 'NT OJES TBARDZ OTAJN YTEKS'), 'GH XNWL UBRUCN HTJWL RXOCL')
        self.check_exceptions(scout_ciphers.vignere)

    def check_exceptions(self, func):
        self.assertRaises(ValueError, func, 'test value', '')
        self.assertRaises(ValueError, func, '', 'test value')
        self.assertRaises(ValueError, func, 'test value', None)
        self.assertRaises(ValueError, func, None, 'test value')
        self.assertRaises(ValueError, func, 'test value', True)
        self.assertRaises(ValueError, func, True, 'test value')
        self.assertRaises(ValueError, func, 'test value', 1)
        self.assertRaises(ValueError, func, 1, 'test value')
        self.assertRaises(ValueError, func, 'test value', 1.5)
        self.assertRaises(ValueError, func, 1.5, 'test value')
