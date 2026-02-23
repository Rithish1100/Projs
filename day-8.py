print('''
                                                                                    
                                                 ,--.    ,----..                    
    ,---,.    ,---,    ,---,                   ,--.'|   /   /   \             .---. 
  ,'  .'  \,`--.' |  .'  .' `\             ,--,:  : |  /   .     :           /. ./| 
,---.' .' ||   :  :,---.'     \         ,`--.'`|  ' : .   /   ;.  \      .--'.  ' ; 
|   |  |: |:   |  '|   |  .`\  |        |   :  :  | |.   ;   /  ` ;     /__./ \ : | 
:   :  :  /|   :  |:   : |  '  |        :   |   \ | :;   |  ; \ ; | .--'.  '   \' . 
:   |    ; '   '  ;|   ' '  ;  :        |   : '  '; ||   :  | ; | '/___/ \ |    ' ' 
|   :     \|   |  |'   | ;  .  |        '   ' ;.    ;.   |  ' ' ' :;   \  \;      : 
|   |   . |'   :  ;|   | :  |  '        |   | | \   |'   ;  \; /  | \   ;  `      | 
'   :  '; ||   |  ''   : | /  ;         '   : |  ; .' \   \  ',  /   .   \    .\  ; 
|   |  | ; '   :  ||   | '` ,/          |   | '`--'    ;   :    /     \   \   ' \ | 
|   :   /  ;   |.' ;   :  .'            '   : |         \   \ .'       :   '  |--"  
|   | ,'   '---'   |   ,.'              ;   |.'          `---`          \   \ ;     
`----'             '---'                '---'                            '---"      
                                                                                     
''')
def find_larger_bid(bidding_dict):
    winner=''
    highest_bid=0
    for bidd in bidding_dict:
        bid_amount=bidding_dict[bidd]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner= bidd
    print(f"the winner is{winner},the highest bid amount{highest_bid}.")

bid={}
count_bidding=True
while count_bidding:
    name=input("Enter what is your name\n")
    price=int(input("Enter the bid price\n"))
    bid[name]= price
    a=input("Are there any other user who want to bid if yes type 'y' if no then type 'n'\n").lower()
    if a=='n':
        count_bidding=False
        find_larger_bid(bid)
    elif a=='y':
        print('\n'*20)

    