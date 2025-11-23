# 5.  Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

def checkElement(li, ele):
    count = 0
    for i in li:
        if i == ele:
            count += 1

    if count > 0:
        return f"Element {ele} is present {count} times in list."
    else:
        return f"Element {ele} is not present in list."

li = [10, 20, 30 , 40, 10]
ele = int(input('Enter the number in [10, 20, 30, 40]: '))
print(checkElement(li, ele))