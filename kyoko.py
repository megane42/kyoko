# -*- coding: utf-8 -*-
import re
import ocr

def format_text(text):
    u""" 各行頭が中黒になるよう整形する関数 """
    return re.sub(u'\n(?!・)', u' ', text)

if __name__ == "__main__":
    for filename in ['dest1.png', 'dest2.png', 'dest3.png', 'dest4.png', 'dest5.png']:
        with open(filename, 'rb') as f:
            data = f.read()

        response  = ocr.call_ms_ocr(data)
        text      = ocr.extract_text(response.json())
        formatted = format_text(text)
        print formatted
        print '-------------------------------'
