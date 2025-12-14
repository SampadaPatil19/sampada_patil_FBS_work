"""
6.  Write a Python program to find the two numbers whose product is 
maximum among all the pairs in a given list of numbers. Use the 
Python set.
"""

def max_product_pair(nums):
    nums = list(set(nums))   # remove duplicates
    nums.sort()

    return nums[-1] * nums[-2]


numbers = [1, 10, 2, 6, 5, 10]
print("Maximum Product:", max_product_pair(numbers))
