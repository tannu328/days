#Create a function that returns the selected filename from a path. Include the extension in your answer.
import os

def get_filename(path):
    return os.path.basename(path)

file_path = "dessktop/classes/days/day7/7.2.py"
filename = get_filename(file_path)
print(filename)
