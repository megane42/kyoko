# -*- coding: utf-8 -*-
import kyoko
import unittest

class OcrTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_format_text(self):
        test_data = (
            u"・ブリの照リ焼き\n"
            u"(2個)\n"
            u"・シェフおすすめの旬野菜\n"
            u"・キャベッとべーコンのシーザーサラダ"
        )
        expected = (
            u"・ブリの照リ焼き (2個)\n"
            u"・シェフおすすめの旬野菜\n"
            u"・キャベッとべーコンのシーザーサラダ"
        )
        self.assertEqual(expected, kyoko.format_text(test_data))

if __name__ == "__main__":
    unittest.main()
