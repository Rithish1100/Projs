import random
def dealcard():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,computer_score):
    if u_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "lose.opponent has blackjack"
    elif u_score > 21:
        return "you went over.you lose"
    elif computer_score >21:
        return "opponent went over.you win"
    elif u_score > computer_score:
        return "you win"
    else:
        return"you lose"
def play_game():
    usercards=[]
    computercards=[]
    is_game_over= False
    computer_score = -1
    user_score = -1
    for i in range(2):
        usercards.append(dealcard())
        computercards.append(dealcard())
    while not is_game_over:
        user_score= calculate_score(usercards)
        computer_score=calculate_score(computercards)

        print(f"your cards:{usercards},current score:{user_score}")
        print(f"computers first card :{computercards[0] }")

        if user_score == 0 or user_score > 21 or computercards == 0:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to draw card ,type 'n' to pass:")
            if user_should_deal == 'y':
                usercards.append(dealcard())
            else:
                is_game_over = True
    while calculate_score != 0 and computer_score < 17:
        computercards.append(dealcard())
        dealer_score = calculate_score(computercards)
    print(f"your final score: {usercards},final score:{user_score}")
    print(f"computer final hand:{computercards},final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play a game of blackjack? type 'y'or 'n'") == "y":
    print("\n"*20)

    play_game()