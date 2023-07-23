import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLOCK_SIZE = 20

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
        
def draw_food(food_position):
    pygame.draw.rect(screen, RED, [food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE])

def update_food():
    return [random.randrange(0, SCREEN_WIDTH-BLOCK_SIZE,BLOCK_SIZE), random.randrange(0, SCREEN_HEIGHT-BLOCK_SIZE,BLOCK_SIZE)]

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Game Ular')

clock = pygame.time.Clock()

def main():
    game_over = False
    game_close = False

    snake_x = SCREEN_WIDTH / 2
    snake_y = SCREEN_HEIGHT / 2

    snake_body = []
    length_of_snake = 1

    food_position = update_food()

    while not game_over:
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 50)
        message = font.render("Kalah!! Tekan SPACE untuk bermain lagi atau ESC untuk keluar", True, GREEN)
        screen.blit(message, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    game_over = True
                    game_close = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -BLOCK_SIZE
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = BLOCK_SIZE
                    snake_x_change = 0
            
            if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
                game_close = True

            snake_x += snake_x_change
            snake_y += snake_y_change

            screen.fill(WHITE)
            draw_food(food_position)

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)

        if len(snake_body) > length_of_snake:
            del snake_body[0]

        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_body)

        pygame.display.update()

        if snake_x == food_position[0] and snake_y == food_position[1]:
            food_position == update_food()
            length_of_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()