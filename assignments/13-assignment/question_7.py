# 7. Python Program to Remove the Given Key from a Dictionary

"""
dict = {1:2, 2:4, 3:6}
print(type(dict))
dict.pop(1)
print(dict)
"""


def removeGivenItem(dict):
    key_to_remove = input('Which Key You wanna remove? ')

    dict.pop(key_to_remove)

    return dict

item_quantity = {
    "Pen": 5,
    "Notebook": 3,
    "Pencil": 10
}
print(removeGivenItem(item_quantity))
