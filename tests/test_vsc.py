""" Test Vit Seg Configs """
import unittest
import ml_collections
import networks.vit_seg_configs as vsc


class TestFuncs(unittest.TestCase):
    """ Test Class for Vit Seg Configs """
    #  Each test method starts with the keyword test_
    def test_b16(self):
        """ Test get_b16_config """
        a_a = vsc.get_b16_config()
        b_b = ml_collections.ConfigDict()
        self.assertIsInstance(a_a, type(b_b))

    def test_testing(self):
        """ Test get_b16_config """
        a_a = vsc.get_testing()
        b_b = ml_collections.ConfigDict()
        self.assertIsInstance(a_a, type(b_b))

    def test_get_r50_b16_config(self):
        """ Test get_b16_config """
        a_a = vsc.get_r50_b16_config()
        b_b = ml_collections.ConfigDict()
        self.assertIsInstance(a_a, type(b_b))

    def test_get_b32_config(self):
        """ Test get_b16_config """
        a_a = vsc.get_b32_config()
        b_b = vsc.get_b16_config()
        self.assertIsInstance(a_a, type(b_b))

    def test_get_l16_config(self):
        """ Test get_b16_config """
        a_a = vsc.get_l16_config()
        b_b = ml_collections.ConfigDict()
        self.assertIsInstance(a_a, type(b_b))

    def test_get_r50_l16_config(self):
        """ Test get_b16_config """
        a_a = vsc.get_r50_l16_config()
        b_b = vsc.get_l16_config()
        self.assertIsInstance(a_a, type(b_b))

    def test_get_l32_config(self):
        """ Test get_b16_config """
        a_a = vsc.get_l32_config()
        b_b = vsc.get_l16_config()
        self.assertIsInstance(a_a, type(b_b))

    def test_get_h14_config(self):
        """ Test get_b16_config """
        a_a = vsc.get_h14_config()
        b_b = ml_collections.ConfigDict()
        self.assertIsInstance(a_a, type(b_b))


if __name__ == "__main__":
    unittest.main()
