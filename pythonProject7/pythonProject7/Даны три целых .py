def transform_numbers(a, b, c):
    def transform(n):
        if n < 0:
            return n ** 2
        elif n > 0:
            return n ** 3
        else:
            return n

    return transform(a), transform(b), transform(c)


# Пример использования функции
a, b, c = -3, 0, 2
result = transform_numbers(a, b, c)
print(result)  # (9, 0, 8)
