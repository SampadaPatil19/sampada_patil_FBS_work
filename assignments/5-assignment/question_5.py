"""
Write a program to accept an integer amount from user and tell minimum  
number of notes needed for representing that amount. (Use looping to optimize  
the problem)
"""

amount = int(input('Enter the Amount in Rupee: '))

notes = [2000, 500, 200, 100, 50, 10]

note_count = {}

for note in notes:
    if amount >= note:
        note_count[note]  = amount // note
        amount = amount % note
    
else:
    print('You entered 0 Amount.')
    
for key, val in note_count.items():
    print(f'{key} : {val}')

