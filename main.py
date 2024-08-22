import random
m="Welcome to the rock paper scissor game"
def dec():
  
  print(m.center(50))

def print_welcome_box():
  
  border = "*" * (len(m) + 4)
  print(border.center(50))


print_welcome_box()
dec() 
print_welcome_box()

running=True
while(running):
  options=("rock","paper","scissor")

  player=None
  computer=random.choice(options)

  while player not in options:
    player=input("Enter your choice(rock,paper,scissor)")

  print(f"Player: {player}")
  print(f"Computer: {computer}")
  if player==computer:
    print("Tie")

  elif player=="rock" and computer=="scissor":
    print("You win")

  elif player=="paper" and computer=="rock":
    print("You win")

  elif player=="scissor" and computer=="paper":
    print("You win")

  else:
    print("You Lose")


  playagain=input("Play again?(y/n)").lower()
  if playagain!="y":
    running=False

print("Thanks for playing")

  
  