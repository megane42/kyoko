# -*- coding: utf-8 -*-
import re
from wand.image import Image

import ocr

def format_text(text):
    u""" 各行頭が中黒になるよう整形する関数 """
    return re.sub(u'(?!^)・', u'\n・', text)

if __name__ == "__main__":
    URL = "http://www.cardenas.co.jp/shop/deli_weekly%E3%81%AE%E3%82%B3%E3%83%94%E3%83%BC.pdf"
    with Image(filename=URL, resolution=600) as entire_img:
        BASE_X = int(0.161 * entire_img.width)  # メニュー領域の最も左の座標
        BASE_Y = int(0.171 * entire_img.height) # メニュー領域の最も上の座標
        WIDTH  = int(0.800 * entire_img.width)  # メニュー領域の幅
        HEIGHT = int(0.157 * entire_img.height) # メニュー領域の高さ

        # 各日のメニューに対して
        for i in 0, 1, 2, 3, 4:
            left   = BASE_X
            right  = left   + WIDTH
            top    = BASE_Y + HEIGHT * i
            bottom = top    + HEIGHT

            # 各日のメニュー領域ごとにクロップ
            with entire_img[left:right, top:bottom] as day_img:
                BOUNDARY = int(0.35 * day_img.width) # メインメニューとサイドメニューの境界 (== メインメニューの幅)

                # メインメニューの領域だけクロップして OCR にかける
                with day_img[0:BOUNDARY,             0:day_img.height] as main_img:
                    ## main_img.save(filename='%d_main.png' % i)
                    data      = main_img.make_blob('png')
                    response  = ocr.call_ms_ocr(data)
                    text      = ocr.extract_text(response.json())
                    formatted = format_text(text)
                    print formatted
                    print '-------------------------------'

                # サイドメニューの領域だけクロップして OCR にかける
                with day_img[BOUNDARY:day_img.width, 0:day_img.height] as side_img:
                    ## side_img.save(filename='%d_side.png' % i)
                    data      = side_img.make_blob('png')
                    response  = ocr.call_ms_ocr(data)
                    text      = ocr.extract_text(response.json())
                    formatted = format_text(text)
                    print formatted
                    print '-------------------------------'
