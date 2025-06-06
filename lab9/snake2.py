import pygame
import random
import psycopg2
from db import insert

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

def generate_food(snake):
    while True:
        new_food = (random.randint(0, (W // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (H // CELL_SIZE) - 1) * CELL_SIZE)
        if new_food not in snake:
            return new_food, random.randint(1, 3), pygame.time.get_ticks()

def get_player_name():
    input_box = pygame.Rect(W // 4, H // 3, W // 4, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = False
    font = pygame.font.SysFont('comicsansms', 16)
    
    error_message = ''
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
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(insert.check_for_identity(text))
                        if insert.check_for_identity(text):
                            error_message = "Это имя уже занято, попробуйте другое."
                            continue
                        else:
                            return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        error_message = ''  # Очистка ошибки

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        prompt_text = font.render("Enter your name:", True, WHITE)
        screen.blit(prompt_text, (W // 4, H // 4))

        if error_message:
            error_surface = font.render(error_message, True, pygame.Color('red'))
            screen.blit(error_surface, (W // 4, H // 3 + 50))

        pygame.display.flip()
        clock.tick(30)

def show_game_over(name, score):
    insert.insert(name, score)

    while True:
        screen.fill(BLACK)
        game_over_text = large_font.render(f"Game Over, {name}!", True, WHITE)
        restart_text = font.render("Press SPACE to restart or ESC to exit", True, WHITE)
        final_score_text = font.render(f"Your score: {score}", True, YELLOW)

        screen.blit(game_over_text, (W // 4, H // 3))
        screen.blit(restart_text, (W // 4, H // 3 + 40))
        screen.blit(final_score_text, (W // 4, H // 3 + 70))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()  # Рестарт
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def main():
    name = get_player_name()
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
                pygame.quit()
                exit()

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
                break
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

        pygame.display.flip()
        clock.tick(speed)

    show_game_over(name, score)  # Обрабатываем game over

if __name__ == "__main__":
    main()
