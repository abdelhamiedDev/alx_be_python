def safe_divide(numerator, denominator):
    try:
        # Convert to float
        num = float(numerator)
        denom = float(denominator)

        # Check division by zero
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        # Perform division
        result = num / denom
        return f"The result of the division is: {result}"

    except ValueError:
        # When conversion to float fails
        return "Error: Both inputs must be numbers."

    except ZeroDivisionError as e:
        # Catch manual raise or actual division by zero
        return f"Error: {e}"

    except Exception as e:
        # Catch anything unexpected
        return f"Unexpected error: {e}"
