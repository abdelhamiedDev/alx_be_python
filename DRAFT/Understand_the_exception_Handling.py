try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
    # This code attempts to divide 10 by 0, which raises a ZeroDivisionError.