"""
This module provides a professional-grade calculator that supports basic 
arithmetic operations and maintains a history of calculations.

We use the CalculatorFactory to create instances of Calculation objects based on user input.
We also include addtional features such as displaying help messages and maintaining a history of calculations.

we will use "look before you leap" and "easier to ask for forgiveness than permission" principles.
This will ensure the calculatr is user-friendly and handles errors gracefully.

"""

import sys
from typing import List
import readline 
from app.calculation import CalculatorFactory, Calculation



def display_help() -> None:
    """
    Displays the help message with usage instructions and supported operations.
    """
    help_message = """
Calculator REPL Help:
=========================
This is a simple command-line calculator that supports basic arithmetic operations and maintains a history of calculations.

Supported Operations:
- add <num1> <num2>: Adds two numbers.
- subtract <num1> <num2>: Subtracts the second number from the first.
- multiply <num1> <num2>: Multiplies two numbers.
- divide <num1> <num2>: Divides the first number by the second (cannot divide by zero).
- power <num1> <num2>: Raises the first number to the power of the second.

special commands:
- help: Displays this help message.
- history: Displays the history of calculations performed during the session.
- exit: Exits the calculator.

Example Usage:

format:
<operation> <number1> <number2>

Example commands:
add 5 3
subtract 10 4
multiply 2 3
divide 8 2
power 2 3
"""
    # Display the help message when the user types 'help'
    print(help_message)



#history of calculations performed during the session.
def display_history(history: List[Calculation]) -> None:
    """
    This function displays the history of calculations performed during the session.
    
    Parameters:
        history (List[Calculation]): A list of Calculation objects representing the history of calculations.
    """
    # Check if the history is empty
    if not history:
        print("No calculations performed yet.") #print a message if the history is empty
        return
    
    # If history is not empty, print each calculation
    else:
        print("Calculation History:")
        # Enumerate through the history list to display each calculation with its index starting from 1
        for i, calculation in enumerate(history, start=1):
            print(f"{i}: {calculation}")



def calculator():
    """
    Professional-grade calculator that supports basic arithmetic operations
    and maintains a history of calculations.

    This function showcases both LBYL and EAFP principles in error handling.
    """

    # Initialize the history list to store calculations
    history = []
    
    # Set up the command-line interface
    print("Welcome to the Calculator REPL!")
    print("Type 'help' for usage instructions or 'exit' to quit.")
    
    # Main loop to read user input and perform calculations
    while True:

        #try-except block to handle user input and potential errors
        try:
            #ask the user for input
            user_input = input(">>" ).strip()

            # Check if the input is empty or a special command
            if not user_input:
               continue  # Skip empty input
           
            #check if the user wants to exit
            elif user_input.lower() == "exit":
               print("Exiting calculator. Goodbye!") #print a message when the user wants to exit
               sys.exit(0)  # Exit the program gracefully
            
            #check if the user wants help           
            elif user_input.lower() == "help":
               display_help()
               continue
           
            #check if the user wants to see the history
            elif user_input.lower() == "history":
               display_history(history)
               continue

            #try to parse the user input into operation and numbers
            # If the input is not a special command, split it into operation and numbers
            # The expected format is: <operation> <num1> <num2>
            try:
                operation, num1_str, num2_str = user_input.split() #spliyt the input into operation and two numbers

                num1 = float(num1_str) # Convert the first number to float
                num2 = float(num2_str) # Convert the second number to float

            # If the input format is incorrect, raise a ValueError
            except ValueError:
                print("Invalid input. Please follow the format: <operation> <num1> <num2>") 
                print("Type 'help' for usage instructions.")
                continue
            
            #try to create a calculator object based on the operation
            try:
                # Create a Calculation object using the CalculatorFactory
                calculation = CalculatorFactory.create_calculator(operation, num1, num2)
            # If the operation is not recognized, raise a ValueError
            except ValueError as e:
                print(f"Error: {e}")
                print("Type 'help' for usage instructions.")
                continue
            
            #try to execute the calculation
            try:
            # Execute the calculation and get the result
            # The excute method will perform the calculation based on the operation
                result = calculation.excute()

            #raise a ZeroDivisionError if the operation is division and the second number is zero
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
                print("please enter a non-zero number for division.")
                continue
            
            # If any other unexpected error occurs, print a generic error message
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue

            # If the calculation is successful, print the result
            # convert the result to string for display
            result_str: str = f'{calculation}'

            # Print the result of the calculation
            print(f"Result: {result_str}\n")

            # Append the calculation to the history
            history.append(calculation)  # Store the calculation in history

        # Handle keyboard interrupts (Ctrl+C) and EOF (Ctrl+D)
        except KeyboardInterrupt:
            print("\nExiting calculator. Goodbye!")
            sys.exit(0)
        except EOFError:
            print("\nExiting calculator. Goodbye!")
            sys.exit(0)


# if the script is run directly, start the calculator REPL
if __name__ == "__main__":
    calculator()


