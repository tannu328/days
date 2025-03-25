#Given a list nums where each integer is between 1 and 100, return a sorted list containing only duplicate numbers from the given nums list

from collections import Counter

def duplicate_nums(nums):

    num_count = Counter(nums)
    

    duplicates = [num for num, count in num_count.items() if count > 1]
    

    if not duplicates:
        return None
    

    return sorted(duplicates)


print(duplicate_nums([1, 20, 553, 40, 553, 5, 6]))
print(duplicate_nums([52,63, 70, 44,52, 77, 83, 99, 999,63, 100, 12, 54]))  
print(duplicate_nums([10, 32, 13, 64, 25, 64, 76, 88, 92, 10]))  
