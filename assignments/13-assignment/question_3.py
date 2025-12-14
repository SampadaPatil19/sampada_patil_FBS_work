# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not


def checkIfPresent():
    # create dictionary
    dict = {'name': 'Gunjan', 'age': 23, 'city': 'Pune'}

    key_to_check = input("Enter the key to check in the dictionary: ")

    # Check if the key exists
    if key_to_check in dict:
        print(f"The key '{key_to_check}' exists in the dictionary.")
        print(f"Its value is: {dict[key_to_check]}")
    else:
        print(f"The key '{key_to_check}' does not exist in the dictionary.")

checkIfPresent()