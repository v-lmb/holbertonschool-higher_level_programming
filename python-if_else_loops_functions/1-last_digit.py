#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
num_neg = abs(number) % 10
if number > 6:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
elif number < 5:
    print(f"Last digit of {number} is -{num_neg} and is greater than 5")
else:
    print(f"Last digit of {number} is {num} and is 0")
