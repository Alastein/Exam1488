a, b, c = 3, 4, 5
sides = sorted([a, b, c])
is_right = sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
print(is_right)  # Output: True
