score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}") 

age = 20
has_id = True
is_vip = False

if age >= 18 and has_id:
    print("Access granted: Standard Entry.")

if is_vip or (age >= 21 and has_id):
    print("Access granted: VIP lounge.")
else:
    print("VIP lounge access denied.")

is_banned = False
if not is_banned:
    print("Account status: Active.")

    status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} evaluated as: {status}")