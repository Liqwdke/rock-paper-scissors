from random import randint


t = ["Rock", "Paper", "Scissors"]


computer = t[randint(0,2)]


player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("döntetlen!")
    elif player == "Rock":
        if computer == "Paper":
            print("vesztettél", computer, "Üti", player)
        else:
            print("Nyertél!", player, "Üti", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("vesztettél", computer, "vágja", player)
        else:
            print("Nyertél!", player, "Üti", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("vesztettél", computer, "Üti", player)
        else:
            print("Nyertél!", player, "vágja", computer)
    else:
        print("Valamit elgépeltél probáld meg ujra!")
   
    player = False
    computer = t[randint(0,2)]