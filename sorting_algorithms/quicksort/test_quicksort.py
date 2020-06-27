import unittest
from quicksort import quicksort

class TestQuickSort(unittest.TestCase):

    def test_quicksort(self):
        self.assertEqual(quicksort([0,0]), [0,0])
        self.assertEqual(quicksort([1]), [1])
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([2, 2, 0, 0]), [0, 0, 2, 2])
        self.assertEqual(quicksort([-1, 2, 3]), [-1, 2, 3])
        self.assertEqual(quicksort([5, 4, 7, -12, 4]), [-12, 4, 4, 5, 7])


if __name__ == "__main__":
    unittest.main()
