#################################################################
# FILE : hello_turtle.py
# WRITER : Shani Kehati, shani , 322866823
# EXERCISE : intro2cs ex1 (2021)
# DESCRIPTION: A simple program that draws a flower bed containing three flowers
##### WEB PAGES I USED: stackoverflow for a linux problem
#############################################################
import turtle as t


def move_30():
    ''' calls the t.forward method with a value of 30
        bcos it is very frequent in this exercise
    '''
    t.forward(30)


def draw_petal():
    '''draws a petal with turtle'''
    move_30()  # 1
    t.right(45)  # 2
    move_30()  # 3
    t.right(135)  # 4 turn right 135 deg
    move_30()  # 5
    t.right(45)  # 6
    move_30()  # 7
    t.right(135)  # 8 turn right 135 deg


def draw_flower():
    '''draws a flower made of 4 petals with turtle (using draw_petal)'''
    t.left(45)
    draw_petal()
    t.left(90)
    draw_petal()
    t.left(90)
    draw_petal()
    t.left(90)
    draw_petal()
    t.left(135)
    t.forward(150)


def draw_flower_and_advance():
    '''draws a flower and moves the turtle - to prepare for another flower (using draw_flower)'''
    draw_flower()
    t.right(90)
    t.up()
    t.forward(150)
    t.right(90)
    t.forward(150)  # *
    t.left(90)
    t.down()


def draw_flower_bed():
    ''' draws a flower bed from 3 flowers (using draw_flower_and_advance)'''
    t.up()
    t.forward(200)  # *
    t.left(180)
    t.down()
    for i in range(3):
        draw_flower_and_advance()


if __name__ == "__main__":
    draw_flower_bed()
    t.done()
