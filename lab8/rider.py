import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COINS = 0


# setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
# setting up texts
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")


DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 



class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
      
 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(original_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0) 
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)


#Setting up sprites
P1 = Player()
E1 = Enemy()
C = Coin()

#Creating sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)

#Adding a new user event
INC_SPEED = pygame.USEREVENT + 1
#Calling INC_SPEED event every second
pygame.time.set_timer(INC_SPEED, 1000)
 
while True:     
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    DISPLAYSURF.blit(background, (0,0))
    coins = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins, (10, 10))


    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    if pygame.sprite.collide_rect(P1, C):
        COINS += 1
        C.rect.top = 0
        C.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound("crash.wav").play()
          time.sleep(0.5)

          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30, 250))
          pygame.display.update()
          
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()
         
    pygame.display.update()
    FramePerSec.tick(FPS)