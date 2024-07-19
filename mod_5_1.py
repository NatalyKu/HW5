def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n not in cache:
            if n <= 0: 
                return 0
            elif n == 1:
                return 1
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n] 
# Отримуємо функцію fibonacci
    return fibonacci


fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(0))
print(fib(1))
print(fib(5))
print(fib(10))
print(fib(5))
 