def double_swap(s, c1, c2):

    translation_table = str.maketrans(f"{c1}{c2}", f"{c2}{c1}")
    return s.translate(translation_table)


print(double_swap("aabbccc", "a", "b"))
print(double_swap("random w#rds writt&n h&r&", "#", "&"))
print(double_swap("128 895 556 788 999", "8", "9"))  
