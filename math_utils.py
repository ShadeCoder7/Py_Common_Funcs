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
