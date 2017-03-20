#!/usr/bin/env python3
import sys


def GetInput():
    """
    Ask the user for the PIN no more three times
    The input is 4 digits only 
    Assume the user's PIN is "1234"
    """
    for i in range(3):
        print("Enter your PIN:")
        pin = input()
        # Check the length
        if len(pin) != 4:
            print("Invalid PIN length. Correct format is: <9876>")
        # Check the type
        elif not pin.isdigit():
            print("Invalid PIN character. Correct format is: <9876>")  
        # Check the code
        elif pin == "1234":
            print("Your PIN is correct")
            return
        print("Your PIN is incorrect")
        
    print("Your bank card is blocked")
    exit(1)        
            

# Main Function
def main():
    """
    Test Function.
    """
    GetInput()
    


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
