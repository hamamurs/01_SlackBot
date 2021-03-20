# coding: utf-8

from slackbot.bot import Bot
import weatherlib.regularly as WeatherReg
import threading

def main():
    bot = Bot()
    thread1 = threading.Thread(target=bot.run)
    thread2 = threading.Thread(target=WeatherReg.main)
    thread1.start()
    thread2.start()

if __name__ == "__main__":
    print('start slackbot')
    main()