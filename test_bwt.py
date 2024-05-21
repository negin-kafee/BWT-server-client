import unittest
from server import bwt_transform, bwt_inverse

class TestBWTFunctions(unittest.TestCase):

    def test_bwt_transform(self):
        self.assertEqual(bwt_transform("AGCTTAGCTA"), "ATT$GGAACTC")

    def test_bwt_inverse(self):
        self.assertEqual(bwt_inverse("ATT$GGAACTC"), "AGCTTAGCTA")
        self.assertEqual(bwt_inverse("invalidbwt"), "Invalid BWT input: missing end-of-string marker ($)")

if __name__ == '__main__':
    unittest.main()

