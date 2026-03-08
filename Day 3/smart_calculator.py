def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

print("""
      1.Add
      2.Subtract
      3.Multiply
      4.Divide
""")

a= float(input("Enter first number: "))
operation = int(input("Choose operation: "))
b = float(input("Enter second number: "))

if(operation == 1):
    print("Result", add(a,b))
elif(operation == 2):
    print("Result", subtract(a,b))  
elif(operation == 3):
    print("Result", multiply(a,b))
elif(operation == 4):
    print("Result", divide(a,b))
else:
    print("Invalid operation")