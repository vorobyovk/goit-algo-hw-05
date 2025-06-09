class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]
        # if self.table[key_hash] is None: # Логічна помилка: цей рядок ніколи не виконається як True.
        # Пояснення:
        # **якщо не помиляюсь**, у Python порожній список ніколи не є None.
        # Він просто є порожнім списком, і його логічне значення є False, але це не те саме, що None.
        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        # if self.table[key_hash] is not None:
        # Аналогічна ситуація, як у методі 'insert' — оригінальний рядок можна видалити без негативних наслідків.
        # (або я щось не розумію)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        for i, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                self.table[key_hash].pop(i)
                return True
        return False


# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
print(H.table)

H.insert("apple", 10)
print(H.table)
print(H.get("apple"))  # Виведе: 10

H.insert("orange", 20)
H.insert("banana", 30)
print(H.table)

H.insert("apple", 50)
print(H.table)

print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30
print(H.get("apple"))  # Виведе: 50(!)
print(H.table)

H.delete("apple")
print(H.get("apple"))  # Виведе: None
print(H.table)