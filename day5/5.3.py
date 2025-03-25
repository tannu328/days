#Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.
from collections import Counter

def count_data_types(*args):
    
    types = [type(arg) for arg in args]
    

    type_counts = Counter(types)
    

    return list(type_counts.items())


print(count_data_types(1, "hello", 2.88, True, 2, "world", 1.99))

print(count_data_types(1, 2, 3))


print(count_data_types("apple", "banana", True, False, 100))
