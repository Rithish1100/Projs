def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    turn_right()
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
            if front_is_clear():
                move()
                