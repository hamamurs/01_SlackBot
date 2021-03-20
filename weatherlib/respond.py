from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

import json
import requests                         # URLアクセスを制御するためのライブラリを読み込む

if __name__ == '__main__':
    import weather as weather
else:
    import weatherlib.weather as weather

@respond_to('天気')
def mention_func(message):
    import subprocess        # import文なので次以降の例では省略します
    subprocess.run("./dist/b")
    w = weather.get_weather(400010)
    #出力データを変数に代入
    weather_today = w['forecasts'][0]['telop']
    location = w['location']['city']
    message.reply('今日の{0}の天気は{1}です。'.format(location,weather_today))
