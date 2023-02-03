def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while front_is_clear != True:
    if at_goal() == True:
        done()
    elif wall_in_front() == True:
        jump()
    elif front_is_clear():
        move()
