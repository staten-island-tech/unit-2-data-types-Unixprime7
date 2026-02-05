number = input("State a number ")
number_value = int(number)
divisor = 1
factor = number_value / divisor
remainder = number_value % divisor

for i in range(number_value):
    i = divisor
    if remainder == 0:
        print(factor)
        divisor = divisor + 1
    else:
        divisor = divisor + 1
