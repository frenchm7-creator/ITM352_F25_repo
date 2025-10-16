def fibonacci(n):
    Fibo = [0, 1]
    for i in range(2, n):
        Fibo.append(Fibo[-1] + Fibo[-2])
    return Fibo[:n]

my_list = [1, 2, 3, 4, 5]
print(fibonacci(len(my_list)))
