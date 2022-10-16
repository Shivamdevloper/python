#Write a program to read your name, contact number, email, and
#birthdate and print those details on the screen.
import re
global IsValidForm
IsValidForm = True
name=input("Enter the name:")
print(name)

regex_name = re.compile(r'([a-z]+)( [a-z]+)*( [a-z]+)*$',
                        re.IGNORECASE)
res = regex_name.search(name)
if res: print("Valid")
else:
    print("Invalid")
    IsValidForm = False

contact=input("Enter the contact number:")
print(contact)

num= r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$'
#num = re.compile(r'([0-9]+)( [0-9]+)*( [0-9]+)*$')

if (re.fullmatch(num, contact)):
    print("valid")
else:
    print("Invalid")
    IsValidForm = False

birthdate=input("Enter the birthdate:")
print(birthdate)
#dd/MM/yyyy
birth=r'(?:0[1-9]|[12]\d|3[01])([\/.-])(?:0[1-9]|1[012])\1(?:19|20)\d\d$'
if (re.fullmatch(birth, birthdate)):
    print("valid")
else:
    print("Invalid")
    IsValidForm = False

email=input("Enter the email:")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

if (re.fullmatch(regex, email)):
    print("Valid Email")
else:
    print("Invalid Email")
    IsValidForm = False

print(email)

if (IsValidForm):
    print("Welcome User!")
else:
    print("Invalid Form Details, Please enter correct details.")
