#In cricket, an over consists of six deliveries a bowler bowls from one end. Create a program that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.

def calculate_overs_and_balls(balls):

    overs = balls // 6
    remaining_balls = balls % 6

    return float(f"{overs}.{remaining_balls}")


balls_bowled = int(input("Enter the number of balls bowled: "))
result = calculate_overs_and_balls(balls_bowled)
print(f"{balls_bowled} balls is equal to {result} overs.")
