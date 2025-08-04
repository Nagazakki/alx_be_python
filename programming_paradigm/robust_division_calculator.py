def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling exceptions for invalid inputs.
    
    Args:
        numerator (str): The numerator as a string.
        denominator (str): The denominator as a string.
    
    Returns:
        str: The result of the division or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Division by zero is not allowed."
        return str(num / denom)
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
