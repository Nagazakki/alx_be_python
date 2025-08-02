FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")
    
    try:
        temp_input = input("Enter temperature (e.g., 100F or 37C): ")
        try:
            temperature = float(temp_input)
        except ValueError:
            raise("Invalid input. Please enter a valid numerical value.")

        unit = input("Is this in Fahrenheit (F) or Celsius (C)? ").strip().upper()

        if unit not in ['C', 'F']:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            return
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
        else:
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
