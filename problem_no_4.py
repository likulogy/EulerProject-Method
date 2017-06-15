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

palindrome = []

for i in range(1000):
    for j in range(1000):
        number = int(i) * int(j)
        if isPalindrome(number) is True:
            palindrome.append(number)

answer = max(palindrome)
print(answer)
