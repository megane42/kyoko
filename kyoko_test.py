# -*- coding: utf-8 -*-
import kyoko
import pytest

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

def test_make_speech():
    main_menu = 'foo'
    side_menu = 'bar'
    speech = (
        u'\n---------------\n'
        u'*メインディッシュ*\n'
        u'foo'
        u'\n---------------\n'
        u'*サイドディッシュ*\n'
        u'bar'
    )
    assert speech in kyoko.make_speech(main_menu, side_menu)

def test_make_speech_error_when_main_is_blank():
    main_menu = ''
    side_menu = 'bar'
    with pytest.raises(RuntimeError):
        kyoko.make_speech(main_menu, side_menu)

def test_make_speech_error_when_side_is_blank():
    main_menu = 'foo'
    side_menu = ''
    with pytest.raises(RuntimeError):
        kyoko.make_speech(main_menu, side_menu)
