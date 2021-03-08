# JSONファイルを制御するためのライブラリを読み込む
import json
# URLアクセスを制御するためのライブラリを読み込む
import requests# URL情報を変数に格納する
url = "https://weather.tsukumijima.net/api/forecast/city/400010"
# URLアクセスして情報を取得する
response = requests.get(url)
# URL取得に失敗した場合の例外処理を行うメソッド
response.raise_for_status()
# 取得したjsonデータをテキストとして読み込む
weather_data = json.loads(response.text)
todays_wether = weather_data['forecasts'][0]['telop']
