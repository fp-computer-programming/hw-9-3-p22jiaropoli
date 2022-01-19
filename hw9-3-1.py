# Author JRI 1/17/22

while True:
    try: 
        temp1 = float(input("Enter the temperature "))
        scale = input("Do you want to cconvert to (f/C)? ")
        if scale.upper() == "C":
            result = (temp1 - 32) * 5 / 9
            print("{0} degrees farenheit is {1} degrees celcius.".format(temp1, result))
        elif scale.upper() == "F":
            result = temp1 / 5 * 9 + 32
            print("{0} degrees celcius is {1} degrees fahrenheit.".format(temp1, result))
        else:
            print("Invalid input, enter F for fahrenheit or C for celsius.")
    except ValueError:
        print("Invalid input, enter a numerical value for the temperature")