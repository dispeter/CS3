import pygame
import time 
import random 
snake_xy = [300, 300]
white = 255
failure = False
blue = 255
length = 0
random_pixel = random.randint(1,10)
def inital():
    pygame.draw.rect(screen, (white,white,white), (snake_xy, (10, 10)))
screen = pygame.display.set_mode((610, 610))
screen.fill((0,0,0))

def where(random_direction):
    length = 0
    # random_pixel = random.randint(1,10)
    failure = False
    # random_direction = random.randint(1,4)
    # while length!=random_pixel and failure == False:
    if screen.get_at(snake_xy)==(0,0,blue):
        print("RIP")
        failure==True
    elif screen.get_at(snake_xy)!= (0,0,blue) and random_direction == 1:#up
        snake_xy[1]-=1
    elif screen.get_at(snake_xy)!= (0,0,blue) and random_direction == 2:#down
        snake_xy[1]+=1
    elif screen.get_at(snake_xy)!= (0,0,blue) and random_direction == 3:#left
        snake_xy[0]-=1
    elif screen.get_at(snake_xy)!= (0,0,blue) and random_direction == 4:#Right 
        snake_xy[0]+=1
    else:
        print("Oops broken")
        failure==True
    length+=1
    pygame.display.update()



def direction():
    random_direction = random.randint(1,4)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, (0,0,blue), ((0, 0) , (0, 610)))
    pygame.draw.rect(screen, (0,0,blue), ((0, 0) , (610, 0)))
    pygame.draw.rect(screen, (0,0,blue), ((610, 0) , (0, 610)))
    pygame.draw.rect(screen, (0,0,blue), ((0, 610) , (610, 0)))
    pygame.display.update()
    random_direction = random.randint(1,4)
    for i in range(0, random_pixel):
        where(random_direction)
pygame.quit()