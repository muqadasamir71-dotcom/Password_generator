import random
import string

print("=" * 35)
print("     PASSWORD GENERATOR")
print("=" * 35)

length = int(input("Enter password length: "))

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nYour Secure Password:")
print(password)

print("=" * 35)
