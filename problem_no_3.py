'''
@Author : https://github.com/likulogy
'''

import math


def isPrime(number_integer):
    '''
    this function will check input value is prime or not. if input value is prime number, return True.
    :param number_integer: integer type number.
    :return: 
    '''
    x = 2
    while x <= number_integer:
        if number_integer % x == 0 and x != number_integer:
            x = x+1
            print('prime testing :', number_integer, False)
            return False

        elif number_integer % x == 0 and x == number_integer:
            print('prime testing :', number_integer, True)
            return True

        else:
            x = x+1


def factorization(number_integer):
    '''
    this function will return factorization result of given number. if input number is squre of specific value, returned value will be include two identical numbers.
    :param number_integer: integer type number.
    :return: 
    '''
    root = math.sqrt(number_integer)
    x = 1
    factorization_firsthalf = []
    while x <= number_integer:
        if root == x:
            factorization_firsthalf.append(x)
            x = x+1
        elif root <= x:
            factorization_secondhalf = []
            for i in reversed(factorization_firsthalf):
                value = number_integer / i
                factorization_secondhalf.append(value)
            factorization_firsthalf = factorization_firsthalf + factorization_secondhalf
            break

        elif number_integer % x == 0:
            factorization_firsthalf.append(x)
            x = x+1
        else:
            x = x+1
    return factorization_firsthalf


number = 600851475143
list = factorization(number)

listPrime = []
for i in list:
    if isPrime(i) is True:
        listPrime.append(i)

print(list)
print(max(listPrime))

