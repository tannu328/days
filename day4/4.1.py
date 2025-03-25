#Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are included. If there are no duplicates, return 0.
from collections import Counter

def count_duplicates(s):

    char_count = Counter(s)
    

    duplicate_count = 0
    

    for count in char_count.values():
        if count > 1:
            duplicate_count += count - 1
    
    return duplicate_count


s = "hello Miss"
result = count_duplicates(s)
print(f"The number of duplicate characters is: {result}")
