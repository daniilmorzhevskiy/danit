# 1. Calculate annual salary
name = input("Введіть ваше імя ")
monthly_salary = input("Яка ваша місячна ЗП у доларах? ")
monthly_salary = float(monthly_salary)
annual_salary = monthly_salary * 12
annual_salary_in_thousands = annual_salary / 1000
print("Ваша річна зарплата, " + name + "," + str(int(annual_salary_in_thousands)) + " тисяч доларів.")

# 2
number = int(input("Введіть парне число"))
if number >= 100:
    if number <= 999:
        if number % 2 == 0:
            print("True")
        else:
            print("False")
    else:
        print("False")
else:
    print("False")

# 3
number_to_reverse = input("Введіть число між 101 та 999 - ")
number_str = str(number_to_reverse)
reversed_number = number_str[2] + number_str[1] + number_str[0]
reversed_number = int(reversed_number)
print("Ваше число у дзеракальному вигляді " + str(reversed_number))

# 4
num1 = input("Введіть перше число")
num1 = int(num1)
num2 = input("Введіть друге число")
num2 = int(num2)

# a
sum_result = num1 + num2
print("Сума = " + str(sum_result))

# b
difference_result = num1 - num2
print("Різниця = " + str(difference_result))

# c
multiplication_result = num1 * num2
print("Множення = " + str(multiplication_result))

# d
if num2 != 0:
    division_result = num1 / num2
    print("Ділення = " + str(division_result))
else:
    print("А от на нуль ділити не можна!")

# e
if num2 != 0:
    remainder_result = num1 % num2
    print("Залишок = " + str(remainder_result))
else:
    print("А от на нуль ділити не можна")

# f
if num1 >= num2:
    print("True")
else:
    print("False")
