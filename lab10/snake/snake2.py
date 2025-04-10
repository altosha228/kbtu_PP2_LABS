import pygame
import random
import psycopg2

pygame.init()

W, H = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 223, 186)
RED = (255, 0, 0)

font = pygame.font.SysFont("comicsansms", 10)
large_font = pygame.font.SysFont("comicsansms", 20)

# Функция для генерации еды
def generate_food(snake):
    while True:
        new_food = (random.randint(0, (W // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (H // CELL_SIZE) - 1) * CELL_SIZE)
        if new_food not in snake:
            return new_food, random.randint(1, 3), pygame.time.get_ticks()

# Функция для ввода имени игрока
def get_player_name():
    input_box = pygame.Rect(W // 4, H // 3, W // 4, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = False
    font = pygame.font.SysFont('comicsansms', 16)
    
    clock = pygame.time.Clock()
    
    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        # Отображаем текст
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        # Отображаем подсказку
        prompt_text = font.render("Enter your name:", True, WHITE)
        screen.blit(prompt_text, (W // 4, H // 4))

        pygame.display.flip()
        clock.tick(30)

# Основная игра
def main():
    name = get_player_name()  # Получаем имя игрока перед началом игры
    snake = [(100, 100), (90, 100), (80, 100)]
    snake_dir = (CELL_SIZE, 0)
    food, food_weight, food_spawn_time = generate_food(snake)
    score = 0
    level = 1
    speed = 10
    running = True
    game_over = False
    food_lifetime = 5000  

    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        new_dir = snake_dir

        if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
            new_dir = (-CELL_SIZE, 0)
        if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
            new_dir = (CELL_SIZE, 0)
        if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
            new_dir = (0, -CELL_SIZE)
        if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
            new_dir = (0, CELL_SIZE)

        if not game_over:
            snake_dir = new_dir
            new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

            if new_head[0] < 0 or new_head[0] >= W or new_head[1] < 0 or new_head[1] >= H or new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)

                if new_head == food:
                    score += food_weight  
                    if score % 3 == 0:
                        level += 1
                        speed += 2
                    food, food_weight, food_spawn_time = generate_food(snake)
                else:
                    snake.pop()

                if pygame.time.get_ticks() - food_spawn_time > food_lifetime:
                    food, food_weight, food_spawn_time = generate_food(snake)

            pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

            for segment in snake:
                pygame.draw.rect(screen, YELLOW, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

            score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
            screen.blit(score_text, (10, 10))
        else:
            game_over_text = large_font.render(f"Game Over, {name}! Press SPACE", True, WHITE)
            screen.blit(game_over_text, (W // 6, H // 3))
            if keys[pygame.K_SPACE]:
                main()
                return

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()

if __name__ == "__main__":
    main()
