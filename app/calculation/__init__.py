"""
This module provides a factory for creating calculator instances based on the operation type.
"""

from abc import ABC, abstractmethod
from app.operations import Operations

class Calculation(ABC):
    """
    Abstract base class for all calculations.
    This class defines the basic structure for calculations, including the operands and the method to execute the calculation.
    It also provides a string representation of the calculation.

    Attributes:
        a (float): The first operand.
        b (float): The second operand.
        operator_symbol (str): The symbol representing the operation (e.g., "+", "-", "*", "/").

    Methods:
        excute() -> float: Execute the calculation and return the result.
        __str__() -> str: Return a string representation of the calculation.
        __repr__() -> str: Return a string representation of the calculation for debugging.
    """

    # __init__ method initializes the operands a and b.
    def __init__(self, a:float, b:float) -> None:
        """
        Initialize the Calculation with two operands.
        The initialization method takes two float numbers as input and assigns them to the instance variables a and b.
        a: float - The first operand.
        b: float - The second operand.

        Why have an __init__ method?
        -The __init__ method is used to initialize the instance variables of the class when an object is created.
        -This promotes encapsulation by allowing each Calculation object to maintain its own state (the values of a and b).
        -It also allows for easy extension of the class in the future if additional attributes or methods are needed.
        """
        self.a: float = a
        self.b: float = b
    
        
    # Excute method is an abstract method that must be implemented by subclasses.
    @abstractmethod
    def excute(self) -> float:
        """
        Abstract method to execute the calculation.
        This method must be implemented by subclasses to perform the specific calculation.
        
        Why use an abstract method?
        -An abstract method defines a contract for subclasses to implement specific behavior.
        -It allows for polymorphism, where different subclasses can provide their own implementations of the calculation.
        """
        pass

    # __str__ method provides a string representation of the calculation.
    def __str__(self) -> str:
        """
        __str_ method returns a string representation of the calculation.
        This is used to display the calculation in a human-readable format.
        It includes the class name, operands, operator symbol, and the result of the calculation.

        Why have a __str__ method?
        -The __str__ method provides a clear and concise way to represent the calculation as a string.
        -It is useful for logging, debugging, and displaying results to the user.
        """
        result = self.excute()
        #returns a string that includes the class name, operands, operator symbol, and result.
        return f"{self.__class__.__name__}: {self.a} {self.operator_symbol} {self.b} = {result}"
    

    # __repr__ method provides a string representation of the calculation for debugging.
    def __repr__(self) -> str:
        """
        __repr_ method returns a string representation of the calculation for debugging purposes.
        It is similar to the __str__ method but is intented to be used for debugging and development.
        """

        #returns a string that includes the class name and the operands.
        return f"{self.__class__.__name__}(a = {self.a}, b = {self.b})"
    

# Factory class to create calculator instances based on the operation type.
class CalculatorFactory:
    """
    This is the factory class for creating calculator instances based on the operation type.
    It uses a class method to register calculator classes and create instances based on the operation type.

    Attributes:
        _calculation (dict): A dictionary that maps operation types to their corresponding calculator classes.

    Methods:
        register_calculator(calculation_type: str) -> None: Decorator to register a calculator class.
        create_calculator(operation: str, a: float, b: float) -> Calculation: Create a calculator instance based on the operation type.

    Why use a factory class?
    -The factory class only deals with object creation, which promotes the Single Responsibility Principle (SRP).
    -It allows for easy extension of the calculator functionality by adding new calculator classes without modifying existing code.
    """
    
    # Class variable to hold the mapping of operation types to calculator classes.
    _calculation = {}

    # Class method to register a calculator class.
    @classmethod
    def register_calculator(cls, calculation_type: str) -> None:
        """
        Decorator to register a calculator class for a specific calculation type.
        calculation_type is a string that represents the type of calculation (ex: "add", "subtract", "multiply", "divide").
        
        The method first checks if the calculation_type is already registered.
        If it is, it raises a ValueError. If not, it registers the subclass in the _calculation dictionary.
        This allows for easy extension of the calculator functionality by adding new calculator classes without modifying existing code.
        """
        
        
        def decorator(subclass):
            """Decorator to register a calculator class."""
            # Check if the calculation_type is already registered.
            if calculation_type in cls._calculation:
                # If it is, raise a ValueError to prevent overwriting.
                raise ValueError(f"Calculation type '{calculation_type}' already registered.")
            # Register the subclass in the _calculation dictionary.
            cls._calculation[calculation_type] = subclass
            return subclass #return the subclass for further use.
        return decorator #return the decorator
    
    # Class method to create a calculator instance based on the operation type.
    @classmethod
    def create_calculator(cls, operation: str, a: float, b: float) -> Calculation:
        """
        This method creates a calculator instance based on the operation type.
        
        Parameters:
            operation (str): The type of operation to perform (e.g., "add", "subtract", "multiply", "divide").
            a (float): The first operand.
            b (float): The second operand.
        Returns:
            Calculation: An instance of the appropriate subclass of Calculation based on the operation type.
        """

        # Check if the operation is registered in the _calculation dictionary.
        if operation not in cls._calculation:
            # If not, raise a ValueError to indicate that the operation is not supported.
            raise ValueError(f"Operation '{operation}' is not supported.") 
        #create and return an instance of the appropriate subclass of Calculation.
        return cls._calculation[operation](a, b)
    

