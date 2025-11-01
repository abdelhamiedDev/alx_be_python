def safe_divide(numerator, denominator):
    """Performs a division operation with error handling for division by zero.

    Args:
        numerator (float): The numerator of the division.
        denominator (float): The denominator of the division.
    Returns:
        float: The result of the division if successful.    
    Raises:
        ValueError: If the denominator is zero.
    """  
    
    
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
        return None
    except TypeError:
        raise TypeError("Error: Please enter numeric values only.")
        return None
    return result
    