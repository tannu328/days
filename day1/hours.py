def convert_to_seconds(time_str):
    # Split the time string into hours, minutes, and seconds
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    # Convert hours and minutes into seconds and add the given seconds
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

# Example usage:
time_str = input("Enter time in HH:MM:SS format: ")
result = convert_to_seconds(time_str)
print(f"{time_str} is equal to {result} seconds.")
