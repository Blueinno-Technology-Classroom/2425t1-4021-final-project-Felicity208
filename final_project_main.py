import pgzrun
from pgzhelper import *
import random
import time




WIDTH = 1200
HEIGHT = 700

player_idle = [
    "player/right/idle/tile000",
    "player/right/idle/tile001",
    "player/right/idle/tile002",
    "player/right/idle/tile003"
]

player_attack = [
    "player/right/attack/tile004",
    "player/right/attack/tile005",
    "player/right/attack/tile006",
    "player/right/attack/tile007",
    "player/right/attack/tile008",
    "player/right/attack/tile009",
    "player/right/attack/tile010"
]

player_attack2 = [
    "player/right/attack2/tile011",
    "player/right/attack2/tile012",
    "player/right/attack2/tile013",
    "player/right/attack2/tile014",
    "player/right/attack2/tile015",
    "player/right/attack2/tile016",
    "player/right/attack2/tile017",
    "player/right/attack2/tile018",
    "player/right/attack2/tile019",
]

player_death = [
    "player/right/death/tile020",
    "player/right/death/tile021",
    "player/right/death/tile022",
    "player/right/death/tile023",
    "player/right/death/tile024",
    "player/right/death/tile025",
    "player/right/death/tile026",
    "player/right/death/tile027",
]

enemy_idle = [
    "enemy/idle/tile000",
    "enemy/idle/tile001",
    "enemy/idle/tile002",
    "enemy/idle/tile003"
]

enemy_attack = [
    "enemy/attack/tile004",
    "enemy/attack/tile005",
    "enemy/attack/tile006",
    "enemy/attack/tile007 copy 2",
    "enemy/attack/tile007 copy 3",
    "enemy/attack/tile007 copy 4",
    "enemy/attack/tile007 copy 5",
    "enemy/attack/tile007 copy",
    "enemy/attack/tile008",
    "enemy/attack/tile009"
]

enemy_attack2 = [
    "enemy/attack2/tile010",
    "enemy/attack2/tile011",
    "enemy/attack2/tile012",
    "enemy/attack2/tile013",
    "enemy/attack2/tile014"
]

enemy_death = [
    "enemy/death/tile015",
    "enemy/death/tile016",
    "enemy/death/tile017",
    "enemy/death/tile018",
    "enemy/death/tile019",
    "enemy/death/tile020"
]






player_spell = [
    "projectiles/player/tile000",
    "projectiles/player/tile001"
]

enemy_spell =[
    "projectiles/enemy/tile002",
    "projectiles/enemy/tile003"
]



backgrounds = [
    "background/typingbg",
    "background/shootingbg",
    "background/gameover-time",
    "background/gameover-hp"
]


player = Actor(player_idle[0])
player.images = player_idle
player.left = -35
player.bottom = HEIGHT + 90 
player.scale = 0.8
player.fps = 6
player.hp = 100

enemy = Actor(enemy_idle [0])
enemy.images = enemy_idle
enemy.right = WIDTH - 20
enemy.bottom = HEIGHT - 40
enemy.scale = 1.6
enemy.fps = 8


player_spells = Actor(player_spell[0])
player_spells.images = player_spell
player_spells.x = 230
player_spells.y = 510
player_spells.scale = 0.2
player_spells.show = False

enemy_spells = Actor(enemy_spell[0])
enemy_spells.images = enemy_spell
enemy_spells.pos = enemy.pos
enemy_spells.scale = 0.3
enemy_spells.show = False

background = Actor(backgrounds[0])
background.x = WIDTH/2
background.y = HEIGHT/2
background.scale = 0.6

questionBank = (['attack', 'spell', 'slash','defeat','slay'])
specialQuestions = (['conquer', 'vanquish', 'triumph', 'overcome'])
question = random.choice(questionBank)
typed = ''
typed_status = 'incomplete'
questions_answered = 0

timer = 10
mode = 1
win = 0



