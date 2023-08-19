# exercises 1
# odd or even number

# number = int(input("Which number do you want to check? "))
#
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# exercises 2
# BMI calculator
#
# print("BMI Calculator")
#
# weight = float(input("insert your weight(kg): "))
# height = float(input("insert your height(m): "))
#
# bmi = round(weight / pow(height, 2), 2)
#
# print(f"your BMI is: {bmi}")
#
# if bmi < 18.5:
#     print("You are Underweight")
# elif 18.5 <= bmi < 25.0:
#     print("You are normal weight")
# elif 25.0 <= bmi < 30.0:
#     print("You are overweight")
# elif 30.0 <= bmi < 35.0:
#     print("You are obese")
# elif bmi >= 35.0:
#     print("You are clinically obese")


# exercises 3
# works out whether if a given year is a leap year

# year = int(input("Which year do you want to check? "))
#
# if year % 100 == 0 and year % 400 == 0:
#     print(f"The {year} is leap")
# elif year % 100 != 0 and year % 4 == 0:
#     print(f"The {year} is leap")
# else:
#     print(f"The {year} is not leap")


# exercises 4
# Love calculator

# print("Welcome to the Love Calculator")
# name = input("What is your name? ").lower()
# partner_name = input("What is your partner name? ").lower()
#
# name_combine = name + partner_name
#
# true_word = "true"
# love_word = "love"
#
# true_count = 0
# love_count = 0
#
# for true_char in true_word:
#     true_count += name_combine.count(true_char)
#
# for love_char in love_word:
#     love_count += name_combine.count(love_char)
#
# love_score_str = str(true_count) + str(love_count)
# love_score_int = int(love_score_str)
#
# if love_score_int < 10 or love_score_int > 90:
#     print(f"Your score is {love_score_int}% , you got together like coke and mentos.")
# elif 40 < love_score_int < 50:
#     print(f"Your score is {love_score_int}% , you are alright together.")
# else:
#     print(f"Your score is {love_score_int}%")
