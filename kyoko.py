# -*- coding: utf-8 -*-
import re
import os
import slackweb
from wand.image import Image
from datetime   import date
from dotenv     import load_dotenv

import ocr

def format_text(text):
    u""" 各行頭が中黒になるよう整形する関数 """
    return re.sub(u'(?!^)・', u'\n・', text)


def make_speech(main_menu, side_menu):
    u""" 台詞の文字列を作る関数 """
    if main_menu == '' or side_menu == '':
        raise RuntimeError('menu string is blank')
    return (
        u'DexeeDeli 新宿フロントタワー店の今日の献立はこちらです。ちゃんと野菜も選ばないとダメですよ？'
        u'\n---------------\n'
        u'*メインディッシュ*\n'
    ) + main_menu + (
        u'\n---------------\n'
        u'*サイドディッシュ*\n'
    ) + side_menu


if __name__ == "__main__":
    try:
        URL = "http://www.cardenas.co.jp/shop/deli_weekly%E3%81%AE%E3%82%B3%E3%83%94%E3%83%BC.pdf"
        with Image(filename=URL, resolution=600) as entire_img:
            # 月曜 : 0 ... 金曜 : 4
            i = date.today().weekday()

            BASE_X = int(0.161 * entire_img.width)  # メニュー領域の最も左の座標
            BASE_Y = int(0.171 * entire_img.height) # メニュー領域の最も上の座標
            WIDTH  = int(0.800 * entire_img.width)  # メニュー領域の幅
            HEIGHT = int(0.157 * entire_img.height) # メニュー領域の高さ

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
                    main_menu = format_text(text)

                # サイドメニューの領域だけクロップして OCR にかける
                with day_img[BOUNDARY:day_img.width, 0:day_img.height] as side_img:
                    ## side_img.save(filename='%d_side.png' % i)
                    data      = side_img.make_blob('png')
                    response  = ocr.call_ms_ocr(data)
                    text      = ocr.extract_text(response.json())
                    side_menu = format_text(text)

        speech = make_speech(main_menu, side_menu)

    except Exception:
        import traceback
        traceback.print_exc()
        speech = 'ごめんなさい、献立の取得に失敗しちゃいました・・・。'

    load_dotenv('.env')
    slack = slackweb.Slack(url=os.environ.get('SLACK_URL'))
    slack.notify(text=speech, username=u'五十嵐響子', icon_url='https://raw.githubusercontent.com/megane42/kyoko/master/kyoko.jpg')