def update():
    global typed, question, typed_status, timer, mode, enemyspells
    
    if round(timer) > 0 and player.hp > 0:
        if mode == 1: 
            if player.image != player_death [-1]:
                player.animate()
            enemy.animate()
            player_spells.animate()
            enemy_spells.animate()
            if round(timer) != 0 and typed_status == 'incomplete':
                timer -= 1/60
            elif round(timer) == 0:
                timer = 0
            if player.hp <= 0 and player.image not in player_death:
                player.images = player_death
            # elif player.hp <= 0 and player.image == player_death [-1]:
            #     player.image = player_death [-1]


            



        if mode == 1:
            if (enemy.collide_pixel(player) or enemy.collide_pixel(player_spells) )and enemy.images != enemy_attack2:
                enemy.images = enemy_death
            if player_attack[-1] == player.image:
                player.images = player_idle
                player.left = 7
                player.bottom = HEIGHT + 38
                player.fps = 6
            if player_attack2[-1] == player.image:
                player.images = player_idle
            if enemy_death [-1] == enemy.image:
                enemy.images = enemy_idle
                enemy.right = WIDTH + 60
                enemy.bottom = HEIGHT + 35
            if enemy_attack [-1] == enemy.image:
                enemy.images = enemy_idle
            if enemy_attack2 [-1] == enemy.image:
                enemy.images = enemy_idle
                enemy.right = WIDTH + 60
                enemy.bottom = HEIGHT + 35
            if player_spells.x <= enemy.x and player.images == player_attack2 and enemy.images not in enemy_death:
                player_spells.show = True
                player_spells.x += 11
                if player_spells.collide_pixel(enemy):
                    player_spells.show = False
            elif player.images not in player_attack2:
                player_spells.pos = player.pos
            if enemy_spells.x >= player.x - 30 and enemy.images == enemy_attack and player.images not in player_death:
                enemy_spells.x -= 15
            elif enemy.images not in enemy_attack:
                enemy_spells.pos = enemy.pos
                enemy_spells.show  = False

    else:
        if player.hp > 0 and round(timer) == 0:
            background.image = backgrounds[2]
            background.scale = 1
        elif player.hp <= 0:
            background.image = backgrounds[3]
            background.scale = 1

    


    
    
def on_key_down(key):
    global typed, question, typed_status, timer, questions_answered, mode
    if round(timer) > 0 and player.hp > 0 and mode == 1:
        if key in range(97, 123):
            #print(chr(key))
            typed += chr(key)
        
        if key == 13:
            typed_status = 'complete'

        if key == 32:
            typed += ' '

        if key == 8:
            typed = typed[0:-1]



        if typed_status == 'complete':
            if typed == question:
                questions_answered += 1
                timer = 10
                typed_status = 'incomplete'
                typed = ''
                if question in specialQuestions:
                    player.images = player_attack2
                else:
                    player.images = player_attack
                    player.x = enemy.left + 60
                    player.fps = 8
                if random.randint(0, 43) >= 30:
                    question = random.choice(specialQuestions)
                else:
                    question = random.choice(questionBank)
            elif typed != question:
                typed = ''
                typed_status = 'incomplete'
                if question in specialQuestions:
                    enemy.images = enemy_attack2
                    enemy.x = player.top
                else:
                    enemy_spells.show = True
                    enemy.images = enemy_attack
                
                if question in specialQuestions:
                    player.hp -= 20
                else:
                    player.hp -= 5


        
def draw():
    screen.clear()
    background.draw()
    if round(timer) > 0 and player.hp > 0 and mode == 1:
        if player_spells.show:
            player_spells.draw()
        if enemy_spells.show:
            enemy_spells.draw()
        screen.draw.filled_rect(Rect(player.x - 35, player.top - 5, 110, 30), 'white')
        screen.draw.filled_rect(Rect(player.x - 30, player.top, 100, 20), 'black')
        screen.draw.filled_rect(Rect(player.x-30, player.top, player.hp, 20), 'green')
        screen.draw.text(question, (20, 100), fontsize=60)
        screen.draw.text(typed, (20, 100), fontsize=60, color='orange')
        screen.draw.text(str(round(timer)), (0, 0), fontsize = 40, color = 'white')
        enemy.draw()
        player.draw()
    elif round(timer) == 0 or player.hp <= 0:
        screen.draw.text("Try again? Press ENTER", center=(WIDTH/2,  600), fontsize = 55, color = 'red')
pgzrun.go()