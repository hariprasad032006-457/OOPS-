"""Practice Python's built-in all() function."""

numbers = [1, 2, 3, 4, 5]
print("All values are truthy:", all(numbers))

values_with_zero = [1, 2, 0, 4]
print("All values are truthy:", all(values_with_zero))
