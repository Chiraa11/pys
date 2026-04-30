import random
item = ["Rock", "Paper", "Scissor"]


while True:

 Uchoice = input("Enter your move = Rock, Paper , Scissor = ")
 Cchoice = random.choice(item)

 print(f"User Choice = {Uchoice}")
 print(f"Computer Choice = {Cchoice}")

 if Uchoice == Cchoice :
  print("Both chooses same = Match Tie.")

 if Uchoice == 'Rock' :
  if Cchoice == 'Paper' :
      print ("Paper covers Rock ,Computer won You lose !")
  else :
      print ("Rock smashes Scissor , Congrats You won Computer lose !")
 elif Uchoice == 'Paper' :
  if Cchoice == 'Rock' :
      print("Paper covers Rock , Congrats You won Computer lose !")
  else:
      print("Scissor cuts Paper , Computer won You lose ! ")

 elif Uchoice == 'Scissor' :
  if Cchoice == 'Rock' :
      print("Rock smashes scissor , Computer won You lose !")
  else:
      print("Scissor cuts paper, Congrats You won Computer lose !")

 else :
  print("You can Only choose between 'Rock', 'Paper', and 'Scissor'")