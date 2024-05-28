#Є помилка у функції Фібоначчі. 
#Перероблена функція від Артема Липко а також фікс багів
def fibonacci(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[-1]

def print_fibonacci_numbers(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print(fib)

def count_operations(n):
    operations = 0
    for i in range(2, n):
        operations += 2
    return operations

n = 10  # Присвоюємо значення змінній n (саме 10те буде = 55)
result = fibonacci(n)  # Виклик функції Фібоначчі з n як аргумент
print("n-те число Фібоначчі:", result)  # Результат

print_fibonacci_numbers(n)  # Виводимо усі числа Фібоначчі до n-те числа Фібоначчі

operations = count_operations(n)  # Підраховуємо кількість операцій
print("Кількість операцій:", operations)  # Підрахунок операцій