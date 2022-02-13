# Purpose: create the game, move the targets, mouse press and key press functions. Premise of the game is to click as
# many targets in the center before the targets are off the screen. Records your high score.

from bullseye import Bullseye
from cs1lib import *
from random import randint

#iniatilize variables, set height and width
H = 1000
W = 1000
N = 100
mpress_x = None
mpress_y = None
blist = []
game_over = False
score = 0
high_score = 0
rpressed = False

# create N number of targets, add them to the list of targets
for i in range(N):
    x = randint(100, W-100)
    y = randint(100, H-100)
    size = randint(5, 30)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    b = Bullseye(x, y, size, vx, vy)
    blist.append(b)

# mouse press callback function
def my_mpress(mx, my):
    global mpress_x, mpress_y, rpressed
    mpress_x = mx
    mpress_y = my
    # call check_click to see if mouse is within a target, if it isn't display game over
    res = check_click(mpress_x, mpress_y)
    if res == False:
        display_game_over()
        rpressed = False


# creates the score counter in top left corner of the game
def draw_score_counter():
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_fill_color(0, 1, 0.8)
    draw_rectangle(0, 0, 100, 100)
    set_font_size(20)
    set_font("Times")
    draw_text("Score:" + str(score), 20, 50)

# game over screen if you click outside of a target
def display_game_over():
    global game_over, high_score
    game_over = True
    enable_stroke()
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 0, 0)
    set_font_size(100)
    draw_text("GAME OVER", 200, 500)
    set_font_size(50)
    set_stroke_color(0, 1, 0.8)
    # updating the high score if needed
    if score > high_score:
        high_score = score
        draw_text("New high score!", 270, 600)
    draw_text("Your score: " + str(score), 270, 650)
    draw_text("High score: " + str(high_score), 270, 700)
    set_font_size(20)
    draw_text("Press r to restart", 290, 800)

#checks whether mouse click is within any of the center of the targets in the bullseye list
def check_click(x, y):
    global mpress_x, mpress_y, score
    # loop through targets
    for i in range(len(blist) - 1, -1, -1):
        #call within_bullseye method and update score if it returns true
        if blist[i].within_bullseye(x, y):
            del blist[i]
            mpress_x = -1
            mpress_y = -1
            #update score depending on how big the target clicked is
            if 0 < blist[i].size <= 10:
                score = score + 25
            elif 10 < blist[i].size <= 20:
                score = score + 15
            elif 20 < blist[i].size:
                score = score + 10
            return True
    return False

# key press callback function
def mykey_press(value):
    global rpressed, score
    # restart game if r is pressed
    if value == "r":
        rpressed = True
        score = 0
        # delete the target list so it's empty for next game
        for i in range(len(blist)-1, -1, -1):
            del blist[i]
        # create new targets and add to target list
        for i in range(N):
            x = randint(90, W - 30)
            y = randint(90, H - 30)
            size = randint(5, 30)
            vx = randint(-5, 5)
            vy = randint(-5, 5)
            b = Bullseye(x, y, size, vx, vy)
            blist.append(b)
    # quit game if q is pressed
    if value == "q":
        cs1_quit()

# main draw function for start_graphics to call
def main_draw():
    global mpress_x, mpress_y
    if game_over == False or rpressed == True:
        set_clear_color(1, 1, 1)
        clear()
        for i in range(len(blist)):
            blist[i].update()
            blist[i].draw()
        draw_score_counter()


start_graphics(main_draw, width=W, height=H, mouse_press=my_mpress, key_press=mykey_press)