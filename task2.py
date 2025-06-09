def binary_search_with_upper_bound(arr, x):
    # Початковий індекс лівої межі списку
    low = 0
    # Початковий індекс правої межі списку
    high = len(arr) - 1
    # Ініціалізація змінної для підрахунку ітерацій
    iterations = 0
    # Ініціалізація змінної для зберігання верхньої межі
    upper_bound = None
    # Виконуємо пошук, поки лівий індекс не перевищить правий
    while low <= high:
        # Збільшуємо лічильник ітерацій
        iterations += 1
        # Обчислюємо середній індекс
        mid = (high + low) // 2
        # Перевіряємо, чи значення посередині списку менше за x
        if arr[mid] < x:
            # Якщо так, ігноруємо ліву половину списку
            low = mid + 1
        # Перевіряємо, чи значення посередині списку більше за x
        elif arr[mid] > x:
            # Оновлюємо верхню межу
            upper_bound = arr[mid]
            # Ігноруємо праву половину списку
            high = mid - 1
        # Якщо значення посередині списку дорівнює x
        else:
            # Оновлюємо верхню межу, оскільки вона буде дорівнювати x
            upper_bound = arr[mid]
            # Повертаємо кількість ітерацій та знайдений елемент
            return (iterations, upper_bound)
    # Якщо елемент не знайдений, повертаємо кількість ітерацій та верхню межу
    return (iterations, upper_bound)

# Тестування функції
arr = [1.1, 1.3, 2.5, 3.8, 4.6]
print(binary_search_with_upper_bound(arr, 3.5))  # (2, 3.8)
print(binary_search_with_upper_bound(arr, 4))  # (3, 4.6)
print(binary_search_with_upper_bound(arr, 6.0))  # (3, None)
print(binary_search_with_upper_bound(arr, 2.5))  # (1, 2.5)
print(binary_search_with_upper_bound(arr, 0))  # (2, 1.1)