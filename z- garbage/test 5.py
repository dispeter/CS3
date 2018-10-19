import pygame

x = 0
y = 0
screen = pygame.display.set_mode((500, 500))

running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

   for x in range(0,600,100):
       for y in range(0,600,100):
           if (x==200 and x==y) or (x==400 and x==y) or (x==0 and x==y):
               pygame.draw.rect(screen, (255, 255, 255), ((x,y), (100 , 100)))
           elif (y==200 and y==400-x) or (y==400 and y==400-x) or (y==0 and y==400-x):
               pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
           elif y==200 or y==400 or y==0:
               pygame.draw.rect(screen, (255, 255, 255), ((0,y), (100 , 100)))
           elif x==300 or x==500 or x==100:
               pygame.draw.rect(screen, (255, 255, 255), ((x,y), (100 , 100)))
           elif (x==200 and y%200==0):
               pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
           elif (y==200 and x%200==0):
               pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))  
           


   pygame.display.update()
pygame.quit()

