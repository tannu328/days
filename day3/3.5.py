def max_difference(tupList):

    max_diff = 0
    

    for tup in tupList:

        diff = abs(tup[1] - tup[0])
        

        if diff > max_diff:
            max_diff = diff
    
    return max_diff


tupList = [(5, 8), (2, 1), (10, 9), (1, 9)]
result = max_difference(tupList)
print(f"The maximum difference is: {result}")
