import unittest

from day1 import compute_captcha, compute_halfway_captcha

class TestCaptcha(unittest.TestCase):
    def setUp(self):
        self.case1 = ('1122', 3)
        self.case2 = ('1111', 4)
        self.case3 = ('1234', 0)
        self.case4 = ('91212129', 9)
        self.case5 = ('1212', 6)
        self.case6 = ('1221', 0)
        self.case7 = ('123425', 4)
        self.case8 = ('123123', 12)
        self.case9 = ('12131415', 4)

    def test_compute_captcha(self):
        self.assertEqual(compute_captcha(self.case1[0]), self.case1[1])
        self.assertEqual(compute_captcha(self.case2[0]), self.case2[1])
        self.assertEqual(compute_captcha(self.case3[0]), self.case3[1])
        self.assertEqual(compute_captcha(self.case4[0]), self.case4[1])

    def test_compute_halfway_captcha(self):
        self.assertEqual(compute_halfway_captcha(self.case5[0]), self.case5[1])
        self.assertEqual(compute_halfway_captcha(self.case6[0]), self.case6[1])
        self.assertEqual(compute_halfway_captcha(self.case7[0]), self.case7[1])
        self.assertEqual(compute_halfway_captcha(self.case8[0]), self.case8[1])
        self.assertEqual(compute_halfway_captcha(self.case9[0]), self.case9[1])

