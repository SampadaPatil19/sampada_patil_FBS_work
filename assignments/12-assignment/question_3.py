# 3.  Python Program to Detect if Two Strings are Anagrams.

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1

    for val in count.values():
        if val != 0:
            return False

    return True


print(is_anagram('sampada', 'sampada'))