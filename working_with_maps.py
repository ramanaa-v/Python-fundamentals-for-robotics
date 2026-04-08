def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

temperatures_celsius = [0, 20, 30, 40]

temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))

print(temperatures_fahrenheit)