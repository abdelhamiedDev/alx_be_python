FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
   # Convert Fahrenheit to Celsius.
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit.
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():

    inserted_temperature = int(input("Enter the temperature to convert: "))
    type_of_conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

    if type_of_conversion == 'C':
        converted_temp = convert_to_fahrenheit(inserted_temperature)
        print(f"{inserted_temperature}°C is {converted_temp:.1f}°F")
    elif type_of_conversion == 'F':
        converted_temp = convert_to_celsius(inserted_temperature)
        print(f"{inserted_temperature}°F is {converted_temp:.1f}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
if __name__ == "__main__":
    main()