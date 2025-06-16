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


#========== Positive Test Cases for Concrete Calculation Classes ===========

@patch.object(Operations, 'add', return_value=8.0)
def test_add_calculation_excute_positive(mock_add):
    """
    Test the execute method of AddCalculator for a positive scenario.
    
    
    This test verifies that the AddCalculator correctly calls the add method from Operations
    with provided operands and returns the expected result.
    """

    #Arrange
    a = 5.0
    b = 3.0
    expected_result = 8.0
    mock_add.return_value = expected_result # Mock the add method to return the expected result
    calc = AddCalculator(a, b)

    #Act
    result = calc.excute()

    #Assert
    assert result == expected_result


@patch.object(Operations, 'subtract', return_value=3.0)
def test_subtract_calculation_excute_positive(mock_subtract):
    """
    Test the execute method of SubtractCalculator for a positive scenario.
    
    This test verifies that the SubtractCalculator correctly calls the subtract method from Operations
    with provided operands and returns the expected result.
    """

    #Arrange
    a = 8.0
    b = 5.0
    expected_result = 3.0
    mock_subtract.return_value = expected_result
    calc = SubtractCalculator(a, b)

    #Act
    result = calc.excute()

    #Assert
    assert result == expected_result



@patch.object(Operations, 'multiply', return_value=10.0)
def test_multiply_calculation_excute_positive(mock_multiply):
    """
    Test the execute method of MultiplyCalculator for a positive scenario.
    
    This test verifies that the MultiplyCalculator correctly calls the multiply method from Operations
    with provided operands and returns the expected result.
    """

    #Arrange
    a = 4.0
    b = 2.5
    expected_result = 10.0
    mock_multiply.return_value = expected_result
    calc = MultiplyCalculator(a, b)

    #Act
    result = calc.excute()

    #Assert
    assert result == expected_result



@patch.object(Operations, 'divide', return_value=5.0)
def test_divide_calculation_excute_positive(mock_divide):
    """
    Test the execute method of DivideCalculator for a positive scenario.
    
    This test verifies that the DivideCalculator correctly calls the divide method from Operations
    with provided operands and returns the expected result.
    """

    #Arrange
    a = 10.0
    b = 2.0
    expected_result = 5.0
    mock_divide.return_value = expected_result
    calc = DivideCalculator(a, b)

    #Act
    result = calc.excute()

    #Assert
    assert result == expected_result


#========== Negative Test Cases for Concrete Calculation Classes ===========

@patch.object(Operations, 'add', side_effect=ValueError("Addtion error"))
def test_add_calculation_excute_negative(mock_add):
    """
    Test the execute method of AddCalculator for a negative scenario.
    
    This test verifies that the AddCalculator raises a ValueError when the add method from Operations fails.
    """

    #Arrange
    a = 5.0
    b = 3.0
    mock_add.side_effect = ValueError("Addition error")  # Mock the add method to raise a ValueError
    calc = AddCalculator(a, b)

    #Act & Assert
    with pytest.raises(ValueError) as e:
        calc.excute()
    
    assert str(e.value) == "Addition error"


@patch.object(Operations, 'subtract', side_effect=ValueError("Subtraction error"))
def test_subtract_calculation_excute_negative(mock_subtract):
    """
    Test the execute method of SubtractCalculator for a negative scenario.
    
    This test verifies that the SubtractCalculator raises a ValueError when the subtract method from Operations fails.
    """

    #Arrange
    a = 8.0
    b = 5.0
    mock_subtract.side_effect = ValueError("Subtraction error")
    calc = SubtractCalculator(a, b)

    #Act & Assert
    with pytest.raises(ValueError) as e:
        calc.excute()
    
    assert str(e.value) == "Subtraction error"


