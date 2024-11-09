import pgzrun
from pgzhelper import *
import random

WIDTH = 1000
HEIGHT = 800

warrior_idle = [
    'warrior/idle/tile000' ,
    'warrior/idle/tile001' ,
    'warrior/idle/tile002' ,
    'warrior/idle/tile003' ,
    'warrior/idle/tile004' ,
    'warrior/idle/tile005' ,
    'warrior/idle/tile006' ,
    'warrior/idle/tile007' ,
    'warrior/idle/tile008' ,
    'warrior/idle/tile009'
]

warrior_attack = [
    'warrior/attack/tile000',
    'warrior/attack/tile001',
    'warrior/attack/tile002',
    'warrior/attack/tile003'
]

zombie_run = [
    'zombie/run/tile002', 
    'zombie/run/tile003',
    'zombie/run/tile004',
    'zombie/run/tile005',
]

zombie_death = [
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

warrior = Actor(warrior_idle[0])
warrior.images = warrior_idle

zombie = Actor(zombie_run[0])
zombie.images = zombie_run


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
    zombie.animate()
    warrior.animate()
    if warrior_attack[-1] == warrior.image:
        warrior.images = warrior_idle
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
