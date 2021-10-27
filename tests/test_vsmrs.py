""" Test Vit Sef Modeling Resnet Skip """
import unittest
import networks.vit_seg_modeling_resnet_skip as vsmrs


class TestFuncs(unittest.TestCase):
    """ Test Class for Vit Sef Modeling Resnet Skip """
    #  Each test method starts with the keyword test_
    def conv3x3(self):
        """ Test conv3x3 """
        a_a = vsmrs.conv3x3(1, 2)
        b_b = vsmrs.StdConv2d(1, 2, 3)
        self.assertIsInstance(a_a, type(b_b))

    def conv1x1(self):
        """ Test conv1x1 """
        a_a = vsmrs.conv1x1(1, 2)
        b_b = vsmrs.StdConv2d(1, 2, 1)
        self.assertIsInstance(a_a, type(b_b))


if __name__ == "__main__":
    unittest.main()
