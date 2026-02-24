import random
import gamedata as g
import art1 as art
cans=0
score=0
a=0
while(cans>=0):

    print(art.a[0])
    if(a==0):
        a=random.randint(0,10)
    b=random.randint(0,10)

    if(cans>=0):
        print("Thats correct ,Current score:",score)

    if(a!=b):
        print("compare A:",g.data[a]['name'],g.data[a]['description'],g.data[a]['country'])
        print(art.b)
        print("compare B:",g.data[b]['name'],g.data[b]['description'],g.data[b]['country'])
        choice=input("how has more followers Type 'A' or 'B':")
        afol=(g.data[a]['follower_count'])
        bfol=(g.data[b]['follower_count'])
        if(choice=='A'):
            if(afol>bfol):
                print("correct answer")
                a=b
                score+=1
            else:
                cans=-1
                print(art.a)
                print("better luck next time,Your score",score)
           
        elif(choice=='B'):
            if(bfol>afol):
                print("correct answer")
                a=b
                score+=1
            else:
                cans=-1
                print(art.a)
                print("Better luck next time",score)
           
    
