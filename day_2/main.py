# exercises 1

# get number and sum the digits of that number and show output
# example : input : 35 output : 8
#
# sum_number = 0
# number = input("please insert number for adds the digits : ")
#
# for digit in number:
#     sum_number += int(digit)
#
# print(sum_number)
#

# exercises 2

# BMI calculator
#
# print("BMI Calculator")
#
# weight = float(input("insert your weight(kg): "))
# height = float(input("insert your height(m): "))
#
# bmi = int(weight / pow(height, 2))
#
# print(f"your BMI is: {bmi}")


# exercises 3

# get the user birthdate and calculate the days , weeks and years spent
# then calculate how many days , weeks and years left

# import time
# import datetime
#
# print("age calculator")
# birthdate = input("enter your birthdate:")
# now_timestamp = time.time()
# birthdate_timestamp = time.mktime(datetime.datetime.strptime(birthdate, "%Y-%m-%d").timetuple())
#
#
# day_timestamp = 86400
# week_timestamp = 86400 * 7
# year_timestamp = 86400 * 365
#
#
# age_timestamp = now_timestamp - birthdate_timestamp
# add_90_years = age_timestamp + (year_timestamp * 90)
# age_left = add_90_years - now_timestamp
#
# days_spent = int(age_timestamp / day_timestamp)
# weeks_spent = int(age_timestamp / week_timestamp)
# years_spent = int(age_timestamp / year_timestamp)
#
# print(f"days spent: {days_spent}")
# print(f"weeks spent: {weeks_spent}")
# print(f"years spent: {years_spent}")
#
#
# days_left = int(age_left / day_timestamp)
# weeks_left = int(age_left / week_timestamp)
# years_left = int(age_left / year_timestamp)
#
# print(f"days left: {days_left}")
# print(f"weeks left: {weeks_left}")
# print(f"years left: {years_left}")
