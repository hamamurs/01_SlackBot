# coding: utf-8

from slackbot.bot import Bot
import wetherlib.regularly as WetherReg

def main():
    bot = Bot()
    WetherReg.main()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    main()