# -*- coding: utf-8 -*-
import kyoko

def test_format_text():
    test_data = (
        u"・ハンバーグチーズ焼きマスタードソース(1個)・チキン竜田揚げあら塩ソース(3個)・ブリの照リ焼き(2個)"
    )
    expected = (
        u"・ハンバーグチーズ焼きマスタードソース(1個)\n"
        u"・チキン竜田揚げあら塩ソース(3個)\n"
        u"・ブリの照リ焼き(2個)"
    )
    assert kyoko.format_text(test_data) == expected
