
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_celsius():
    print("\nIs your temperature in fahrenheit or celsius?")
    print("F: Fahrenheit")
    print("C: Celsius")

    choice = input("Select F or C:")

    if choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} °F is equal to {celsius:.2f} °C")
    elif choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} °C is equal to {fahrenheit:.2f} °F")
    else:
        print("Invalid input, try again.")


if __name__ == "__main__":
    fahrenheit_celsius()

    
