class Fibonacci:
    def generateFibonacci(min, max):
        fibonacci = [] # define empty list
        x = min
        while x < max:
            if 0<=len(fibonacci)<2:
                fibonacci.append(x) #[min, min]
            else:
                x = fibonacci[-1] + fibonacci[-2] #(N-1) + (N-2) = N
                if x < max:
                    fibonacci.append(x) # [min, min, N]
        fibonacci = fibonacci[1:] # [min, N]
        return fibonacci


if __name__ == '__main__':
    fib = Fibonacci.generateFibonacci(1, 4000000)
    sum = 0
    for i in fib:
        if i % 2 == 0:
            sum = sum + i
        else:
            continue
    print(sum)
