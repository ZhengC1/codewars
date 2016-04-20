#! usr/bin/python

# Author: ZhengC
# Lang: 2.7.6
# CodeWars: simple elevator
# @{0.0}@ codemonkey for encouragement


def goto(level, button):

    levels = ['0', '1', '2', '3']

    if (button in levels) and (level > -1 and level < 4):
        cat = int(button)
        return cat - level
    else:
        return 0

print goto(2, '1')
print goto(2, '0')
print goto(1, '1')
print goto(3, '2')
