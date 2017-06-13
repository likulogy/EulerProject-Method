# Problem
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

# Solution
In this case, I decided to use simple `while` loop for perform calculation between range from 0 to 1000.

Before using `while` loop in code, a function that checking 'is it multiple of three or five?' needed to more simple code.

```python
def m5(number):
    if number % 5 == 0:
        return True
    else:
        return False
```

in code described above, `%` calculate returns residual value as result of conditional expressed in `if` loop. so input of `m5()` function is not multiple of five it will return `False` value.

then, using a while loop to calculate from 1 to 1000. a usage of class is still bit tricky for me, so code is still not clean. this should be refined :)
```python
if __name__ == '__main__':
    x = 1
    sum = 0
    while x < 1000:
        if test_isMultiple.m3(x) is True:
            sum = sum + x
            print(x, sum, 3)
            x = x + 1
            continue
        elif test_isMultiple.m5(x) is True:
            sum = sum + x
            print(x, sum, 5)
            x = x + 1
            continue
        else:
            print(x, sum)
            x = x + 1
    print(sum)
```
