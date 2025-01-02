import random
import string
import time

print('********** PASSWORD GENERATOR **********')
password_count = int(input("How many password you want to generate? "))
length = int(input("How many characters do you want in your password? "))

#Setting length limit.
if length > 70:
    print("Warning: Maximum password length is 70.")
    time.sleep(1)
    print("STOPPING EXECUTION...")
    exit()

print("\n")
full_set = string.ascii_letters + string.digits + string.punctuation
print("Generating passwords...")
time.sleep(1)
for x in range(1, password_count + 1):
    print(f"Password {x}:")
    for y in range(length):
        choice = random.choice(full_set)
        print(choice, end='')

    print("\n")
    time.sleep(1)

print(f"Generated {password_count} passwords.")
strength = ""
if length <= 4:
    strength = "Weak"
elif length <= 8:
    strength = "Good"
elif length <= 11:
    strength = "Strong"
elif length <= 70:
    strength = "Very strong"
time.sleep(1)
print(f"Password Strength: {strength}")
