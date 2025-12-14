# 2. Python Program to Concatenate Two Dictionaries Into One

def concat_dict():
    # Create two dictionaries
    dict1 = {'name' : 'Gunjan', 'last_name': 'Patil'}
    dict2 = {'course' : 'CSE', 'Department' : 'Computer Science'}
    """
    print("Dictionary 1:", dict1)
    print("Dictionary 2:", dict2)"""

    # Concatenate dict2 into dict1 using update method
    dict1.update(dict2)

    print("CONCATINATED DICTIONARY:\n", dict1)

concat_dict()