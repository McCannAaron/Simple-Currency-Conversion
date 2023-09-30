"""
Name: Aaron McCann
Project: Currency Conversion
Date: 2/6/2023
"""

# Introduction

print("Welcome to the currency conversion calculator. This program can take coins and bills and converts \
it to a currency of your choice.")

print("To begin, please answer the questions below:")

print()

# Variables

pennies = float(input("How many pennies do you have: "))
nickels = float(input("How many nickels do you have: "))
dimes = float(input("How many dimes do you have: "))
quarters = float(input("How many quarters do you have: "))
bills = float(input("How much in bills do you have: "))

print()

combined = float(((pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25) + bills))
combined = round(combined, 2)

print("You have $" + str(combined) + ". Now let's convert this to euros.")

print()

# Conversion

euros = 0.94

print("The current conversion rate states that $1 = €" + str(euros) + ".")

print()

convert = float(combined * euros)
convert = round(convert, 2)

print("You have €" + str(convert) + ".")

print()

print("Thank you for using this program. I hope you found it useful.")
