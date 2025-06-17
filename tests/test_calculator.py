
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


def test_calculator_exit(monkeypatch, capsys):
    """
    Test the calculator function to ensure it exits correctly when 'exit' is entered.

    AAA pattern:
    -Arrange: Prepare the input 'exit' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure the program exits without any errors.
    """
    #Arrange
    user_input = "exit\n"  # Simulate user input for exiting the calculator
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering 'exit
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    
    # Assert
    captured = capsys.readouterr()
    assert "Exiting calculator. Goodbye!" in captured.out  # Ensure the exit message is printed
    assert exc_info.type == SystemExit  # Ensure the SystemExit exception is raised
    assert exc_info.value.code == 0  # Ensure the exit code is 0, indicating a normal exit


def test_calculator_help_command(monkeypatch, capsys):
    """
    Test the calculator function to ensure it displays help when 'help' is entered.

    AAA pattern:
    -Arrange: Prepare the input 'help' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure the help message is printed correctly.
    """
    
    # Arrange
    user_input = "help\nexit\n"  # Simulate user input for help and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering 'help'
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Calculator REPL Help:" in captured.out  # Ensure the help message is printed
    assert "Exiting calculator. Goodbye!" in captured.out  # Ensure the exit message is printed



def test_calculator_invalid_input(monkeypatch, capsys):
    """
    Test the calculator function to ensure it handles invalid input gracefully.

    AAA pattern:
    -Arrange: Prepare the input 'invalid_command' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure an error message is printed for invalid input.
    """
    
    # Arrange
    user_input = "invalid input\nadd 5\nexit\n"  # Simulate user input with an invalid command and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering invalid command

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()


    # Assert
    captured = capsys.readouterr()
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out  # Ensure the error message is printed
    assert "Type 'help' for usage instructions." in captured.out  # Ensure the help message is suggested
    


def test_calculator_addition(monkeypatch, capsys):
    """
    Test the calculator function to ensure it performs addition correctly.

    AAA pattern:
    -Arrange: Prepare the input 'add 5 3' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure the result of addition is printed correctly.
    """
    
    # Arrange
    user_input = "add 5 3\nexit\n"  # Simulate user input for addition and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering addition command
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: AddCalculator: 5.0 + 3.0 = 8.0" in captured.out  # Ensure the result of addition is printed


def test_calculator_subtraction(monkeypatch, capsys):
    """
    Test the calculator function to ensure it performs subtraction correctly.

    AAA pattern:
    -Arrange: Prepare the input 'subtract 10 4' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure the result of subtraction is printed correctly.
    """
    
    # Arrange
    user_input = "subtract 10 4\nexit\n"  # Simulate user input for subtraction and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering subtraction command
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: SubtractCalculator: 10.0 - 4.0 = 6.0" in captured.out  # Ensure the result of subtraction is printed

def test_calculator_multiplication(monkeypatch, capsys):
    """
    Test the calculator function to ensure it performs multiplication correctly.
    AAA pattern:
    -Arrange: Prepare the input 'multiply 2 3' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure the result of multiplication is printed correctly.
    """
    
    # Arrange
    user_input = "multiply 2 3\nexit\n"  # Simulate user input for multiplication and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering multiplication command
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: MultiplyCalculator: 2.0 * 3.0 = 6.0" in captured.out  # Ensure the result of multiplication is printed

def test_calculator_division(monkeypatch, capsys):
    """
    Test the calculator function to ensure it performs division correctly.
    AAA pattern:
    -Arrange: Prepare the input 'divide 8 2' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure the result of division is printed correctly.
    """
    
    # Arrange
    user_input = "divide 8 2\nexit\n"  # Simulate user input for division and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering division command
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: DivideCalculator: 8.0 / 2.0 = 4.0" in captured.out  # Ensure the result of division is printed


def test_calculator_division_by_zero(monkeypatch, capsys):
    """
    Test the calculator function to ensure it handles division by zero correctly.
    AAA pattern:
    -Arrange: Prepare the input 'divide 8 0' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure an error message is printed for division by zero.
    """
    
    # Arrange
    user_input = "divide 8 0\nexit\n"  # Simulate user input for division by zero and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering division command
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out  # Ensure the error message for division by zero is printed


