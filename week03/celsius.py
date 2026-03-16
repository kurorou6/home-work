def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print("Temperature in Fahrenheit:", fahrenheit)
    if fahrenheit > 90:
        print("It is really hot! Be careful 🔥")
    if fahrenheit < 30:
        print("It is very cold! Dress warmly ❄️")
main()