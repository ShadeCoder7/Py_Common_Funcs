# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# In other words, a prime number can only be divided evenly by 1 and itself.
# For example, 7 is prime because its only divisors are 1 and 7. However, 10 is not prime because it can be divided by 1, 2, 5, and 10.

def is_prime(number):
    if number <= 1:
        return False  # If the number is less than or equal to 1, it is not prime
    for i in range(2, number):  # Check all numbers between 2 and 'numero-1'
        if number % i == 0:
            return False  # If a divisor is found, it is not prime
    return True  # If no divisors are found, it is prime

#Examples
print(is_prime(7))  # Prints True because 7 is prime
print(is_prime(15))  # Prints False because 15 is not prime


# The 'greater' function takes two numbers and returns the greater one.
# For example, if we compare 10 and 5, the function returns 10 because it's greater.
# If we compare 3 and 8, the function returns 8 because it's greater.

def greater(a, b):
    if a > b:
        return a  # If 'a' is greater than 'b', return 'a'
    else:
        return b  # If 'b' is greater than 'a', return 'b'

#Examples
print(greater(10, 5))  # Prints 10 because 10 is greater than 5
print(greater(3, 8))   # Prints 8 because 8 is greater than 3


# The 'is_even' function checks whether a given number is even or odd.
# A number is even if it is divisible by 2 with no remainder, and it is odd if it is not.
# For example, 4 is even because 4 % 2 == 0, but 7 is odd because 7 % 2 != 0.

def is_even(number):
    if number % 2 == 0:  # Check if the number is divisible by 2 with no remainder
        return True  # Return True if the number is even
    else:
        return False  # Return False if the number is odd

# Example usage:
print(is_even(4))  # This will print True, because 4 is even
print(is_even(7))  # This will print False, because 7 is odd


# The 'factorial' function calculates the factorial of a given number 'n'.
# The factorial of a number is the product of all positive integers less than or equal to that number.
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    if n == 1:
        return 1  # Base case: if n is 1, return 1
    return n * factorial(n - 1)  # Return the result of the multiplication

#Examples
print(factorial(5))  # This will print 120, as the factorial of 5 is 120


# The 'fibonacci' function calculates the Fibonacci number at position 'n'.
# The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous ones.
# For example, the Fibonacci number at position 4 is 3, since the sequence is: 0, 1, 1, 2, 3...

def fibonacci(n):
    if n == 0:  # Base case: if n is 0, return 0
        return 0
    elif n == 1:  # Base case: if n is 1, return 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive calls to get the sum of the two previous numbers

# Example usage:
print(fibonacci(4))  # This will print 3, because the Fibonacci number at position 4 is 3
print(fibonacci(10))  # This will print 55, because the Fibonacci number at position 10 is 55
