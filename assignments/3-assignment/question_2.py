# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

ch = input("Enter any alphabet: ").lower()

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet only.")

elif ch in ['a', 'e', 'i', 'o', 'u']:
    print(f"{ch} is a VOWEL.")

else:
    print(f"{ch} is a CONSONANT.")
