from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rockpapersciss= input("0 for rock 1 for paper 2 for scissors")

if rockpapersciss == 0:
    print (rock)

elif rockpapersciss == 1:
        print (paper)
else:
    print (scissors)

computer_choice = randint (0 , 2)
print("computer chose:")
print([computer_choice])

if computer_choice == 0:
    print (rock)

elif computer_choice == 1:
        print (paper)
else:
    print (scissors)