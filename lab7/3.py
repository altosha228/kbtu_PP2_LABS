import pygame

pygame.init()
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

color = (255, 0, 0)
x = 50
y = 50
radius = 25
speed = 20

FPS = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
        
       


        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - radius > 0: y -= speed
        if pressed[pygame.K_DOWN] and y + radius < screen_height: y += speed
        if pressed[pygame.K_LEFT] and x - radius > 0 : x -= speed
        if pressed[pygame.K_RIGHT] and x + radius < screen_width : x += speed


        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (x, y), radius)
        pygame.display.flip()
        FPS.tick(60)