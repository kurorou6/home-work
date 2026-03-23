temperature = (float(input("Enter temperature: ")))
fahrenheit = 1.8 * temperature +32
if fahrenheit > 90:
    print("Heat warning!")
elif fahrenheit < 30:
    print("Cold warning!")
else:
    print("Normal weather.")