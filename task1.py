#Python programming Internship - Task 1
#Name: Syed Nihaparveen 
#Core Python Challenges 
# =============================
# Task 1 – Core Python Challenges
# =============================
#---------------------------------------------------------------------------------------------------
# 1️. Sum of Two Numbers
print("---- Sum of Two Numbers ----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

#---------------------------------------------------------------------------------------------------
# 2️. Odd or Even Checker
print("\n---- Odd or Even Checker ----")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

#---------------------------------------------------------------------------------------------------
# 3️. Factorial Calculation
print("\n---- Factorial Calculation ----")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is", fact)

#---------------------------------------------------------------------------------------------------
# 4️.Fibonacci Sequence
print("\n---- Fibonacci Sequence ----")
terms = int(input("How many terms? "))
first, second = 0, 1
print("Fibonacci Sequence:")
for _ in range(terms):
    print(first, end=" ")
    first, second = second, first + second
print()

#---------------------------------------------------------------------------------------------------
# 5️. String Reverse
print("\n---- String Reverse ----")
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

#---------------------------------------------------------------------------------------------------
# 6️. Palindrome Check
print("\n---- Palindrome Check ----")
word = input("Enter a word: ")
if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")

#---------------------------------------------------------------------------------------------------
# 7️. Leap Year Check
print("\n---- Leap Year Check ----")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

#---------------------------------------------------------------------------------------------------
# 8️. Armstrong Number
print("\n---- Armstrong Number Check ----")
num = int(input("Enter a number: "))
order = len(str(num))
sum_val = sum(int(digit) ** order for digit in str(num))

if num == sum_val:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
