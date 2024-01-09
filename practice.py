class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return Number(self.value / other.value)
        else:
            raise ValueError("Division by zero is not allowed")


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        result_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def __sub__(self, other):
        result_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def __mul__(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def __truediv__(self, other):
        if other.numerator != 0:
            result_numerator = self.numerator * other.denominator
            result_denominator = self.denominator * other.numerator
            return Fraction(result_numerator, result_denominator)


class Library:
    def __init__(self, name, address, num_books):
        self.name = name
        self.address = address
        self.num_books = num_books

    def __add__(self, other):
        return Library(self.name, self.address, self.num_books + other)

    def __sub__(self, other):
        return Library(self.name, self.address, self.num_books - other)

    def __iadd__(self, other):
        self.num_books += other
        return self

    def __isub__(self, other):
        self.num_books -= other
        return self

    def __lt__(self, other):
        return self.num_books < other.num_books

    def __gt__(self, other):
        return self.num_books > other.num_books

    def __le__(self, other):
        return self.num_books <= other.num_books

    def __ge__(self, other):
        return self.num_books >= other.num_books

    def __eq__(self, other):
        return self.num_books == other.num_books

    def __ne__(self, other):
        return self.num_books != other.num_books


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __sub__(self, other):
        from datetime import datetime
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        delta = date1 - date2
        return delta.days

    def __add__(self, days):
        from datetime import datetime, timedelta
        date = datetime(self.year, self.month, self.day)
        new_date = date + timedelta(days=days)
        return Date(new_date.day, new_date.month, new_date.year)


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = self.make_area()

    def make_area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    num_calculations = 0

    @staticmethod
    def calculate_triangle_area(base, height):
        AreaCalculator.num_calculations += 1
        return 0.5 * base * height

    @staticmethod
    def calculate_rectangle_area(length, width):
        AreaCalculator.num_calculations += 1
        return length * width

    @staticmethod
    def calculate_square_area(side):
        AreaCalculator.num_calculations += 1
        return side * side

    @staticmethod
    def calculate_rhombus_area(diagonal1, diagonal2):
        AreaCalculator.num_calculations += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_num_calculations():
        return AreaCalculator.num_calculations


class MathOperations:
    @staticmethod
    def max_of_four(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min_of_four(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average_of_four(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * MathOperations.factorial(n - 1)


num1 = Number(5)
num2 = Number(3)

result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2

print(result_add.value) 
print(result_sub.value)  
print(result_mul.value)  
print(result_div.value) 

frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

result_add_frac = frac1 + frac2
result_sub_frac = frac1 - frac2
result_mul_frac = frac1 * frac2
result_div_frac = frac1 / frac2

print(f"Addition: {result_add_frac.numerator}/{result_add_frac.denominator}")
print(f"Subtraction: {result_sub_frac.numerator}/{result_sub_frac.denominator}")
print(f"Multiplication: {result_mul_frac.numerator}/{result_mul_frac.denominator}")
print(f"Division: {result_div_frac.numerator}/{result_div_frac.denominator}")

library1 = Library("Library A", "123 Main St", 100)
library2 = Library("Library B", "456 Oak St", 150)

result_add = library1 + 50
result_sub = library1 - 30

print(result_add.num_books) 
print(result_sub.num_books)

library1 += 20
library2 -= 10

print(library1.num_books)
print(library2.num_books)

print(library1 < library2)
print(library1 >= library2)

date1 = Date(10, 1, 2022)
date2 = Date(5, 1, 2022)

days_difference = date1 - date2
print(f"Days difference: {days_difference}")

new_date = date1 + 7
print(f"New date: {new_date.day}/{new_date.month}/{new_date.year}")

circle = Circle(5)
print(circle.area)

area_triangle = AreaCalculator.calculate_triangle_area(3, 4)
area_rectangle = AreaCalculator.calculate_rectangle_area(5, 6)
area_square = AreaCalculator.calculate_square_area(7)
area_rhombus = AreaCalculator.calculate_rhombus_area(8, 9)

print(f"Triangle Area: {area_triangle}")
print(f"Rectangle Area: {area_rectangle}")
print(f"Square Area: {area_square}")
print(f"Rhombus Area: {area_rhombus}")

print(f"Number of calculations: {AreaCalculator.get_num_calculations()}")

result_max = MathOperations.max_of_four(5, 8, 3, 7)
result_min = MathOperations.min_of_four(5, 8, 3, 7)
result_average = MathOperations.average_of_four(5, 8, 3, 7)
result_factorial = MathOperations.factorial(5)

print(f"Max: {result_max}")
print(f"Min: {result_min}")
print(f"Average: {result_average}")
print(f"Factorial: {result_factorial}")
