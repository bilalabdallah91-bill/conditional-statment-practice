#message welcome
print(f"\n {'='*10}WELCOME TO THE CONDITINAL STATMENT PROJECTS{'='*10}\n\n")

#1/first project
#password
correct_password="bill***mbk"
#Input your name.
user_name=input("Please enter your name:\n")
#input password
password=input("Please enter your password:\n").lower()
#chek user password
if correct_password==password:
    print(f"Welcome {user_name} to te app😊")
else:
    print(f"Sorry {user_name} you can't use the app,try again")
print('='*53)

#2/Second project
#type a Word
typed=input(f"Please {user_name} type:(yes) or (maybe) or (can)\n") 
#check guess
if typed == "yes":
    print(f"You typed {typed}")
elif typed == "maybe":
    print(f"You typed {typed}")
elif typed == "can":
    print(f"You typed {typed}")
else:
    print(f"You typed {typed}, which is not an option\nplease stick to the options")
print('='*53)

#3/Third project
#check number
correct_number=91

#Input number
guessed=int(input(f"Please {user_name} guessr a number:\n"))

#check number
if guessed==correct_number:
    print(f"Good guess😊.")
else:
    print(f"Your guess is {guessed} but the correctwis {correct_number},try again")
print('='*53)
