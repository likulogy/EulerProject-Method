def checker(x, st, ed):
    list = []
    for i in range(st, ed + 1):
        list.append(x % i)
    if sum(list) == 0:
        return True
    else:
        return False

x = 20
while x > 0:
    if checker(x, 1, 20):
        print(x)
        break
    else:
        x = x + 20
