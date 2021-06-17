import pgzrun
import random

WIDTH = 800
HEIGHT = 600
bowl = Actor('basket')
bowl.x = WIDTH // 2
bowl.y = HEIGHT - 40

apples = []

game_timer = 10
timer_decrement = 0.2
game_timer_start = 10


def makeApple():
    apples.append(Actor('apple'))
    apples[-1].x = random.randint(40, WIDTH - 40)
    apples[-1].y = -100


makeApple()
score = 0


def drawScore():
    screen.draw.text("score: " + str(score), (45, 30))
    screen.draw.text("Time: " + str(round(game_timer)), (60, 60))


def draw():
    screen.clear()
    screen.blit('skybg', (0, 0))

    if game_timer <= 0:
        screen.clear()
        screen.blit('skybg', (0, 0))
        display_text = "Game Over\nScore " + str((score))
        screen.draw.text(display_text, fontsize=60, center=(400, 300), shadow=(1, 1), color=(255, 255, 255),
                         scolor="#202020")
    bowl.draw()
    drawScore()
    for apple in apples:
        apple.draw()


def update():
    global score, game_timer, game_timer_start
    if game_timer <= 0:
        return
    else:
        game_timer -= 0.017

    if keyboard.left:
        bowl.x -= 5
    elif keyboard.right:
        bowl.x += 5

    for apple in apples:
        if apple.y > HEIGHT + 40:
            apple.y = -100
            apple.x = random.randint(40, WIDTH - 40)
        else:
            apple.y += 10
    for apple in apples:
        if apple.colliderect(bowl):
            score += 1
            game_timer = game_timer_start - (score * timer_decrement)
            apples.remove(apple)
            makeApple()


pgzrun.go()
