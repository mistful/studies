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



if __name__ == '__main__':
    unittest.main()
