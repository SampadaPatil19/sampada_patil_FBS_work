"""
4. Write a Python program that finds all pairs of elements in a list whose 
sum is equal to a given value.
"""

def find_pairs(nums, target):
    pairs = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))

    return pairs


numbers = [2, 4, 3, 5, 7, 8]
target = 9

print("Pairs with sum =", target, ":", find_pairs(numbers, target))
