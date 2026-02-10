number1 = input("State the first number: ")
number_value1 = int(number1)

number2 = input("State the second number: ")
number_value2 = int(number2)

def gcf(number_value1, number_value2):
    for i in range(number_value1):
        x = number_value1 - i
        if number_value1 % x == 0 and number_value2 % x == 0:
            y = int(x)
            print(y)
            return
gcf(number_value1, number_value2)