import random

snake = '''_______
---'   _|____)--
---'   (___)
      (_____)
      (_____)
      (____)
---.__(___)
'''

water = '''
    _______  ______      ____) ____
  ____)__________)    ______ 
          _______ _______) _______)
__________)  ______ _______) ____
'''

gun = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

a=[snake,gun,water]

user_choice=int(input("Enter your Choice"))
if user_choice<0 and user_choice>2:
    print("Invalid Input")
else:
    print("user Choice")
    print(a[user_choice])

comp_choice=random.randint(0,2)
print("Computer Choice")
print(a[comp_choice])

if user_choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and user_choice == 2:
    print("You lose")
elif comp_choice > user_choice:
    print("You lose")
elif user_choice > comp_choice:
    print("You win!")
elif comp_choice == user_choice:
    print("It's a draw")
