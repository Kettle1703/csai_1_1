import numpy
import matplotlib.pyplot


def fibonacci(n):
    result = numpy.zeros(n, dtype=int)
    result[0] = 0
    result[1] = 1
    for i in range(2, n):
        result[i] = result[i-1] + result[i-2]
    return result


N = 13  # количество чисел Фибоначчи

fib_array = fibonacci(N)

matplotlib.pyplot.plot(numpy.arange(N), fib_array, 'x-', linewidth=0.5, markersize=4)
matplotlib.pyplot.xlabel('Номер числа Фибоначчи')
matplotlib.pyplot.ylabel('Значение числа Фибоначчи')
matplotlib.pyplot.title('График чисел Фибоначчи')
matplotlib.pyplot.xticks(numpy.arange(0, N, 2))  # настройка деления по оси x
matplotlib.pyplot.show()
