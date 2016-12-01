# (WIP) DexeeDeli 新宿フロントタワー店の今日の献立お知らせ bot

![五十嵐響子](https://pbs.twimg.com/media/CL-g-97UcAANZhA.png)

## Install
* `sudo apt-get install imagemagick libmagickwand-dev`
* `pip install -r requirements.txt`

## Set Up
* `cp .env.sample .env`
* write:
    * [Microsoft Computer Vision API](https://www.microsoft.com/cognitive-services/en-us/computer-vision-api) key
    * Slack Incoming Webhook URL

## Run
* `python kyoko.py`

## Test
* `py.test`

## TODO
* error handling
* dockerize
* change speech randomly
