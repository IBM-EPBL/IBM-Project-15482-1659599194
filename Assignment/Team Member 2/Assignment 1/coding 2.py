def add(numx, numy):
    return numx + numy
def subtract(numx, numy):
    return numx- numy
def multiply(numx, numy):
    return numx * numy
def divide(numx, numy):
    return numx / numy
print("please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")
select = int(input("select operations from 1, 2, 3, 4 :"))
number_x = int(input("Enter first number: "))
number_y = int(input("Enter second number: "))
if select == 1:
    print(number_x, "+", number_y, "=", add(number_x, number_y))
elif select == 2:
    print(number_x, "-", number_y, "=", subtract(number_x, number_y))
elif select == 3:
    print(number_x, "*", number_y, "=", multiply(number_x, number_y))
elif select == 4:
    print(number_x, "/", number_y, "=", divide(number_x, number_y))
else:
    print("Invalid input")
