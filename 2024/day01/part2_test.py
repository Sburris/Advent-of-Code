import unittest
import part2

class Test_Day01Part2_test(unittest.TestCase):
    def test_sample_input_test(self):
        list1 = [3,4,2,1,3,3]
        list2 = [4,3,5,3,9,3]
        expected = 31

        output = part2.get_similarity_score(list1, list2)
        self.assertEqual(expected, output)