# Normal method

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


a = int(input('Enter a number: '))

if is_prime(a):
    print(f'{a} is a prime number')
else:
    print(f'{a} is NOT a prime number')

#ed1