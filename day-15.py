MENU={
    "espresso":{
        "ingridents":{
        "water":50,
        "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
    "ingridents":{
        "water":200,
        "milk":150,
        "coffee":24,
        },
        "cost":2.5,
    },
    "capachino":{
        "ingridents":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    },
}

resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0,
}
a=0
user_inputs= ""
cost=0
s=0
coins=0
while (a==0):
        user_inputs = input("what would you like to order(espresso,latte,capachino):")
        if (user_inputs=="off"): 
            a=1
        elif(user_inputs=="report"):
            print(resources)
            a=1
        else:
           quater=input("Enter the number of quaters:")
           dimes=input("Enter the number of dimes:")
           nickel=input("Enter the number of nickels:")
           pennis=input("Enter the number of pennis:")
           s=0
           coins=(int(quater)+(float(dimes)*0.10)+(float(nickel)*0.05)+(float(pennis)*0.01))
           while(s==0):
            if(user_inputs=="espresso" and float(coins)>=1.5):
                s=3
                consume=50
                consume1=18
                if(resources["water"]<50):
                 print("Insufficient water")
                 s=1
                elif(resources["coffee"]<18):
                 print("Insufficent coffee")
                 s=1
                if(resources["water"]>0):
                 resources["water"]=resources.get("water",0)-consume
                if(resources["coffee"]>0):
                 resources["coffee"]=resources.get("coffee",2)-consume1
                 cost+=MENU["espresso"]["cost"]
            elif(float(coins)<1.5 and user_inputs=="espresso"):
               print("sorry that is not enough money,money refunded")
            if(s==3):
               coins-=1.5
               resources["money"]+=1.5
               print("Enjoy your espresso")
               s=1
            if(user_inputs=="latte" and float(coins)>=2.5):
             s=4
             consume=200
             consume1=24
             consume2=150
             if(resources["water"]<200):
                 print("Insufficient water")
                 s=1
             elif(resources["coffee"]<24):
                 print("Insufficent coffee")
                 s=1
             elif(resources["milk"]<150):
                 print("Inssuficient milk")
                 s=1
             if(resources["water"]>0):
                 resources["water"]=resources.get("water",0)-consume
             if(resources["coffee"]>0):
                   resources["coffee"]=resources.get("coffee",1)-consume1
             if(resources["milk"]>0):
                  resources["milk"]=resources.get("milk",2)-consume2
                  cost+=MENU["latte"]["cost"]
            elif(float(coins)<2.5 and user_inputs=="latte"):
               print("sorry that is not enough money")
               s=1
            if(s==4):
               print("here is your latte,enjoy")
               coins-=2.5
               resources["money"]+=2.5
               s=1
            if(user_inputs=="capachino" and float(coins)>=3):
                s=6
                consume=250
                consume1=24
                consume2=100
                if(resources["water"]<250):
                 print("Insufficient water")
                 s=1
                elif(resources["coffee"]<24):
                 print("Insufficent coffee")
                 s=1
                elif(resources["milk"]<100):
                 print("Inssuficient milk")
                 s=1
                if(resources["water"]>0):
                 resources["water"]=resources.get("water",0)-consume
                if(resources["coffee"]>0):
                 resources["coffee"]=resources.get("coffee",1)-consume1
                if(resources["milk"]>0):
                 resources["milk"]=resources.get("milk",2)-consume2
                 cost+=MENU["capachino"]["cost"]
                if(s==6):
                   print("here is your capachino,enjoy")
                   coins-=3
                   resources["money"]+=3
                   s=1
        if(coins>0):
            print("your change/refunded money",coins)
            s=1
        elif(float(coins)<3 and user_inputs=="capachino"):
            print("sorry that is not enough money")
            s=1
    

        




# TODO 6  check transaction sucess
# TODO 7 Make coffee