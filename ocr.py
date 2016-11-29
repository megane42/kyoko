# -*- coding: utf-8 -*-
import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')

def call_ms_ocr(data, language='ja', detectOrientation=False) :
    u""" Microsoft Computer Vision API / OCR を呼び出す関数 """
    KEY = os.environ.get('MS_COMPUTERVISION_API_KEY')
    params = {'language': language, 'detectOrientation': detectOrientation}
    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': KEY}
    return requests.post('https://api.projectoxford.ai/vision/v1.0/ocr', params=params, headers=headers, data=data)

def extract_text(obj):
    u""" MS OCR の実行結果を走査して、抽出された文字列全体を返す関数。文字列は line ごとに改行される。 """
    text = u''
    for region in obj['regions']:
        for line in region['lines']:
            for word in line['words']:
                text += word['text']
            text += u'\n'
    return text
