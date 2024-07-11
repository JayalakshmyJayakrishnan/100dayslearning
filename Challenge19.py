def add(a,b):
  return a + b
  
def subtract(a,b):
  return a - b
  
def multiply(a,b):
  return a*b
  
def divide(a,b):
  if b!= 0:
    return a/b
  else:
      print("Invalid!")

def modulus(a,b):
  if b==0:
    print("Invalid!")
  else:
    return a % b

def power(a,b):
  return a ** b


print("Select operation:")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. MODULUS")
print("6. POWER")


selection = input("Enter selection (1/2/3/4/5/6): ")


n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))


if selection == '1':
    print(n1, "+", n2, "=", add(n1, n2))
elif selection == '2':
    print(n1, "-", n2, "=", subtract(n1, n2))
elif selection == '3':
    print(n1, "*", n2, "=", multiply(n1, n2))
elif selection == '4':
    print(n1, "/", n2, "=", divide(n1, n2))
elif selection == '5':
    print(n1, "%", n2, "=", modulus(n1, n2))
elif selection == '6':
    print(n1, "**", n2, "=", power(n1, n2))
else:
    print("Invalid input!"
