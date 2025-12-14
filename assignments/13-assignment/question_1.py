# 1. Python Program to Add a Key-Value Pair to the Dictionary


# Approach 1
my_dict = {'name': 'Gunjan', 'age': 23}

print("Dictionary before adding:", my_dict)

my_dict['city'] = 'Pune'

print("Dictionary after adding:", my_dict)


# Approach 2 
# add multiple key-value pairs based on user input
num_pairs = int(input("How many key-value pairs do you want to add? "))

for i in range(num_pairs):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for {key}: ")
    my_dict[key] = value

print("Dictionary after adding user inputs:", my_dict)


