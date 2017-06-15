# Problem
## Largest palindrome product
- A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
- Find the largest palindrome made from the product of two 3-digit numbers.
- URL : https://projecteuler.net/problem=4
# Solution
## defining fuction that checks symmetry of given number.
At the beginning, I decided using Brute Force method rather than some mathematical approaches while expected loop count is relatively small, so modern calculators(AKA computer) able to calculate effectively.

```python
def isPalindrome(number_integer):
    number = list(str(number_integer))
    reversed_number = number[::-1]
    object_count = len(number)

    for i in range(object_count):
        forward = int(number[i])
        backward = int(reversed_number[i])
        if forward != backward:
            return False
    return True
```
with this function, palindromity(??!) of given number easily tested. when initial stage that I starts to develop this code, I used `reverse(number)` than `number[::-1]`. anyway, that is not subscriptable so cannot be directly compared with `number` list.

to direct comparison I need to returned exactly reversed list, so I using `::-1` slicer. 

## Numbers generation for Brute Force
```python
palindrome = []

for i in range(1000):
    for j in range(1000):
        number = int(i) * int(j)
        if isPalindrome(number) is True:
            palindrome.append(number)

answer = max(palindrome)
print(answer)
```
`for` loop block generates lots of numbers that result of product between two numbers. these generated numbers tested it's palindromity by custom-defined function mentioned above.

almost million loops after, answer will be appeared forward your eyes!
