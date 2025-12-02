def exchangeLastAndFirstChar(s):
    if s == "" or (s[1:] == ""):
        print("New string:", s)
    else:
        first = s[0]
        last = s[-1]

        middle = ""

        for i in range(1, len(s) - 1):
            middle = middle + s[i]

        new_string = last + middle + first

    return f"New string is '{new_string}'"

s = input('Enter a String: ')
result = exchangeLastAndFirstChar(s)
print(result)

