from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from slacker import Slacker

import os
import subprocess        # import文なので次以降の例では省略します


@respond_to('設定')
def mention_func(message):
    #subprocess.run("./dist/b")
    slack = Slacker(os.environ["API_TOKEN"])
    slack.chat.post_message('削除予定_bot_test', '設定画面を開きます',as_user=True)
    subprocess.run("./usersetting/dist/b")