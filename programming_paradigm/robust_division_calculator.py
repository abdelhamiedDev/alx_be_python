def safe_divide(numerator, denominator):
    """Performs a division operation with error handling for division by zero.

    Args:
        numerator (float): The numerator of the division.
        denominator (float): The denominator of the division.
    Returns:
        float: The result of the division if successful.

    Raises:
        TypeError: If inputs are not numeric.
        ZeroDivisionError: If denominator is zero.
    """  
    # Convert inputs to float and validate
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except (ValueError, TypeError) as e:
        # Use a consistent exception for non-numeric inputs
        raise TypeError("Error: Please enter numeric values only.") from e

    # Check for division by zero explicitly
    if denominator == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")

    # Successful division: return the formatted string requested by the user
    result = numerator / denominator
    return f"The result of the division is {result}"