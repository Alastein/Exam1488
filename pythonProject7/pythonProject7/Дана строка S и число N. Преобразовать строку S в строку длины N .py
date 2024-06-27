s, n = "Hello", 8
transformed_s = s[-n:] if len(s) > n else '.' * (n - len(s)) + s
print(transformed_s)  # Output: "...Hello"
