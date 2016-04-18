#!usr/bin/python

single = ["", "one", "two", "three",
          "four", "five", "six",
          "seven", "eight", "nine",
          "ten", "eleven", "twelve", "thirteen",
          "fourteen", "fifteen", "sixteen",
          "seventeen", "eighteen", "nineteen"]

tens = [
    "", "twenty", "thirty", "fourty",
    "fifty", "sixty", "seventy", "eighty",
    "ninety"]

big = ["", "hundred", "thousand", "million", "billion"]


def int_to_english(n):
    if n < 20:
        return single[n]
    elif n < 100:
        return tens[(n / 10) - 1] + " " + int_to_english(n % 10)
    elif n < 1000:
        return single[n / 100] + " "
    + big[(n / 100) / (n / 100)] + " " + single[n % 100]
    elif n <

print int_to_english(111)
