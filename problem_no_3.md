# Problem
## Largest prime factor
- The prime factors of 13195 are 5, 7, 13 and 29.
- What is the largest prime factor of the number 600851475143 ?
- URL : https://projecteuler.net/problem=3
# Solution
1. factorization of given number.

first of all, I need to perform factorization of given number. given number is quite big, so if i try with simple while loop with linear incremental(`x = x + 1`) step, it's result will be took devastatingly long period.
```python
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
```
we know really helpful, but general principle on this problem. if we factorization '9' or '81', it's result have symmetry. '1 ... n ... n^2'.

least we could halting loop when loop value is reaching over `sqrt(n)` value. with this procedure we could reduce loop-needed count dramatically(in this case, almost 775,146 times faster!)

and, we can take another half-part of factorization result by simple devide from given number with 1-sqrt(n) loop result

2. check prime number.

ok, then we need to check given value is prime number. just devide given number from 1 to given number and make checks that is multiple of some specific value that is not equal to given number or 1.

```python
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
```

anyway, this code still needs powerful computation power during near-one-million loops, I adopt PyPy for fast calculation.

this code tooks less than 1 seconds to evaluate answer of given problem.
