def safe_divide(numerator, denominator):
    try:
        # Convert to float
        num = float(numerator)
        denom = float(denominator)

        # Check division by zero
        if denom == 0:
            raise ZeroDivisionError

        # Perform division
        result = num / denom
        return f"The result of the division is: {result}"

    except ValueError:
        # When conversion to float fails
        return "Error: Both inputs must be numbers."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except Exception as e:
        # Catch anything unexpected
        return "Unexpected error occurred."
