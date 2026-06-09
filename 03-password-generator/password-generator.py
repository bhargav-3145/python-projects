import random
char = []
for i in range(65, 91):
    char.append(chr(i))
for i in range(97, 123):
    char.append(chr(i))
for i in range(10):
    char.append(str(i))
special = '!@#$%^&*()[]{}-_+=:;,.<>?/|'
for ch in special:
    char.append(ch)
password = ""
length = int(input("Enter password length : "))
for i in range(length):
    password += random.choice(char)
print(password)