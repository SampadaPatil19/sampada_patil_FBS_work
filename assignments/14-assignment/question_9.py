"""
9. Write a Python program to find all the unique combinations of 3 
numbers from a given list of numbers, adding up to a target number. 
"""

def three_sum(nums, target):
    nums = sorted(set(nums))
    result = []

    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    result.append((nums[i], nums[j], nums[k]))

    return result


numbers = [1, 2, 3, 4, 5, 6]
target = 10

print("3-number combinations:", three_sum(numbers, target))
