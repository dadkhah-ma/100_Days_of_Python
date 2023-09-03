# exercises 1
# area calculation
#
# def area_calculate(height, width):
#     return height * width
#
#
# print("Area Calculation")
#
# wall_height = int(input("Height of wall : "))
# wall_width = int(input("Width of wall : "))
#
# coverage = 5
#
# needs_can = round(area_calculate(wall_height, wall_width) / coverage)
#
# print(f"You need {needs_can} cans")


# exercises 2
# find prime number

import math

# def is_prime(number):
#     if number == 3 or number == 2:
#         return True
#
#     round_up_sqrt = math.ceil(math.sqrt(number))
#
#     while round_up_sqrt > 1:
#
#         if number % round_up_sqrt == 0:
#             return False
#
#         round_up_sqrt -= 1
#
#     return True
#
#
# def is_prime_simple(number):
#     for range_number in range(2, number):
#         if number % range_number == 0:
#             return False
#     return True
#
#
# def print_result(number):
#     if number == 1:
#         return print("it cat be calculate")
#
#     if is_prime_simple(number):
#         return print("Its prime")
#
#     return print("Its composite ")
#
#
# print("Calculate to be prime number")
# number_input = int(input("What is your number to calculate? -> "))
# print(f"The tested number is {number_input}")
#
# print_result(number_input)
