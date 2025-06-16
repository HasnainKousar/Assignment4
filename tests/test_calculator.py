
import sys
import pytest
from io import StringIO
from app.calculator import calculator, display_help, display_history

def test_display_help(capsys):
    """    
    Test the display_help function to ensure it prints the help message correctly.

    AAA pattern:
    Arrange: Prepare the expected output.(none needed here)
    Act: Call the display_help function.
    Assert: Capture the output and compare it with the expected help message.
    """

    #Arrange
    #no specific arrangement needed for this test


    #Act
    display_help() 


    #Assert
    
    captured = capsys.readouterr()
    expected_output = """
Calculator REPL Help:
=========================
This is a simple command-line calculator that supports basic arithmetic operations and maintains a history of calculations.

Supported Operations:
- add <num1> <num2>: Adds two numbers.
- subtract <num1> <num2>: Subtracts the second number from the first.
- multiply <num1> <num2>: Multiplies two numbers.
- divide <num1> <num2>: Divides the first number by the second (cannot divide by zero).

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
"""
    assert captured.out.strip() == expected_output.strip() # Ensure the output matches the expected help message


def test_display_history_empty(capsys):
    """
    Test the display_history function with an empty history list.

    AAA pattern:
    Arrange: Prepare an empty history list.
    Act: Call the display_history function.
    Assert: Capture the output and ensure it indicates no calculations were performed.
    """
    
    # Arrange
    history = []  # Empty history list

    # Act
    display_history(history)

    # Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations performed yet."  # Ensure the output indicates no calculations were performed


def test_display_history_with_calculations(capsys):
    """
    Test the display_history function with a non-empty history list.

    AAA pattern:
    Arrange: Prepare a history list with Calculation objects.
    Act: Call the display_history function.
    Assert: Capture the output and ensure it displays the calculations correctly.
    """
    
    # Arrange
    history = [
        "AddCalculator: 5.0 + 3.0 = 8.0",
        "SubtractCalculator: 10.0 - 4.0 = 6.0",
        "MultiplyCalculator: 2.0 * 3.0 = 6.0",
        "DivideCalculator: 8.0 / 2.0 = 4.0"
    ]

    # Act
    display_history(history)

    # Assert
    captured = capsys.readouterr()
    expected_output = """Calculation History:
1: AddCalculator: 5.0 + 3.0 = 8.0
2: SubtractCalculator: 10.0 - 4.0 = 6.0
3: MultiplyCalculator: 2.0 * 3.0 = 6.0
4: DivideCalculator: 8.0 / 2.0 = 4.0"""
    
    assert captured.out.strip() == expected_output.strip() # Ensure the output matches the expected history format




