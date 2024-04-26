def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0  # Лічильник ітерацій

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        # Перевірка, чи знайдений елемент відповідає шуканому
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            # Знаходимо найменший індекс, який відповідає шуканому значенню
            while mid > 0 and arr[mid-1] == x:
                mid -= 1
                iterations += 1
            return (iterations, arr[mid])

    # Якщо шуканий елемент більший за всі елементи у масиві
    if left == len(arr):
        return (iterations, None)
    # Якщо лівий край вказує на елемент, який більший або рівний x
    return (iterations, arr[left])

# Тестування функції
arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
x = 0.5
result = binary_search(arr, x)
print(f"Iterations: {result[0]}, Upper bound: {result[1]}")

x = 0.45
result = binary_search(arr, x)
print(f"Iterations: {result[0]}, Upper bound: {result[1]}")


# Пояснення:
# Функція повертає кортеж, перший елемент якого – кількість ітерацій, а другий – "верхня межа".
# Якщо шуканий елемент точно відповідає значенню у масиві, повертається відповідний елемент.
# Якщо точного значення у масиві не існує, функція визначає найменший більший або рівний елемент.