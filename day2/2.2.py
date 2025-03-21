def calculate_overs_and_balls(balls):

    overs = balls // 6
    remaining_balls = balls % 6

    return float(f"{overs}.{remaining_balls}")


balls_bowled = int(input("Enter the number of balls bowled: "))
result = calculate_overs_and_balls(balls_bowled)
print(f"{balls_bowled} balls is equal to {result} overs.")
