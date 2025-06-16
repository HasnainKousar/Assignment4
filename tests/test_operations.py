"""
Unit tests for the Operations class.

Tests include addition, subtraction, multiplication, division, and error handling for division by zero.
It will cover both postive and negative scenarios to ensure the Operations class' static methods work correctly.

Tests are organized following AAA (Arrange, Act, Assert) pattern for clarity and maintainability.
"""


from app.operations import Operations
import pytest

def test_add_positive():
    """
    Test addition of two postive numbers.
    
    This test checks if the add method correctly sums two positive float numbers. 
    """

    #Arrange
    a = 5.0
    b = 3.0
    expected_result = 8.0

    #Act
    result = Operations.add(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_add_negative():
    """
    Test addition of two negative numbers.

    This test checks if the add method correctly sums two negative float numbers.
    """

    #Arrange
    a = -5.0
    b = -3.0
    expected_result = -8.0

    #Act
    result = Operations.add(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"

def test_mixed_addition():
    """
    Test addition of a positive and a negative number.

    This test checks if the add method correctly sums a positive and a negative float number.
    """

    #Arrange
    a = 5.0
    b = -3.0
    expected_result = 2.0

    #Act
    result = Operations.add(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"

def test_subtract_positive():
    """
    Test subtraction of two positive numbers.

    This test checks if the subtract method correctly subtracts two positive float numbers.
    """
    #Arrange
    a = 9.0
    b = 4.0
    expected_result = 5.0

    #Act
    result = Operations.subtract(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


def test_subtract_negative():
    """
    Test subtraction of two negative numbers.

    This test checks if the subtract method correctly subtracts two negative float numbers.
    """
    #Arrange
    a = -9.0
    b = -4.0
    expected_result = -5.0

    #Act
    result = Operations.subtract(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"

def test_mixed_subtraction():
    """
    Test subtraction of a positive and a negative number.
    This test checks if the subtract method correctly subtracts a positive and a negative float number.
    """
    #Arrange
    a = 5.0
    b = -3.0
    expected_result = 8.0

    #Act
    result = Operations.subtract(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"

def test_multiply_positive():
    """
    Test multiplication of two positive numbers.
    This test checks if the multiply method correctly multiplies two positive float numbers.
    """
    #Arrange
    a = 6.0
    b = 7.0
    expected_result = 42.0

    #Act
    result = Operations.multiply(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"

def test_multiply_negative():
    """
    Test multiplication of two negative numbers.
    This test checks if the multiply method correctly multiplies two negative float numbers.
    """
    #Arrange
    a = -6.0
    b = -7.0
    expected_result = 42.0

    #Act
    result = Operations.multiply(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"

def test_mixed_multiplication():
    """
    Test multiplication of a positive and a negative number.
    This test checks if the multiply method correctly multiplies a positive and a negative float number.
    """
    #Arrange
    a = 6.0
    b = -7.0
    expected_result = -42.0

    #Act
    result = Operations.multiply(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"

def test_divide_positive():
    """
    Test division of two positive numbers.
    This test checks if the divide method correctly divides two positive float numbers.
    """
    #Arrange
    a = 10.0
    b = 2.0
    expected_result = 5.0

    #Act
    result = Operations.divide(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"

def test_divide_negative():
    """
    Test division of two negative numbers.
    This test checks if the divide method correctly divides two negative float numbers.
    """
    #Arrange
    a = -10.0
    b = -2.0
    expected_result = 5.0

    #Act
    result = Operations.divide(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"

def test_mixed_division():
    """
    Test division of a positive and a negative number.
    This test checks if the divide method correctly divides a positive and a negative float number.
    """
    #Arrange
    a = 10.0
    b = -2.0
    expected_result = -5.0

    #Act
    result = Operations.divide(a, b)

    #Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"



def test_divide_by_zero():
    """
    Test division by zero.
    This test checks if the divide method raises a ValueError when attempting to divide by zero.
    """
    #Arrange
    a = 10.0
    b = 0.0

    #Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        Operations.divide(a, b)






