# test_main.py

import unittest
from main import count_four_legged_animals

class TestAniimalLegCounter(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(count_four_legged_animals(['lion','monkey','deer','snake','elephant']),3)

    def test_normal_case_2(self):
        self.assertEqual(count_four_legged_animals(['frog','horse','spider','ant']), 2)

    def test_normal_case_3(self):
        self.assertDictEqual(count_four_legged_animals(['dog','cat','lion']), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_four_legged_animals([]), 0)

    def test_edge_case_unknown_animals(self):
        self.assertEqual(count_four_legged_animals(['dragon','unicorn']), 0)

    def test_edge_case_mixed_known_and_unknown(self):  
        self.assertEqual(count_four_legged_animals(['lion','unicorn','dog','ghost']), 2)


if __name__ == '__main__':
    unittest.main()




    
    