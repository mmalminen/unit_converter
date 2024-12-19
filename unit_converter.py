from typing import Callable, Tuple

# conversion factors
c_to_f_factor = 9/5
f_to_c_factor = 5/9
g_to_oz_factor = 0.03527396
m_to_f_factor = 3.28084

# temperature conversion functions
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * c_to_f_factor) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * f_to_c_factor

# weight conversion functions
def gram_to_ounce(gram: float) -> float:
    return gram * g_to_oz_factor

def ounce_to_gram(ounce: float) -> float:
    return ounce / g_to_oz_factor

# distance conversion functions
def meter_to_feet(meter: float) -> float:
    return meter * m_to_f_factor

def feet_to_meter(feet: float) -> float:
    return feet / m_to_f_factor

# keeps prompting until valid float is entered
def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nInvalid input.\nPlease enter a number.\nUse dot(.) as separator\n")

# structure for conversion menu
def conversion_menu(title: str, options: list[Tuple[str, Callable[[float], float], str, str]]) -> None:
    while True:
        print(f"\n{title}:")
        for i, (option, _, _, _) in enumerate(options, 1):
            print(f"{i}. {option}")
        print(f"{len(options) + 1}. Return to Main Menu")
        
        choice = input(f"Enter your choice (1-{len(options) + 1}): ")
        
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            option, conversion_func, from_unit, to_unit = options[int(choice) - 1]
            value = get_float_input(f"Enter value in {from_unit}: ")
            result = conversion_func(value)
            print(f"\n{value} {from_unit} is {result:.2f} {to_unit}.")
        elif choice == str(len(options) + 1):
            return
        else:
            print("Invalid selection, please try again.")

# options for conversion menu
def main() -> None:
    temperature_options = [
        ("Convert Celsius to Fahrenheit", celsius_to_fahrenheit, "Celsius", "Fahrenheit"),
        ("Convert Fahrenheit to Celsius", fahrenheit_to_celsius, "Fahrenheit", "Celsius")
    ]
    
    weight_options = [
        ("Convert Grams to Ounces", gram_to_ounce, "grams", "ounces"),
        ("Convert Ounces to Grams", ounce_to_gram, "ounces", "grams")
    ]
    
    distance_options = [
        ("Convert Meters to Feet", meter_to_feet, "meters", "feet"),
        ("Convert Feet to Meters", feet_to_meter, "feet", "meters")
    ]

# main menu
    while True:
        print("\nMain Menu:")
        print("1. Temperature")
        print("2. Weight")
        print("3. Distance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            conversion_menu("Temperature Conversion", temperature_options)
        elif choice == '2':
            conversion_menu("Weight Conversion", weight_options)
        elif choice == '3':
            conversion_menu("Distance Conversion", distance_options)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == '__main__':
    main()
