def validation(pin):
    if len (pin) == 6 and pin.isdigit():
        return True
    else:
        return False
    
pin = input("enter pin")

if validation(pin):
    print("pin is valid")
else:
    print("invalid pin please enter 6 digits pin")