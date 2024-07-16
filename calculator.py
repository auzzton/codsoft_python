a = int(input("Enter the first number "))
b= int(input("Enter the second number "))
operator=input("Enter your desired operator (+,-,*,/)")
if(operator  == '+'):
    op = a + b
if(operator  == '-'):
    op = a - b
if(operator  == '*'):
    op = a * b
if(operator  == '/'):
    op = a / b
print(f"Result = {op}")