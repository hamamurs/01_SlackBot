# coding: utf-8
import os
import json
import requests

from slacker import Slacker

def get_weather(city_number):
    url = "https://weather.tsukumijima.net/api/forecast/city/{0}".format(city_number)
    # URLアクセスして情報を取得する
    response = requests.get(url)
    # URL取得に失敗した場合の例外処理を行うメソッド
    response.raise_for_status()
    # 取得したjsonデータをテキストとして読み込む
    weather_data = json.loads(response.text)

    return(weather_data)

def main():
    w = get_weather(400010)
    t = w['forecasts'][0]
    telop = t['telop']
    print('今日の天気は{0}です'.format(telop))
    slack = Slacker(os.environ["API_TOKEN"])
    slack.chat.post_message('削除予定_bot_test', '今日の天気は{0}です'.format(telop),as_user=True)

if __name__ == '__main__':
    main()