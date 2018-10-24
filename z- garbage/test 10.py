import pygame
import random
import time
print("Pygame Color Changing Pyrimid")
screen = pygame.display.set_mode((550,500))
r=0
g=0
b=0
color=[r,g,b]
y=80
running=True
drawn=False
screen.fill((255,255,255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
    if drawn==True:
        y=80
        for f in range(0,3):
            n=random.randint(0,255)
            color[f]=n
        time.sleep(0.00000001)
        drawn=False
    while drawn==False:
        for i in range(0,6):
            x=0
            for j in range(6-i):
                x+=50
            for j in range(1,i):
                pygame.draw.rect(screen, color[0:], ((x, y), (50, 50)))
                x+=50
            for i in range(i, 0, -1):
                pygame.draw.rect(screen, color[0:], ((x, y), (50, 50)))
                x+=50
            y+=50
        drawn=True
    pygame.display.update()
pygame.quit()
