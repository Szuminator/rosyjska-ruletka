import random

print("ROSYJSKA RULETKA v2.0")
print("Dodaj graczy, gdy juz dodasz tyle ile chcesz napisz ok i wcisnij enter")

listOfPlayers = []
x = input()
listOfPlayers.append(x)

while x != "ok":
    x = input()
    listOfPlayers.append(x)

del listOfPlayers[-1]

print("LISTA GRACZY:")
for i in listOfPlayers:
    print(i)
helper = 0
remover = 1000000
shot = 0
while len(listOfPlayers) > 1:
    print("\nAKTUALNA LISTA ŻYWYCH GRACZY: ")
    for i in listOfPlayers:
        zeroOrOther = random.randrange(0, 8)
        if (zeroOrOther == 0):
            if(shot > 0):
                continue
            else:
                print(i, " :BOOM!!!")
                remover = helper
                shot = 2
        else:
            print(i, " :Uff.. uszlo na sucho")
        helper = helper + 1
    if(remover < 1000000):
        del listOfPlayers[remover]
    helper = 0
    remover = 1000000
    shot = 0
    wait = input("Nacisnij enter by kontynuowac")
print("Wygral/a: ", listOfPlayers[0])
w = input()
