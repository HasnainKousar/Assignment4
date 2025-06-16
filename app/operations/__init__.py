"""
For this module, we will use Object-Oriented Programming (OOP) principles to create a class called Operation.
This class will contain methods for basic arithmetic operations: addition, subtraction, multiplication, and division.

Instead of creating a separate function for each operation, we will define static methods within the Operation class.
Static methods allow us to call these methods without needing to create an instance of the class.
This allows us to group related operations together and makes the code more organized and reusable.

"""


class Operations:

    @staticmethod
    def add(a: float, b:float) -> float:
        """
        Returns the sum of a and b.
        a:float - a supposed to be a number with type float(decimal point number)
        b:float - b supposed to be a number with type float(decimal point number)
        The sum will be returned as a float(decimal point number)
        
        """

        return a + b #math part where it will add the two numbers together and return the sum as a float(decimal point number).


    @staticmethod
    def subtract(a:float, b:float) -> float:
        """
        Returns the difference of a and b.
        a:float - a supposed to be a number with type float(decimal point number)
        b:float - b supposed to be a number with type float(decimal point number)
        The difference will be returned as a float(decimal point number)

        """
        return a - b #math part where it will subtract the two numbers and return the difference as a float(decimal point number).
    

    @staticmethod
    def multiply(a:float, b:float) -> float:
        """
        Returns the product of a and b.
        a:float - a supposed to be a number with type float(decimal point number)
        b:float - b supposed to be a number with type float(decimal point number)
        The product will be returned as a float(decimal point number)

        """
        return a * b #math part where it will multiply the two numbers and return the product as a float(decimal point number).
    

    @staticmethod
    def divide(a:float, b:float) -> float:
        """
        Returns the quotient of a and b. 
        a:float - a supposed to be a number with type float(decimal point number)
        b:float - b supposed to be a number with type float(decimal point number)
        The quotient will be returned as a float(decimal point number).

        In the case of division, the denominator cannot be zero so the function first checks if b == 0.
        If b is zero, it raises a ValueError with the message "Cannot divide by zero."
        If b is not zero, it will return the quotient (a / b). 
       
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b #math part where it will divide the two numbers and return the quotient as a float(decimal point number).
    
    @staticmethod
    def power(a: float, b: float) -> float:
        """
        Returns a raised to the power of b.
        a:float - a supposed to be a number with type float(decimal point number)
        b:float - b supposed to be a number with type float(decimal point number)
        The result will be returned as a float(decimal point number)

        """
        return a ** b #math part where it will raise the first number to the power of the second and return the result as a float(decimal point number).
    
    
    