def test_calculator_history(monkeypatch, capsys):
    """
    Test the calculator function to ensure it displays the history of calculations correctly.
    AAA pattern:
    -Arrange: Prepare the input 'history' to simulate user input.
    -Act: Call the calculator function with the input.
    -Assert: Ensure the history of calculations is printed correctly.
    """
    
    # Arrange
    user_input = "add 5 3\nsubtract 10 4\nhistory\nexit\n"  # Simulate user input for addition, subtraction, history, and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering commands
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Calculation History:" in captured.out  # Ensure the history header is printed
    assert "1: AddCalculator: 5.0 + 3.0 = 8.0" in captured.out  # Ensure the first calculation is in history
    assert "2: SubtractCalculator: 10.0 - 4.0 = 6.0" in captured.out  # Ensure the second calculation is in history

def test_calculator_invalid_number_input(monkeypatch, capsys):
    """
    Test the calculator function to ensure it handles invalid number input gracefully.
    AAA pattern:
    -Arrange: Prepare the input 'add five three' to simulate user input with invalid numbers.
    -Act: Call the calculator function with the input.
    -Assert: Ensure an error message is printed for invalid number input.
    """
    
    # Arrange
    user_input = "add five three\nexit\n"  # Simulate user input with invalid numbers and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering invalid command
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out  # Ensure the error message for invalid input is printed
    assert "Type 'help' for usage instructions." in captured.out  # Ensure the help message is suggested


def test_unsupported_operation(monkeypatch, capsys):
    """
    Test the calculator function to ensure it handles unsupported operations gracefully.
    AAA pattern:
    -Arrange: Prepare the input 'modulus 5 3' to simulate user input with an unsupported operation.
    -Act: Call the calculator function with the input.
    -Assert: Ensure an error message is printed for unsupported operations.
    """
    
    # Arrange
    user_input = "modulus 5 3\nexit\n"  # Simulate user input with an unsupported operation and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering unsupported command
    
    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Operation 'modulus' is not supported." in captured.out  # Ensure the error message for unsupported operation is printed
    assert "Type 'help' for usage instructions." in captured.out  # Ensure the help message is suggested


def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    """
    Test the calculator's handling of keyboard interrupts(Ctrl+C).

    AAA pattern:
    -Arrange: Simulate a keyboard interrupt by raising KeyboardInterrupt.
    -Act: Call the calculator function and expect a KeyboardInterrupt.
    -Assert: Ensure the program exits gracefully without any errors.
    """

    # Arrange
    def mock_input(prompt):
        raise KeyboardInterrupt
    monkeypatch.setattr('builtins.input', mock_input)  # Mock input to simulate keyboard interrupt

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Keyboard interrupt detected. Exiting calculator. Goodbye!" in captured.out  # Ensure the exit message is printed


def test_calculator_eof_error(monkeypatch, capsys):
    """
    Test the calculator's handling of EOFError (Ctrl+D).

    AAA pattern:
    -Arrange: Simulate an EOFError by raising EOFError.
    -Act: Call the calculator function and expect an EOFError.
    -Assert: Ensure the program exits gracefully without any errors.
    """

    # Arrange
    def mock_input(prompt):
        raise EOFError
    monkeypatch.setattr('builtins.input', mock_input)  # Mock input to simulate EOFError

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "EOF detected. Exiting calculator. Goodbye!" in captured.out  # Ensure the exit message is printed



def test_calculator_unexpected_error(monkeypatch, capsys):
    """
    Test the calculator's handling of unexpected errors during calculation execution.

    AAA pattern:
    -Arrange: mock the execute method to raise an unexpected error.
    -Act: Call the calculator function and expect an unexpected error.
    -Assert: Ensure the program exits gracefully without any errors.
    """

    # Arrange
    class MockCalculator:
        def excute(self):
            raise Exception("Unexpected error")
        
        def __str__(self):
            return "MockCalculation"
        
    def mock_create_calculator(operation, a, b):
        return MockCalculator()
    
    monkeypatch.setattr('app.calculator.CalculatorFactory.create_calculator', mock_create_calculator)  # Mock the factory method to return a mock calculator
    user_input = "add 5 3\nexit\n"  # Simulate user input for addition and then exit
    monkeypatch.setattr('sys.stdin', StringIO(user_input))  # Mock input to simulate user entering addition command

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "An unexpected error occurred: Unexpected error" in captured.out  # Ensure the unexpected error message is printed
    









