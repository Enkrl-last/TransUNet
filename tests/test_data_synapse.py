import unittest
import datasets.dataset_synapse as ds
import numpy as np


class TestGetData(unittest.TestCase):
    #  Each test method starts with the keyword test_
    def test_rrf(self):
        test_ar1 = np.ndarray([1, 2, 3])
        test_ar2 = np.ndarray([8, 7, 6])
        a, b = ds.random_rot_flip(test_ar1, test_ar2)
        self.assertIsInstance(a, np.ndarray)
        self.assertIsInstance(b, np.ndarray)

    def test_rr(self):
        test_ar1 = np.ndarray([5, 3, 4])
        test_ar2 = np.ndarray([3, 3, 2])
        a, b = ds.random_rotate(test_ar1, test_ar2)
        self.assertIsInstance(a, np.ndarray)
        self.assertIsInstance(b, np.ndarray)


if __name__ == "__main__":
    unittest.main()
