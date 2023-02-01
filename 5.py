# both work, not sure which is more efficient

""" 
def get_summed_pair(lst, val):
    for i in range(len(lst) - 2):
        for j in range(1, len(lst) - 1):
            if lst[i] + lst[j] == val:
                return (lst[i], lst[j])
    return 'no pairs sum to the target' 
"""

def get_summed_pair(lst, val):
    lst.sort()
    left = 0
    right = len(lst) - 1
    while left < right:
        tot = lst[left] + lst[right]
        if tot == val:
            return (lst[left], lst[right])
        if tot < val:
            left += 1
        else:
            right -= 1
    return 'no pairs sum to the target'

print(get_summed_pair([5, 10, 4, 7, 6, 2], 9))
