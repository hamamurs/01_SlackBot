# coding: utf-8

from slackbot.bot import Bot
import weatherlib.regularly as WeatherReg

def main():
    bot = Bot()
    WeatherReg.main()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    main()