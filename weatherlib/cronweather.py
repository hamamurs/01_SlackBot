# coding: utf-8
import os
import json
import requests
from slacker import Slacker

if __name__ == '__main__':
    import weather as weather
else:
    import weatherlib.weather as weather

def main():
    w = weather.get_weather(400010)
    #出力データを変数に代入
    weather_today = w['forecasts'][0]['telop']
    location = w['location']['city']

    slack = Slacker(os.environ["API_TOKEN"])
    slack.chat.post_message('削除予定_bot_test', '今日の{0}の天気は{1}です'.format(location,weather_today),as_user=True)

if __name__ == '__main__':
    main()