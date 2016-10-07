import unittest
#import shutil

from main import *   # inport main.py all function

class Test_main(unittest.TestCase):

    # 注意: 因为 test 要求 顺序执行, 
    #       故用 test_01_xxx(), test_02_yyy() 这种命名方式

    def_FileName_TestInput = "test-input.txt"

    def test_01_checkStringBad(self):
        #self.assertEqual(False, checkStringBad("","",False))
        self.assertFalse(checkStringBad("",""))
        self.assertFalse(checkStringBad(None,""))
        self.assertTrue(checkStringBad("1",""))


if __name__ == '__main__':
    unittest.main()

