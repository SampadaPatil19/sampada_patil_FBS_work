"""
5.  Write a Python program to find the longest common prefix of all 
strings. Use the Python set.
"""

def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = ""
    min_length = min(len(s) for s in strings)

    for i in range(min_length):
        chars = set(s[i] for s in strings)
        if len(chars) == 1:
            prefix += chars.pop()
        else:
            break

    return prefix


words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(words))
