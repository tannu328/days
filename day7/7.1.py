def check_last_character(name):

    return name[-1].lower() == 'a'

def check_first_last_char(name):

    return name[0].lower() == 'd' and name[-1].lower() == 'd'

def main():
    name = input("Enter a name: ")


    last_char_check = check_last_character(name)
    print(f"Does the last character is 'a'? {last_char_check}")

    
    first_last_char_check = check_first_last_char(name)
    print(f"Are the first and last characters both 'd'? {first_last_char_check}")


main()
