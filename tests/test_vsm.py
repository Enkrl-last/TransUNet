""" Test Vit Seg Modelling """
import unittest
from torch import ones
import ml_collections
import networks.vit_seg_modeling as vsm


class TestFuncs(unittest.TestCase):
    """ Test Class for Vit Seg Modelling """
    #  Each test method starts with the keyword test_
    def swish(self):
        """ Test swish """
        x_tensor = ones(2, 3)
        a_a = vsm.swish(x_tensor)
        b_b = x_tensor * ones(2, 3)
        self.assertIsInstance(a_a, type(b_b))


class TestMlp(unittest.TestCase):
    """ Test Class for Mlp Class """
    def setUp(self):
        """ Init """
        self.calculator = vsm.Mlp(ml_collections.ConfigDict())

    def test_forward(self):
        """ Test forward """
        x_tensor = ones(2, 3)
        a_a = self.calculator.forward(x_tensor)
        self.assertIsInstance(a_a, type(x_tensor))


class DecoderBlock(unittest.TestCase):
    """ Test Class for DecoderBlock Class """

    def setUp(self):
        """ Init """
        self.dec = vsm.DecoderBlock(1, 2)

    def test_forward(self):
        """ Test forward """
        x_tensor = ones(2, 3)
        a_a = self.dec.forward(x_tensor)
        self.assertIsInstance(a_a, type(x_tensor))


class VisionTransformer(unittest.TestCase):
    """ Test Class for VisionTransformer Class """

    def setUp(self):
        """ Init """
        self.v_t = vsm.VisionTransformer(ml_collections.ConfigDict())

    def test_forward(self):
        """ Test forward """
        x_tensor = ones(2, 3)
        a_a = self.v_t.forward(x_tensor)
        self.assertIsInstance(a_a, type(x_tensor))


if __name__ == "__main__":
    unittest.main()
