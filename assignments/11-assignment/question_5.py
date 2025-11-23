# 5. Python Program to Sort a List According to the Length of the Elements within the list.

"""
Approach 1
def sortAccordingToLen(list):
    final_lsit = sorted(list, key=len)

    return final_lsit

list = ['Python', 'C', 'JavaScript', 'Java']

print(sortAccordingToLen(list))
"""

def sortAccordingToLen(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return list


list = ['Python', 'C', 'JavaScript', 'Java']

print(sortAccordingToLen(list))