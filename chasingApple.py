import pgzrun
import random
WIDTH = 800
HEIGHT = 600
basket = Actor('basket')
basket.x = WIDTH // 2
basket.y = HEIGHT - 40
apple = Actor('apple')
is_game_over = False
game_timer = 10
score = 0
def position_fruit():
    apple.x = random.randint(40, WIDTH - 40)
    apple.y = -100
def draw_score():
    screen.draw.text("score: " + str(score), (45, 30))
    screen.draw.text("Time: " + str(round(game_timer)), (45, 60))
    if is_game_over:
        display_text = "Game Over\nScore " + str((score))
        position=((WIDTH//2)-100, (HEIGHT//2))
        screen.draw.text(display_text,position, fontsize=60, color=(255, 255, 255))
def move_basket():
    if keyboard.left:
        basket.x -= 5
    elif keyboard.right:
        basket.x += 5
def apple_fall():
    if apple.y > HEIGHT + 40:
        position_fruit()
    else:
        apple.y += 10
    check_collision()  
def check_collision():
    global score 
    
    if apple.colliderect(basket):
        sounds.pop.play()
        score += 1
        position_fruit()
def draw():
    global game_timer,isgame
    screen.clear()
    screen.blit('skybg', (0, 0))
    draw_score()
    basket.draw()
    apple.draw()
def update():
    global game_timer,is_game_over
    
    if not is_game_over:
        move_basket()
        apple_fall()
       
        if game_timer<=0:
            sounds.gameover.play()
            is_game_over = True
        else:
            game_timer -= 0.017
position_fruit()
pgzrun.go()