integer_var = 10          
float_var = 3.5           
string_var = "Python"    
boolean_var = True        

print("Integer value:", integer_var, "Type:", type(integer_var))
print("Float value:", float_var, "Type:", type(float_var))
print("String value:", string_var, "Type:", type(string_var))
print("Boolean value:", boolean_var, "Type:", type(boolean_var))

print("\n--- Arithmetic Operations ---")

print("Addition:", integer_var + float_var)
print("Subtraction:", integer_var - float_var)
print("Multiplication:", integer_var * float_var)
print("Division:", integer_var / float_var)

print("\n--- Type Conversion with User Input ---")

try:
    num1 = input("Enter a number (integer): ")
    num2 = input("Enter another number (float): ")

    int_num = int(num1)
    float_num = float(num2)

    print("Converted Integer:", int_num, "Type:", type(int_num))
    print("Converted Float:", float_num, "Type:", type(float_num))

    print("Sum of numbers:", int_num + float_num)

except ValueError:
    print("Invalid input! Please enter numeric values only.")

print("\n--- Dynamic Typing Demonstration ---")

x = 10
print("x =", x, "Type:", type(x))

x = "Now I am a string"
print("x =", x, "Type:", type(x))

x = 5.5
print("x =", x, "Type:", type(x))
