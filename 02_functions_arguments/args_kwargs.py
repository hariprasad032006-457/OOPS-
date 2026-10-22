"""Practice *args and **kwargs."""


def add_all_numbers(*args):
    """Print all supplied numbers and their sum."""
    print("Numbers:", *args)
    print("Total:", sum(args))


def kwargs_to_list(**kwargs):
    """Return keyword arguments as key/value pairs."""
    return list(kwargs.items())


if __name__ == "__main__":
    add_all_numbers(1, 2, 3, 4, 5)
    print(kwargs_to_list(name="John", age=30, city="New York"))
