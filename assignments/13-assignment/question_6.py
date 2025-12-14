# 6. Python Program to Multiply All the Items in a Dictionary

def mulDictVal(dict):
    total_hours = 1

    for item in dict.values():
        total_hours *= item
    
    return total_hours

working_hours = {'Gunjan' : 8, 'Sampada' : 6, 'Ayush' : 8}
print(mulDictVal(working_hours))