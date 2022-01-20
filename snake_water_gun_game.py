import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "g": #s for snake and g for gun so by gun we kill snake so here i win
            return True
        elif you == "w": #s for snake and w for water so snake drinks water so here i lose
            return False
    elif comp == "g":
        if you == "w":
            return True #w for Water and g for gun so  gun falls in water so here i win
        elif you == "s":
            return False#s for snake and g for gun so by gun we kill snake so here i win
    elif comp == "w":
        if you == "s":#s for snake and w for water so snake drinks water so here i lose
            return True
        elif you =="g": #s for snake and w for water so snake drinks water so here i lose
            return False




comp=print("comp turn: snake(s),water(w),gun(g)")
r=random.randint(1, 3)
if r == 1:
    comp = "s"
elif r == 2:
    comp = "w"
elif r == 3:
    comp == "g"

you = input("your turn: snake(s),water(w),gun(g)")


print(F"comp takes {comp}")
print(F"you takes {you}")


a=game(comp,you)
if a == None:
    print("the game is tie")
elif a == True:
    print("you win!")
elif a==False:
    print("you loose!")
