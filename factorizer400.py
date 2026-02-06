number = input("State a number ")
number_value = int(number)


for i in range(number_value):
    x = i + 1
    factor = number_value / x
    remainder = number_value % x
    
    if remainder == 0:
        print(int(factor))
        x = x + 1
    else:
        x = x + 1
