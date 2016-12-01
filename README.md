# Kyoko - DexeeDeli 新宿フロントタワー店の今日の献立お知らせ bot

![五十嵐響子](https://pbs.twimg.com/media/CL-g-97UcAANZhA.png)

## About
* Kyoko is a Slack bot who tells us today's menu of [DexeeDeli Kita Shinjuku](http://www.cardenas.co.jp/shop/dexee-deli/-dexee-diner-750.html).
* Kyoko stands for "KYO no KOndate" (今日の献立: "today's menu" in Japanese).

![screen shot](https://github.com/megane42/kyoko/blob/master/screenshot.jpg?raw=true)

## Set Up
* `cp .env.sample .env`
* `vim .env` and write:
    * [Microsoft Computer Vision API](https://www.microsoft.com/cognitive-services/en-us/computer-vision-api) key
    * Slack Incoming Webhook URL

## Run Natively
* install requirements:
    * `sudo apt-get install imagemagick libmagickwand-dev ghostscript`
    * `pip install -r requirements.txt`
* and run:
    * `python kyoko.py`

## Run on Docker
* `docker run --rm --env-file /path/to/.env megane42/kyoko`

## Run Periodically
* use cron
    * Kyoko does not have any mechanism to run periodically

## Test
* `py.test`

## TODO
* error handling
* change speech randomly
