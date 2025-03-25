# functions
import math


def greet():
    print("hello, functions")


def area_circle(radius):
    result = 22 / 7 * radius ** 2
    result = round(result)
    print(result)


def volume_cylinder(height, radius, precision=2):
    v = 22 / 7 * radius ** 2 * height
    v = round(v, precision)
    print(f"Radius is {radius},height is {height},volume is {v}")


def area_triangle(a, b, c):
    """"calculates the area of a triangle then returns the result"""
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))
    area = math.sqrt(area)
    area = round(area)
    print(f"Area is {area}")
    return area

# 4 == * 4 * 3 * 2 * 1
def factorial (num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
        return result
def add_numbers(*args):
    result = 0
    for number in args:
        result += number
    return result

# function that if i give ksh3, 000
def clean_numbers(word):
    return 3000

#variable args
print(add_numbers(1, 2, 3))
print(add_numbers(1, 2, 3, 4))




#print(factorial(5))


# use a function == call function
area_triangle(3, 4, 5)

volume_cylinder(10, 7.25, 3)
volume_cylinder(7, 10.768, 1)
volume_cylinder(radius=45, height=67, precision=2)

# area_circle(7)
# area_circle(25)
# area_circle(7.5654)
