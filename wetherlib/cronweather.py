# coding: utf-8
import os

from slacker import Slacker
import weather

def main():
    w = weather.get_weather(400010)
    t = w['forecasts'][0]
    telop = t['telop']

    slack = Slacker(os.environ["API_TOKEN"])
    slack.chat.post_message('削除予定_bot_test', '今日の天気は{0}です'.format(telop),as_user=True)

if __name__ == '__main__':
    main()