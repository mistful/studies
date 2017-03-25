import unittest
import codewars


class TestMethods(unittest.TestCase):
    def test_disemvowel(self):
        self.assertEqual(codewars.disemvowel('This website is for losers \nY LOL!'), 'Ths wbst s fr lsrs \nY LL!')

    def test_series_sum_zero(self):
        self.assertEqual('0.00', codewars.series_sum(0))

    def test_series_sum_one(self):
        self.assertEqual('1.00', codewars.series_sum(1))

    def test_series_sum_two(self):
        self.assertEqual('1.25', codewars.series_sum(2))

    def test_series_sum_five(self):
        self.assertEqual('1.57', codewars.series_sum(5))

    def test_alphabet_position_one_word(self):
        self.assertEqual(codewars.alphabet_position('AbEd'), '1 2 5 4')

    def test_alphabet_position_empty(self):
        self.assertEqual(codewars.alphabet_position(''), '')

    def test_alphabet_position_several_words(self):
        self.assertEqual(codewars.alphabet_position('AbEd Zy Aa'), '1 2 5 4 26 25 1 1')

    def test_alphabet_position_non_letters(self):
        self.assertEqual(codewars.alphabet_position('Ab;Ed 1'), '1 2 5 4')

    def test_longest_empty(self):
        self.assertEqual(codewars.longest('', ''), '')

    def test_longest_equal_lines(self):
        self.assertEqual(codewars.longest('abcde', 'abcde'), 'abcde')

    def test_longest_lines_with_repeats(self):
        self.assertEqual(codewars.longest('xyaabbbccccdefww', 'xxxxyyyyabklmopq'), 'abcdefklmopqwxy')

if __name__ == '__main__':
    unittest.main()
