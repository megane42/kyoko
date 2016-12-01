# -*- coding: utf-8 -*-
import requests
import os
from dotenv import load_dotenv

def call_ms_ocr(data, language='ja', detectOrientation=False) :
    u""" Microsoft Computer Vision API / OCR を呼び出す関数 """

    load_dotenv('.env')
    KEY = os.environ.get('MS_COMPUTERVISION_API_KEY')

    return requests.post(
        'https://api.projectoxford.ai/vision/v1.0/ocr',
        params={'language': language, 'detectOrientation': detectOrientation},
        headers={'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': KEY},
        data=data
    )

def extract_text(obj):
    u""" MS OCR の実行結果から、抽出された文字列全体を返す関数 """
    return ''.join([ word['text'] for region in obj['regions'] for line in region['lines'] for word in line['words'] ])
