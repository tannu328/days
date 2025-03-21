def convert_to_seconds(time):

    hours, minutes, seconds = map(int, time.split(':'))
    

    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds


time = input("Enter time in HH:MM:SS format: ")
result = convert_to_seconds(time)
print(f"{time} is equal to {result} seconds.")
