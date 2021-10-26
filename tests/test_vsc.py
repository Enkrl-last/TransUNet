import unittest
import networks.vit_seg_configs as vsc
import ml_collections


class TestGetData(unittest.TestCase):
    #  Each test method starts with the keyword test_
    def test_b16(self):
        a = ml_collections.ConfigDict()
        b = vsc.get_b16_config()
        self.assertIsInstance(a, type(b))

    # def test_rr(self):
    #     test_ar1 = np.ndarray([5, 3, 4])
    #     test_ar2 = np.ndarray([3, 3, 2])
    #     a, b = ds.random_rotate(test_ar1, test_ar2)
    #     self.assertIsInstance(a, np.ndarray)
    #     self.assertIsInstance(b, np.ndarray)


if __name__ == "__main__":
    unittest.main()
