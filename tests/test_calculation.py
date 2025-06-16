"""
Tests for the calculation module of the application.

we will use unit tests and parameterized tests to ensure the calculator's functionality is robust and handles various scenarios.

"""

import pytest
from app.operations import Operations
from unittest.mock import patch
from app.calculation import (
    CalculatorFactory,
    Calculation,
    AddCalculator,
    SubtractCalculator,
    MultiplyCalculator,
    DivideCalculator,
)


#========== Test Cases for CalculatorFactory ===========

def test_calculator_factory_add():
    """
    Test the CalculatorFactory for addition operation.

    Test that the CalculatorFactory correctly creates an AddCalculator instance
    when the operation is 'add'.
    """

    #Arrange
    operation = 'add'
    a = 5.0
    b = 3.0

    #Act
    calc = CalculatorFactory.create_calculator(operation, a, b)

    #Assert
    assert isinstance(calc, AddCalculator)
    assert calc.a == a
    assert calc.b == b


    
def test_calculator_factory_subtract():
    """
    Test the CalculatorFactory for subtraction operation.

    Test that the CalculatorFactory correctly creates a SubtractCalculator instance
    when the operation is 'subtract'.
    """

    #Arrange
    operation = 'subtract'
    a = 8.0
    b = 5.0

    #Act
    calc = CalculatorFactory.create_calculator(operation, a, b)

    #Assert
    assert isinstance(calc, SubtractCalculator)
    assert calc.a == a
    assert calc.b == b



def test_calculator_factory_multiply():
    """
    Test the CalculatorFactory for multiplication operation.

    Test that the CalculatorFactory correctly creates a MultiplyCalculator instance
    when the operation is 'multiply'.
    """

    #Arrange
    operation = 'multiply'
    a = 4.0
    b = 2.5

    #Act
    calc = CalculatorFactory.create_calculator(operation, a, b)

    #Assert
    assert isinstance(calc, MultiplyCalculator)
    assert calc.a == a
    assert calc.b == b

def test_calculator_factory_divide():
    """
    Test the CalculatorFactory for division operation.
    Test that the CalculatorFactory correctly creates a DivideCalculator instance
    when the operation is 'divide'.
    """
    #Arrange
    operation = 'divide'
    a = 10.0
    b = 2.0

    #Act
    calc = CalculatorFactory.create_calculator(operation, a, b)

    #Assert
    assert isinstance(calc, DivideCalculator)
    assert calc.a == a
    assert calc.b == b


def test_calculator_factory_invalid_operation():
    """
    Test the CalculatorFactory with an invalid operation.

    Test that the CalculatorFactory raises a ValueError when an unsupported operation is provided.
    """
    #Arrange
    operation = 'invalid_operation'
    a = 5.0
    b = 3.0

    #Act & Assert
    with pytest.raises(ValueError) as e:
        # Attempt to create a calculator with an unsupported operation
        CalculatorFactory.create_calculator(operation, a, b)
    # Assert that a ValueError is raised with the expected message
    assert  f"Operation '{operation}' is not supported." in str(e.value) 
    
def test_calculator_factory_duplicate_registration():
    """
    Test the CalculatorFactory for duplicate registration of a calculator.

    This test checks if the CalculatorFactory raises a ValueError when trying to register
    a calculator with an operation that is already registered.
    """
    #Arrange and Act
    # Try to register the same calculator again
    with pytest.raises(ValueError) as e:
        @CalculatorFactory.register_calculator('add')
        class DuplicateAddCalculator(Calculation):
            operator_symbol = "+"
            def execute(self):
                return Operations.add(self.a, self.b)
            

                
    # Assert that a ValueError is raised with the expected message
    assert f"Calculation type 'add' already registered." in str(e.value)
    


# def test_duplicate_calculator_registration():
#     # Attempt to register another calculator for an already registered operation
#     with pytest.raises(ValueError, match="Calculaton type 'add' already registered."):
#         @CalculatorFactory.register_calculator("add")
#         class DummyAddCalculator(Calculation):
#             operator_symbol = "+"
#             def excute(self):
#                 return Operations.add(self.a, self.b)


#========== Test String Representation of Calculation Classes ===========

@patch.object(Operations, 'add', return_value=8.0)
def test_add_calculation_str(mock_add):
    """
    Test the string representation of AddCalculator.
    
    This test checks if the string representation of AddCalculator
    correctly formats the addition operation.
    """
    #Arrange
    a = 5.0
    b = 3.0
    calc = AddCalculator(a, b)

    #Act
    result_str = str(calc)

    #Assert
    assert result_str == "AddCalculator: 5.0 + 3.0 = 8.0"

@patch.object(Operations, 'subtract', return_value=3.0)
def test_subtract_calculation_str(mock_subtract):
    """
    Test the string representation of SubtractCalculator.
    
    This test checks if the string representation of SubtractCalculator
    correctly formats the subtraction operation.
    """
    #Arrange
    a = 8.0
    b = 5.0
    calc = SubtractCalculator(a, b)

    #Act
    result_str = str(calc)

    #Assert
    assert result_str == "SubtractCalculator: 8.0 - 5.0 = 3.0"

@patch.object(Operations, 'multiply', return_value=10.0)
def test_multiply_calculation_str(mock_multiply):
    """
    Test the string representation of MultiplyCalculator.
    
    This test checks if the string representation of MultiplyCalculator
    correctly formats the multiplication operation.
    """
    #Arrange
    a = 4.0
    b = 2.5
    calc = MultiplyCalculator(a, b)

    #Act
    result_str = str(calc)

    #Assert
    assert result_str == "MultiplyCalculator: 4.0 * 2.5 = 10.0"

@patch.object(Operations, 'divide', return_value=5.0)
def test_divide_calculation_str(mock_divide):
    """
    Test the string representation of DivideCalculator.
    
    This test checks if the string representation of DivideCalculator
    correctly formats the division operation.
    """
    #Arrange
    a = 10.0
    b = 2.0
    calc = DivideCalculator(a, b)

    #Act
    result_str = str(calc)

    #Assert
    assert result_str == "DivideCalculator: 10.0 / 2.0 = 5.0"










#========== Parameterized Tests for excute method ===========




#========== parameterized tests for string representation ===========