@patch.object(Operations, 'multiply', side_effect=ValueError("Multiplication error"))
def test_multiply_calculation_excute_negative(mock_multiply):
    """
    Test the execute method of MultiplyCalculator for a negative scenario.
    
    This test verifies that the MultiplyCalculator raises a ValueError when the multiply method from Operations fails.
    """

    #Arrange
    a = 4.0
    b = 2.5
    mock_multiply.side_effect = ValueError("Multiplication error")
    calc = MultiplyCalculator(a, b)

    #Act & Assert
    with pytest.raises(ValueError) as e:
        calc.excute()
    
    assert str(e.value) == "Multiplication error"


@patch.object(Operations, 'divide', side_effect=ValueError("Division error"))
def test_divide_calculation_excute_negative(mock_divide):
    """
    Test the execute method of DivideCalculator for a negative scenario.
    
    This test verifies that the DivideCalculator raises a ValueError when the divide method from Operations fails.
    """

    #Arrange
    a = 10.0
    b = 2.0
    mock_divide.side_effect = ValueError("Division error")
    calc = DivideCalculator(a, b)

    #Act & Assert
    with pytest.raises(ValueError) as e:
        calc.excute()
    
    assert str(e.value) == "Division error"

#========== Diviode by Zero Test Case ===========
@patch.object(Operations, 'divide', side_effect=ZeroDivisionError("Cannot divide by zero."))
def test_divide_calculation_zero_division(mock_divide):
    """
    Test the execute method of DivideCalculator for division by zero.
    
    This test verifies that the DivideCalculator raises a ZeroDivisionError when attempting to divide by zero.
    """

    #Arrange
    a = 10.0
    b = 0.0
    mock_divide.side_effect = ZeroDivisionError("Cannot divide by zero.")
    calc = DivideCalculator(a, b)

    #Act & Assert
    with pytest.raises(ZeroDivisionError) as e:
        calc.excute()
    
    assert str(e.value) == "Cannot divide by zero."
    



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


#========== Test __repr__ Method of Calculation Classes ===========


def test_calculation_repr_representation_add():
    """
    Test the __repr__ method of AddCalculator.
    
    This test checks if the __repr__ method of AddCalculator returns the expected string representation.
    """
    #Arrange
    a = 5.0
    b = 3.0
    calc = AddCalculator(a, b)

    #Act
    result_repr = repr(calc)

    #Assert
    assert result_repr == "AddCalculator(a = 5.0, b = 3.0)"

def test_calculation_repr_representation_subtract():
    """
    Test the __repr__ method of SubtractCalculator.
    
    This test checks if the __repr__ method of SubtractCalculator returns the expected string representation.
    """
    #Arrange
    a = 8.0
    b = 5.0
    calc = SubtractCalculator(a, b)

    #Act
    result_repr = repr(calc)

    #Assert
    assert result_repr == "SubtractCalculator(a = 8.0, b = 5.0)"


def test_calculation_repr_representation_multiply():
    """
    Test the __repr__ method of MultiplyCalculator.
    This test checks if the __repr__ method of MultiplyCalculator returns the expected string representation.
    """
    #Arrange
    a = 4.0
    b = 2.5
    calc = MultiplyCalculator(a, b)

    #Act
    result_repr = repr(calc)

    #Assert
    assert result_repr == "MultiplyCalculator(a = 4.0, b = 2.5)"

def test_calculation_repr_representation_divide():
    """
    Test the __repr__ method of DivideCalculator.
    
    This test checks if the __repr__ method of DivideCalculator returns the expected string representation.
    """
    #Arrange
    a = 10.0
    b = 2.0
    calc = DivideCalculator(a, b)

    #Act
    result_repr = repr(calc)

    #Assert
    assert result_repr == "DivideCalculator(a = 10.0, b = 2.0)"



#========== Parameterized Tests for excute method ===========

@pytest.mark.parametrize(
    "calculator_type, a, b, expected_result",
    [
        ("add", 5.0, 3.0, 8.0),
        ("subtract", 8.0, 5.0, 3.0),
        ("multiply", 4.0, 2.5, 10.0),
        ("divide", 10.0, 2.0, 5.0),
    ]
)

