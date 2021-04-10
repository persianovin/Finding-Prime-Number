# Optimal method

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6

    return True


a = int(input('Enter a number: '))

if is_prime(a):
    print(f'{a} is a prime number')
else:
    print(f'{a} is NOT a prime number')
