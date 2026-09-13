# 01_variables_and_types.py
# Module 1: Basics & Syntax - Data Types and Dynamic Typing

# 1. Variables & Dynamic Typing (No data types needed like in C!)
name = "Alex"          # String (str)
age = 18               # Integer (int)
gpa = 8.5              # Floating point (float)
is_learning_python = True  # Boolean (bool)

# 2. Printing output using f-strings
print("--- User Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"Learning Python: {is_learning_python}")

# 3. Checking Data Types using type()
print("\n--- Data Types ---")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of gpa: {type(gpa)}")
print(f"Type of is_learning_python: {type(is_learning_python)}")

# 4. Basic Type Casting (Converting types)
str_age = str(age)     # Converts int -> string
int_gpa = int(gpa)     # Converts float -> int (truncates to 8)

print("\n--- Type Casting ---")
print(f"Age as string: '{str_age}' (Type: {type(str_age)})")
print(f"GPA as integer: {int_gpa} (Type: {type(int_gpa)})")