@patch.object(Operations, 'add')
@patch.object(Operations, 'subtract')
@patch.object(Operations, 'multiply')
@patch.object(Operations, 'divide')
def test_calculation_execute_parameterized(
    mock_divide, mock_multiply, mock_subtract, mock_add,
    calculator_type, a, b, expected_result
):
    """
    Parameterized test for the execute method of different calculation subclasses.
    
    This test checks if the execute method of each calculator type returns the expected result.
    """
    # Arrange
    if calculator_type == "add":
        mock_add.return_value = expected_result
    elif calculator_type == "subtract":
        mock_subtract.return_value = expected_result
    elif calculator_type == "multiply":
        mock_multiply.return_value = expected_result
    elif calculator_type == "divide":
        mock_divide.return_value = expected_result
    
    # Act
    calc = CalculatorFactory.create_calculator(calculator_type, a, b)
    result = calc.excute()

    # Assert
    if calculator_type == "add":
        mock_add.assert_called_once_with(a, b)

    elif calculator_type == "subtract":
        mock_subtract.assert_called_once_with(a, b)
    
    elif calculator_type == "multiply":
        mock_multiply.assert_called_once_with(a, b)

    elif calculator_type == "divide":
        mock_divide.assert_called_once_with(a, b)

    assert result == expected_result


#========== parameterized tests for string representation ===========

@pytest.mark.parametrize("calculator_type, a, b, expected_str", [
    ("add", 5.0, 3.0, "AddCalculator: 5.0 + 3.0 = 8.0"),
    ("subtract", 8.0, 5.0, "SubtractCalculator: 8.0 - 5.0 = 3.0"),
    ("multiply", 4.0, 2.5, "MultiplyCalculator: 4.0 * 2.5 = 10.0"),
    ("divide", 10.0, 2.0, "DivideCalculator: 10.0 / 2.0 = 5.0"),
])

@patch.object(Operations, 'add', return_value=8.0)
@patch.object(Operations, 'subtract', return_value=3.0)
@patch.object(Operations, 'multiply', return_value=10.0)
@patch.object(Operations, 'divide', return_value=5.0)

def test_calculation_str_parameterized(
    mock_divide, mock_multiply, mock_subtract, mock_add,
    calculator_type, a, b, expected_str
):
    """
    Parameterized test for the string representation of different calculation subclasses.
    
    This test checks if the string representation of each calculator type matches the expected format.
    """
    # Arrange
    calc = CalculatorFactory.create_calculator(calculator_type, a, b)

    # Act
    result_str = str(calc)

    # Assert
    assert result_str == expected_str

@pytest.mark.parametrize("calculator_type, a, b, expected_repr", [
    ("add", 5.0, 3.0, "AddCalculator(a = 5.0, b = 3.0)"),
    ("subtract", 8.0, 5.0, "SubtractCalculator(a = 8.0, b = 5.0)"),
    ("multiply", 4.0, 2.5, "MultiplyCalculator(a = 4.0, b = 2.5)"),
    ("divide", 10.0, 2.0, "DivideCalculator(a = 10.0, b = 2.0)"),
])
@patch.object(Operations, 'add', return_value=8.0)
@patch.object(Operations, 'subtract', return_value=3.0)
@patch.object(Operations, 'multiply', return_value=10.0)
@patch.object(Operations, 'divide', return_value=5.0)
def test_calculation_repr_parameterized(
    mock_divide, mock_multiply, mock_subtract, mock_add,
    calculator_type, a, b, expected_repr
):
    """
    Parameterized test for the __repr__ method of different calculation subclasses.
    
    This test checks if the __repr__ method of each calculator type returns the expected string representation.
    """
    # Arrange
    calc = CalculatorFactory.create_calculator(calculator_type, a, b)

    # Act
    result_repr = repr(calc)

    # Assert
    assert result_repr == expected_repr


#========== End of Test Cases for Calculation Module ===========