"""
Create seperate calculator classes for each operation.
These classes inherit from the Calculation abstract base class and implement the excute method for each specific operation.

Why create separate classes for each operation?
- This promotes Polymorphism, allowing each operation to have its own implementation of the excute method.
- Modularity: Each operation is encapsulated in its own class, making the code more 
maintainable and easier to understand.
"""
@CalculatorFactory.register_calculator("add" )
class AddCalculator(Calculation):
    """
    Create seperate calculator classes for each operation.
    These classes inherit from the Calculation abstract base class and implement the excute method for each specific operation.

    Why create separate classes for each operation?
    - This promotes Polymorphism, allowing each operation to have its own implementation of the excute method.
    - Modularity: Each operation is encapsulated in its own class, making the code more 
    maintainable and easier to understand.
    """


    """
    Calculator for addition.
    it inherits from the Calculation abstract base class and implements the excute method for addition.
    It specifically handles the addtion operation, keeping the implementation sperate from other operations.
    """

    # operator_symbol is a class variable that represents the symbol for the addition operation.
    operator_symbol = "+"
    def excute(self) -> float: 
        return Operations.add(self.a, self.b) #uses the Operations class to perform the addition operation.



@CalculatorFactory.register_calculator("subtract")
class SubtractCalculator(Calculation):
    """
    Calculator for subtraction.
    It inherits from the Calculation abstract base class and implements the excute method for subtraction.
    It specifically handles the subtraction operation, keeping the implementation separate from other operations."""
    
    operator_symbol = "-" # "-" is the operator symbol for subtraction.
    def excute(self) -> float:
        return Operations.subtract(self.a, self.b) #uses the Operations class to perform the subtraction operation.



@CalculatorFactory.register_calculator("multiply" )
class MultiplyCalculator(Calculation):
    """
    Calculator for multiplication.
    It inherits from the Calculation abstract base class and implements the excute method for multiplication.
    It specifically handles the multiplication operation, keeping the implementation separate from other operations.
    """
    operator_symbol = "*" # "*" is the operator symbol for multiplication.
    def excute(self) -> float:
        
        return Operations.multiply(self.a, self.b) #uses the Operations class to perform the multiplication operation.
    

@CalculatorFactory.register_calculator("divide" )
class DivideCalculator(Calculation):
    """
    Calculator for division.
    It inherits from the Calculation abstract base class and implements the excute method for division.
    It specifically handles the division operation, keeping the implementation separate from other operations.
    """

    operator_symbol = "/" # "/" is the operator symbol for division.
    def excute(self) -> float:
        # Check if b is zero.
        if self.b == 0:
            #raise a ValueError if b is zero.
            raise ValueError("Cannot divide by zero.") 
        # If b is not zero, use the Operations class to perform the division operation.
        return Operations.divide(self.a, self.b)




# @CalculatorFactory.register_calculator("power" )
# class PowerCalculator(Calculation):
#     """Calculator for exponentiation."""
#     operator_symbol = "^"
#     def excute(self) -> float:
#         return Operations.power(self.a, self.b)
    

