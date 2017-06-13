class test_isMultiple:
    def m3(number):
        if number % 3 == 0:
            return True
        else:
            return False

    def m5(number):
        if number % 5 == 0:
            return True
        else:
            return False

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
