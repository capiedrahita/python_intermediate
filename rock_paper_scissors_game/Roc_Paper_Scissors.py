#Rock Paper Scissors Game
import random
print("Welcome to Rock-Paper-Scissors Game\n")

play = int(input("Please choose Rock(1) - Paper(2) or Scissors(3): \n"))
comp_play = random.randint(1,3)
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

if play == 1:
    print("You Choose Rock:")
    print(rock)
elif play == 2:
    print("You Choose Paper:")
    print(paper)
else:
    print("You Choose Scissors:")
    print(scissors)

if comp_play == 1:
    print("PC Choose Rock:")
    print(rock)
elif comp_play == 2:
    print("PC Choose Paper:")
    print(paper)
else:
    print("PC Choose Scissors:")
    print(scissors)

if (play==1 and comp_play==1) or (play==2 and comp_play==2) or (play==3 and comp_play==3):
    print("Deuce")
elif (play==1 and comp_play==2) or (play==2 and comp_play==3) or (play==3 and comp_play==1):
    print("You Loose")
else:
    print("You Win")