# 11. Write a program to accept an integer amount from user and tell minimum 
# number of notes needed for representing that amount

amount = int(input('Enter the Amount: '))

notes = [2000, 500, 200, 100, 50, 10]

notes_count = {}

for note in notes:
    if amount >= note:
        notes_count[note] = amount // note
        amount = amount % note

for key, val in notes_count.items():
    print(f'{key} : {val}')