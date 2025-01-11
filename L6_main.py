import pgzrun
from pgzhelper import *
import random

WIDTH = 1000
HEIGHT = 800

player_idle = [
    'player/idle/tile000',
    'player/idle/tile001',
    'player/idle/tile002',
    'player/idle/tile003'
]

player_attack = [
    'player/attack/tile004',
    'player/attack/tile005',
    'player/attack/tile006',
    'player/attack/tile007',
    'player/attack/tile008',
    'player/attack/tile009',
    'player/attack/tile010'
]

player_attack2 = [
    'player/attack2/tile011',
    'player/attack2/tile012',
    'player/attack2/tile013',
    'player/attack2/tile014' ,
    'player/attack2/tile015',
    'player/attack2/tile016',
    'player/attack2/tile017',
    'player/attack2/tile018',
    'player/attack2/tile019'
]

enemy_idle = [
    'zombie/tile000', 
    'zombie/tile001',
    'zombie/tile002',
    'zombie/tile003',
]

enemy_death = [
    'zombie/die/tile014',
    'zombie/die/tile015',
    'zombie/die/tile016',
    'zombie/die/tile017',
    'zombie/die/tile018',
    'zombie/die/tile019',
    'zombie/die/tile020',
    'zombie/die/tile021',
    'zombie/die/tile022',
    'zombie/die/tile023',
    'zombie/die/tile024'
]

player = Actor(player_idle[0])
player.images = player_idle

enemy = Actor(enemy_idle[0])
enemy.images = enemy_idle


zombie.scale = 4
zombie.right = WIDTH + 60
zombie.bottom = HEIGHT - 30
zombie.fps = 4

warrior.scale = 5
warrior.x = 90
warrior.y = HEIGHT - 140
warrior.fps = 6

questionBank = (['attorney', 'apollo j', 'athena c'])
question = random.choice(questionBank)
typed = ''

def update():
    player.animate()
    enemy.animate()
    if player_attack[-1] == player.image:
        player.images = player_idle
        warrior.x = 90
    if zombie_death[-1] == zombie.image:
        zombie.images = zombie_run

    

def on_key_down(key):
    global typed, question
    
    
    if key in range(97, 123):
        #print(chr(key))
        typed += chr(key)
    
    if key == 32:
        typed += ' '

    if key == 8:
        typed = typed[0:-1]


    if typed == question:
        typed = ''
        warrior.images = warrior_attack
        warrior.x = zombie.left - 30
        zombie.images = zombie_death
        question = random.choice(questionBank)





def draw():
    screen.clear()
    screen.draw.text(question, (20, 100), fontsize=60)
    screen.draw.text(typed, (20, 100), fontsize=60, color='orange')
    zombie.draw()
    warrior.draw()


pgzrun.go()
