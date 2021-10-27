""" Test Data Synapse """
import unittest
import numpy as np
import datasets.dataset_synapse as ds


class TestGetData(unittest.TestCase):
    """ Test Class for Data Synapse """
    #  Each test method starts with the keyword test_
    def test_rrf(self):
        """ Test random_rot_flip """
        test_ar1 = np.ndarray([1, 2, 3])
        test_ar2 = np.ndarray([8, 7, 6])
        a_a, b_b = ds.random_rot_flip(test_ar1, test_ar2)
        self.assertIsInstance(a_a, np.ndarray)
        self.assertIsInstance(b_b, np.ndarray)

    def test_rr(self):
        """ Test random_rotate """
        test_ar1 = np.ndarray([5, 3, 4])
        test_ar2 = np.ndarray([3, 3, 2])
        a_a, b_b = ds.random_rotate(test_ar1, test_ar2)
        self.assertIsInstance(a_a, np.ndarray)
        self.assertIsInstance(b_b, np.ndarray)


if __name__ == "__main__":
    unittest.main()
