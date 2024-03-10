from datetime import datetime
import pygame

w, h = 1400, 1050
run = True

pygame.init()

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

background = pygame.image.load("MickeyClock.jpg")
big_hand = pygame.image.load("big_hand.png")   # Минутная стрелка
small_hand = pygame.image.load("small_hand.png")  # Часовая стрелка

original_rect_sh = small_hand.get_rect(center=(w // 2, h // 2))
original_rect_bh = big_hand.get_rect(center=(w // 2, h // 2))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("BYE BYE !")

    screen.blit(background, (0, 0))

    now = datetime.now()
    hours = now.hour % 12  # Преобразуем 24-часовой формат в 12-часовой
    minutes = now.minute

    # Часовая стрелка (каждый час = 30° + дополнительный угол от минут)
    hour_angle = hours * -30 + (minutes / 60) * -30  
    rotated_sh = pygame.transform.rotate(small_hand, hour_angle)
    rotated_rect_sh = rotated_sh.get_rect(center=original_rect_sh.center)

    # Минутная стрелка (каждая минута = 6°)
    minute_angle = minutes * -6
    rotated_bh = pygame.transform.rotate(big_hand, minute_angle)
    rotated_rect_bh = rotated_bh.get_rect(center=original_rect_bh.center)

    screen.blit(rotated_sh, rotated_rect_sh.topleft)
    screen.blit(rotated_bh, rotated_rect_bh.topleft)

    print(f"Hours = {hours}, Minutes = {minutes}")

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
