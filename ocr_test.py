# -*- coding: utf-8 -*-
import ocr

def test_extract_text():
    test_data = {"regions":[
        {"boundingBox":"55,67,493,384","lines":[
            {"boundingBox":"55,67,493,47","words":[
                {"boundingBox":"55,86,11,11", "text":"a"},
                {"boundingBox":"77,75,46,35", "text":"b"},
            ]},
            {"boundingBox":"55,67,493,47","words":[
                {"boundingBox":"55,86,11,11", "text":"c"},
                {"boundingBox":"77,75,46,35", "text":"d"},
            ]},
        ]},
        {"boundingBox":"55,67,493,384","lines":[
            {"boundingBox":"55,67,493,47","words":[
                {"boundingBox":"55,86,11,11", "text":"e"},
                {"boundingBox":"77,75,46,35", "text":"f"},
            ]},
            {"boundingBox":"55,67,493,47","words":[
                {"boundingBox":"55,86,11,11", "text":"g"},
                {"boundingBox":"77,75,46,35", "text":"h"},
            ]},
        ]},
    ]}
    assert ocr.extract_text(test_data) == "abcdefgh"
