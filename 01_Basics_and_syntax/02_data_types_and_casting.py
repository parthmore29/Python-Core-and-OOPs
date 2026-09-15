# 02_data_types_and_casting.py
# Core Concepts: Fundamental Types, Dynamic Typing, and Type Conversion

# 1. Fundamental Primitive Data Types
age = 21                  # int
gpa = 8.5                 # float
is_enrolled = True        # bool
course_name = "Python"    # str

print("--- Fundamental Types ---")
print(f"age: {age} | Type: {type(age)}")
print(f"gpa: {gpa} | Type: {type(gpa)}")
print(f"is_enrolled: {is_enrolled} | Type: {type(is_enrolled)}")
print(f"course_name: '{course_name}' | Type: {type(course_name)}")


# 2. Dynamic Typing (Python variables can change types dynamically)
data = 100
print(f"\n--- Dynamic Typing ---\nInitial data: {data} ({type(data)})")

data = "Now I am a string"
print(f"Reassigned data: '{data}' ({type(data)})")


# 3. Explicit Type Casting (Conversion)
str_num = "42"
converted_num = int(str_num)  # String to Int
float_val = float(age)        # Int to Float
str_gpa = str(gpa)            # Float to String

print("\n--- Type Casting ---")
print(f"Converted String '42' -> Int: {converted_num} ({type(converted_num)})")
print(f"Converted Int {age} -> Float: {float_val} ({type(float_val)})")
print(f"Converted Float {gpa} -> String: '{str_gpa}' ({type(str_gpa)})")


# 4. Truthy and Falsy Values
# In Python, empty structures, 0, None, and False evaluate to False.
print("\n--- Boolean Evaluation (Truthy/Falsy) ---")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('Hello'): {bool('Hello')}")