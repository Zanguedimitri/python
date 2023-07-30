import pygame
import random
import time
pygame.init()
black=(0,0,0)
largueur, hauteur = 450, 500
fenetre = pygame.display.set_mode((largueur, hauteur), pygame.RESIZABLE)
x,y = 15,25
a=random.randint(400,449)
b=random.randint(400,499)

serpent=pygame.image.load("serpent.png").convert()
nourriture=pygame.image.load("nourriture.png").convert()
fenetre.blit(nourriture,(a,b))
fenetre.blit(serpent,(x,y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            largueur=event.w
            hauteur=event.h
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        y -=1 
    
    elif keys [pygame.K_DOWN]:
        y +=1
    
    elif keys[pygame.K_LEFT]:
        x -=1
    
    elif keys[pygame.K_RIGHT]:
        x +=1
    
    if pygame.Rect(x,y,serpent.get_width(),serpent.get_height()).colliderect(pygame.Rect(a,b,nourriture.get_width(),nourriture.get_height())) :
            fenetre.fill(black)
            a=random.randint(1,largueur)
            b=random.randint(1,hauteur)
            serpent=pygame.image.load("serpent.png").convert()
            corps=pygame.image.load("corps.png").convert()
            fenetre.blit(serpent,(x,y))
        

    fenetre.fill(black)
    nourriture=pygame.image.load("nourriture.png").convert()
    serpent=pygame.image.load("serpent.png").convert()
    fenetre.blit(serpent,(x,y))
    fenetre.blit(nourriture,(a,b))
 


    pygame.display.flip() 
pygame.quit()