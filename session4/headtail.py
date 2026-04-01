import random

player = 0
computer = 0
i = ""

while i != "x":
    print("\n--- Your:", player, "| CPU:", computer, "---")

    i = input("(O_O)=0  2$=1  exit=x : ")

    if i in ("0", "1"):
        coin = random.randint(0, 1)

        if coin == 0:
            print("Coin is: (O_O)")
        else:
            print("Coin is: 2$")

        if int(i) == coin:
            print("You won!")
            player += 1
        else:
            print("You lost!")
            computer += 1
    elif i != "x":
        print("Enter 0, 1 or x only!")

print("Player:", player)
print("Computer:", computer)
if player > computer:
    print("You have won more than the computer!")
elif player < computer:
    print("The Computer have won more than you.")
else:
    print("It is a Tie!!!!")        
print("Goodbyeeeee !!!!")