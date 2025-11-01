import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    try:
        # Convert string arguments to float
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Call safe_divide with numeric values
        result = safe_divide(numerator, denominator)
        print(f"The result of the division is: {result}")
        
    except ValueError:
        print("Error: Please enter valid numeric values.")
        sys.exit(1)
    except ZeroDivisionError as e:
        print(str(e))
        sys.exit(1)
    except TypeError as e:
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()