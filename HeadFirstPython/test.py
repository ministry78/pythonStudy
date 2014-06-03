# -*- coding: UTF-8 -*-
__author__ = 'drudy'

import random

secret = random.randint(1,100)
guess = 0
tries = 0
print "你好，我是电脑机器人，接下来我们开始一个猜数字的游戏!"
print "游戏规则是：我会随机给1至100的数字，你来猜我给的数字，猜对了有奖品哦！机会只有6次哦！"

while guess != secret and tries < 6:
    guess = input("你猜的数字是多少，请输出来？")
    if guess < secret:
        print "小了哦！还有机会哦"
    elif guess > secret:
        print "大了哦！还有机会哦"
# tries = tries + 1
if guess == secret:
    print "真棒，你猜对了，快去领奖吧！"
else:
    print "真抱歉，机会已经用完了哦，祝你下次好运！"
    print "真实的数字是", secret
