import random
print("Rock(R) Paper(P) Scissor(S)")
user=int(input("Enter  0 or 1 or 2:"))
computer=random.randint(0,2)
print("Computer chooses:",computer)

if user>2:
    print("Invalid")
else:
    if user==computer:
        print("Draw match")
    elif user>computer:
        print("You win")
    elif computer>user:
        print("You Loose")
    elif user==0 and computer==2:
        print("You win")
    elif user==2 and computer==0:
        print("You Loose")

