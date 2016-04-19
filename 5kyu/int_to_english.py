#!usr/bin/python

# Author: ZhengC
# Lang: Python 2.7
# CodeWars: int_to_english
# @{0.0}@ codemonkey for encouragement

single = ["", "one", "two", "three",
          "four", "five", "six",
          "seven", "eight", "nine",
          "ten", "eleven", "twelve", "thirteen",
          "fourteen", "fifteen", "sixteen",
          "seventeen", "eighteen", "nineteen"]

tens = [
    "", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty",
    "ninety"]

big = ["", "hundred", "thousand", "million", "billion"]


def int_to_english(n):

    if n < 20:
        return (single[n])
    elif n < 100:
        return (tens[(n / 10) - 1] +
                " " + int_to_english(n % 10)).rstrip()
    elif n < 1000:
        return (int_to_english(n / 100) +
                " " + big[1] + " " + int_to_english(n % 100)).rstrip()
    elif n < 1000000:
        return (int_to_english(n / 1000) +
                " " + big[2] + " " + int_to_english(n % 1000)).rstrip()
    elif n < 1000000000:
        return (int_to_english(n / 1000000) +
                " " + big[3] + " " + int_to_english(n % 1000000)).rstrip()
    elif n < 10000000000000:
        return (int_to_english(n / 1000000000) +
                " " + big[4] + " " + int_to_english(n % 1000000000)).rstrip()

print "{} {}".format("test 1", int_to_english(11))
print "{} {}".format("test 2", int_to_english(47))
print "{} {}".format("test 3", int_to_english(333))
print "{} {}".format("test 4", int_to_english(4444))
print "{} {}".format("test 5", int_to_english(55555))
print "{} {}".format("test 6", int_to_english(6666666))
print "{} {}".format("test 7", int_to_english(777777777))
print "{} {}".format("test 8", int_to_english(8888888888))
