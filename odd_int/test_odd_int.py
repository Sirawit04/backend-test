# from odd_int import odd_int

# def test_odd_int():
#     assert odd_int([1, 1, 2]) == 2
#     assert odd_int([0]) == 0
#     assert odd_int([7]) == 7
#     assert odd_int([0, 1, 0, 1, 0]) == 0
#     assert odd_int([1, 2, 2, 1, 3]) == 3


#     print("All tests passed")

# if __name__ == "__main__":
#     test_odd_int()

import unittest
from odd_int import odd_int  

class TestOddInt(unittest.TestCase):
    
    def test_single_element(self):
        self.assertEqual(odd_int([7]), 7)
    
    def test_zero(self):
        self.assertEqual(odd_int([0]), 0)

    def test_1_1_2(self):
        self.assertEqual(odd_int([1, 1, 2]), 2)

    def test_0_1_0_1_0(self):
        self.assertEqual(odd_int([0, 1, 0, 1, 0]), 0)

    def test_final(self):
        self.assertEqual(odd_int([1,2,2,3,3,3,4,3,3,3,2,2,1]), 4)    

if __name__ == '__main__':
    unittest.main()