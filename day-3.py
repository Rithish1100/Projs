import random
c=int(input ("what do u choose? type 0 for rock ,type 1 for paper,type 2 for scissors.\n"))
a=random.randint(0,2)
if a==0:
    print("rock")
elif a==1:
    print("paper")
elif a==2:
    print("scissors")
if c==0 and a==1:
    print("paper wins,pc wins")
elif c==1 and a==2:
    print("scissors wins,pc wins ")
elif c==2 and a==0:
    print("rock wins,pc wins")
elif c==0 and a==0:
    print("no one wins,tie")
elif c==1 and a==1:
     print("no one wins,tie")
elif c==2 and a==2:
     print("no one wins,tie")
else:
    print("user wins")