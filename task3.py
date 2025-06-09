import timeit
import os


# Реалізація алгоритму Боєра-Мура
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1


# Реалізація алгоритму Кнута-Морріса-Пратта
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1


# Реалізація алгоритму Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i : i + substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (
                current_slice_hash - ord(main_string[i]) * h_multiplier
            ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])
            ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1


# Отримуємо абсолютний шлях до каталогу, де знаходиться скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Визначаємо шлях до файлів у підкаталозі "test"
file1_path = os.path.join(script_dir, "tests", "text1.txt")
file2_path = os.path.join(script_dir, "tests", "text2.txt")

# Завантаження текстових файлів
with open(file1_path, "r", encoding="cp1252") as file:
    text1 = file.read()
with open(file2_path, "r", encoding="cp1252") as file:
    text2 = file.read()

# Інше кодування:
# with open(file1_path, "r", encoding="utf-8") as file:
#     text1 = file.read()
# with open(file2_path, "r", encoding="utf-8") as file:
#     text2 = file.read()

# Вибір підрядків для тестування
existing_substring = "алгоритм"
non_existing_substring = "вигаданий_підрядок"


# Функція для вимірювання часу
def measure_time(func, text, pattern):
    def wrapper():
        return func(text, pattern)

    return timeit.timeit(wrapper, number=1000)


# Вимірювання часу для статті 1
print("Article 1:")
print(
    f"Boyer-Moore (existing): {measure_time(boyer_moore_search, text1, existing_substring)}"
)
print(
    f"Boyer-Moore (non-existing): {measure_time(boyer_moore_search, text1, non_existing_substring)}"
)

print(f"KMP (existing): {measure_time(kmp_search, text1, existing_substring)}")
print(f"KMP (non-existing): {measure_time(kmp_search, text1, non_existing_substring)}")

print(
    f"Rabin-Karp (existing): {measure_time(rabin_karp_search, text1, existing_substring)}"
)
print(
    f"Rabin-Karp (non-existing): {measure_time(rabin_karp_search, text1, non_existing_substring)}"
)

# Вимірювання часу для статті 2
print("Article 2:")
print(
    f"Boyer-Moore (existing): {measure_time(boyer_moore_search, text2, existing_substring)}"
)
print(
    f"Boyer-Moore (non-existing): {measure_time(boyer_moore_search, text2, non_existing_substring)}"
)

print(f"KMP (existing): {measure_time(kmp_search, text2, existing_substring)}")
print(f"KMP (non-existing): {measure_time(kmp_search, text2, non_existing_substring)}")

print(
    f"Rabin-Karp (existing): {measure_time(rabin_karp_search, text2, existing_substring)}"
)
print(
    f"Rabin-Karp (non-existing): {measure_time(rabin_karp_search, text2, non_existing_substring)}"
)


# Article 1:

# Boyer-Moore (existing): 0.931506378999984
# Boyer-Moore (non-existing): 0.4010898209999141

# KMP (existing): 4.286350661999677
# KMP (non-existing): 4.4682860170014465

# Rabin-Karp (existing): 9.509096677000343
# Rabin-Karp (non-existing): 9.70561644100053

# Article 2:

# Boyer-Moore (existing): 1.4283098630003224
# Boyer-Moore (non-existing): 0.6422397300011653

# KMP (existing): 6.998151818999759
# KMP (non-existing): 7.01754259900008

# Rabin-Karp (existing): 14.642822736999733
# Rabin-Karp (non-existing): 15.205429467001522