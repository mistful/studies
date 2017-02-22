import unittest
import codewars


class TestMethods(unittest.TestCase):
    def test_disemvowel(self):
        self.assertEqual(codewars.disemvowel('This website is for losers \nY LOL!'), 'Ths wbst s fr lsrs \nY LL!')

    def test_consec_empty(self):
        self.assertEqual(codewars.longest_consec([], 1), '')

    def test_consec_too_short_list(self):
        self.assertEqual(codewars.longest_consec(['aa'], 2), '')

    def test_consec_k_neg(self):
        self.assertEqual(codewars.longest_consec(['aa'], -1), '')

    def test_consec_single_longest_starts_from_first_element(self):
        self.assertEqual(codewars.longest_consec(['doctor', 'who', 'where', 'what'], 2), 'doctorwho')

if __name__ == '__main__':
    unittest.main()