from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

import json
import requests                         # URLアクセスを制御するためのライブラリを読み込む

@respond_to('天気')
def mention_func(message):
    url = "https://weather.tsukumijima.net/api/forecast/city/400010"

    message.reply('今日の{0}の天気は{1}です。'.format(location,wether_today))

def get_wether(url):
    # URLアクセスして情報を取得する
    response = requests.get(url)
    # URL取得に失敗した場合の例外処理を行うメソッド
    response.raise_for_status()
    # 取得したjsonデータをテキストとして読み込む
    weather_data = json.loads(response.text)

    #出力データを変数に代入
    wether_today = weather_data['forecasts'][0]['telop']
    location = weather_data['location']['city']
