def caching_fibonacci(cache = None):
    if cache == None:
        cache = {}
        def fibonacci(n):
            print (f"Cache start: {cache}")
            if n not in cache:
                if n <= 0:
                    return 0
                elif n == 1:
                    return 1
                else:
                    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
                    print(f"Hard work {n}")
            else:
                cache[n]
                print(f"Easy work {n}")
            print (f"Cache end: {cache}")
            return cache[n]
# Отримуємо функцію fibonacci
    return fibonacci

data = {2: 1, 3: 2, 4: 3, 5: 5, 6: 8}
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(0))
print(fib(1))
print(fib(5))
print(fib(10))


 