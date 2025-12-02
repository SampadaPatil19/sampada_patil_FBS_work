# 6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

"""str = 'Sampada Patil'

print(str.replace(" ", '-'))"""

def replaceWithHypen(str):
    new_str = ''

    for ch in str:
        if ch == ' ':
            new_str += '-'
        else:
            new_str += ch

    # print(new_str)    
    return new_str

str = input('Enter a String: ')
result = replaceWithHypen(str)
print(result)