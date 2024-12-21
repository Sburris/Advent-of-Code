import unittest
import part1

class Test_Day01Part1_test(unittest.TestCase):
    def test_sample_input_test(self):
        list1 = [3,4,2,1,3,3]
        list2 = [4,3,5,3,9,3]
        expected = 11

        output = part1.get_distances(list1, list2)
        self.assertEqual(expected, output)