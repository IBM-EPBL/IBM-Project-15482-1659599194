def add(numa, numb):
    return numa + numb
def subtract(numa, numb):
    return numa - numb
def multiply(numa, numb):
    return numa * numb
def divide(numa, numb):
    return numa / numb
print("please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")
select = int(input("select operations from 1, 2, 3, 4 :"))
number_a = int(input("Enter first number: "))
number_b = int(input("Enter second number: "))
if select == 1:
    print(number_a, "+", number_b, "=", add(number_a, number_b))
elif select == 2:
    print(number_a, "-", number_b, "=", subtract(number_a, number_b))
elif select == 3:
    print(number_a, "*", number_b, "=", multiply(number_a, number_b))
elif select == 4:
    print(number_a, "/", number_b, "=", divide(number_a, number_b))
else:
    print("Invalid input")
