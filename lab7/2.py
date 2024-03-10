import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Музыкальный плеер")
done = False

# Список песен
songs = [
    "Grand Blue OP intro.wav",
    "OIIAOIIA CAT x AFTER DARK.wav",
    "RX4D - Лучше купи Ryzen (feat. Tessa Amd).wav",
    "Blend S Opening.wav"
]
current_index = 0
paused = False

def playNextSong():
    
    global paused, current_index
    if paused:
        paused = False  
    current_index = (current_index + 1) % len(songs)
    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()

def playPrevSong():
    
    global paused, current_index
    if paused:
        paused = False
    current_index = (current_index - 1) % len(songs)
    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()

def pauseSong():
    
    global paused
    if paused:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    paused = not paused


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 20)

clicked = False  

def draw_button(x, y, w, h, text, action=None):
    
    global clicked
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, GRAY, (x, y, w, h))
        if click[0] and clicked:
            if action:
                action()
            clicked = False  
    else:
        pygame.draw.rect(screen, WHITE, (x, y, w, h))

    pygame.draw.rect(screen, BLACK, (x, y, w, h), 2)

    
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text_surf, text_rect)

def draw_title(x, y, text):
    
    text_surf = font2.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x, y))
    screen.blit(text_surf, text_rect)

clock = pygame.time.Clock()

while not done:
    screen.fill(WHITE)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playNextSong()
            if event.key == pygame.K_LEFT:
                playPrevSong()
            if event.key == pygame.K_SPACE:
                pauseSong()

    
    draw_title(200, 50, f"Now plays: {songs[current_index]}")

    
    draw_button(20, 200, 100, 50, "Prev", playPrevSong)
    draw_button(150, 200, 100, 50, "Play/Pause", pauseSong)
    draw_button(280, 200, 100, 50, "Next", playNextSong)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
