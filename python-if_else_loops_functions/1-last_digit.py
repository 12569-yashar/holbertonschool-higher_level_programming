#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
print(f"{number}")

if number < 0:
    num = -int(str(number)[-1])
elif number > 0:
    num = int(str(number)[-1])
else:
    num = 0

if (num<6):
	print(f"Last digit of {number} is {num} and is less than 6 and not 0")
elif(num>5):
	print(f"Last digit of {number} is {num} and is greater than 5")
else:
	print(f"Last digit of {number} is 0 and is 0")
