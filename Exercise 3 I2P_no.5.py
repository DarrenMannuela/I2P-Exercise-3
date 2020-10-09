celsius = 0
kelvin = 0
fahrenheit = 0


def convert_to_celsius():
    global celsius, kelvin, fahrenheit
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_kelvin():
    global celsius, kelvin, fahrenheit
    kelvin = celsius + 273.13
    return kelvin


def convert_temp():
    global celsius, kelvin, fahrenheit
    fahrenheit = int(input("Enter a temperature in Fahrenheit :"))
    print("\nThe temperature in Fahrenheit is :", fahrenheit)
    convert_to_kelvin()
    convert_to_celsius()
    print("The temperature in Celsius is:", celsius)
    print("The temperature in Kelvin is:", kelvin)
    


convert_temp()
