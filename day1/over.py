def calculate_overs_and_balls(balls):

    overs = balls // 6  # Integer division to get the number of overs
    remaining_balls = balls % 6  # Remainder gives the number of balls left

    # Return the value in the format overs.balls as a float
    return float(f"{overs}.{remaining_balls}")

# Example usage:
balls_bowled = int(input("Enter the number of balls bowled: "))
result = calculate_overs_and_balls(balls_bowled)
print(f"{balls_bowled} balls is equal to {result} overs.")
