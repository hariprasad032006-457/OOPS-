# Function to add all numbers passed as arguments
def add_all_num(*args):

    total=sum(args)
    for num in args:
        print(num)
    print("Total:", total)
add_all_num(1, 2, 3, 4, 5)

# Function to convert keyword arguments to a list
def dict_to_list(**kwargs):
    return list(kwargs.items())

result = dict_to_list(name="John", age=30, city="New York")
print(result)