# exercises 1
# calculate the average student height from a list

# student_height_sum = 0
# students_height = input("Please insert list of students heights ").split()
# students_count = len(students_height)
#
# for height in students_height:
#     student_height_sum += int(height)
#
# print(f"The sum of student height is : {student_height_sum}")
# print(f"The student count is : {students_count}")
# print(f"The avg of student height is : {round(student_height_sum / students_count)}")


# exercises 2
# calculate the highest score from a list

# highest_score = 0
# score_list = map(
#     int,
#     input("Please insert list of student score ").split()
# )
#
# for score in score_list:
#     if score > highest_score:
#         highest_score = score
#
# print(f"The highest score is : {highest_score}")


# exercises 3
# calculate the sum of all even numbers from 1 to 100. including 1 and 100
#
# total = 0
# for number in range(1, 101):
#
#     if number % 2 == 0:
#         total += number
#
# print(f"The sum of even number between 1 - 100 is : {total}")


# exercises 3
# Fizz buzz exercise

# for number in range(1, 101):
#
#     if number % 3 == 0 and number % 5 == 0:
#         print('fizzbuzz')
#         continue
#
#     if number % 3 == 0:
#         print('fizz')
#         continue
#
#     if number % 5 == 0:
#         print('buzz')
#         continue
#
#     print(number)
