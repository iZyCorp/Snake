import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = {
    'position': [100, 50],
    'body': [[100, 50], [90, 50], [80, 50]],
    'direction': 'RIGHT'
}

food = {
    'position': [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
}

game = {
    'score': 0,
    'time': pygame.time.Clock(),
    'alive': True,
}

def show_score():
    font = pygame.font.SysFont('times new roman', 20)
    score = font.render('Score : ' + str(game['score']), True, (255, 255, 255))
    score_rect = score.get_rect()
    score_rect.midtop = (WIDTH / 2, 10)
    screen.blit(score, score_rect)

def show_death_screen():
    font = pygame.font.SysFont('times new roman', 20)
    title = font.render('Vous êtes hélas décédé :/', True, (255, 30, 255))
    title_rect = title.get_rect()
    title_rect.midtop = (WIDTH / 2, 20)
    screen.blit(title, title_rect)

def handle_inputs():
    for event in pygame.event.get():

        # When the player quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Snake moves
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake['direction'] != 'DOWN':
                snake['direction'] = 'UP'
            elif event.key == pygame.K_DOWN and snake['direction'] != 'UP':
                snake['direction'] = 'DOWN'
            elif event.key == pygame.K_LEFT and snake['direction'] != 'RIGHT':
                snake['direction'] = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake['direction'] != 'LEFT':
                snake['direction'] = 'RIGHT'

def update_snake():
    if snake['direction'] == 'UP':
        snake['position'][1] -= 10
    if snake['direction'] == 'DOWN':
        snake['position'][1] += 10
    if snake['direction'] == 'LEFT':
        snake['position'][0] -= 10
    if snake['direction'] == 'RIGHT':
        snake['position'][0] += 10

    snake['body'].insert(0, list(snake['position']))

    if snake['position'] == food['position']:
        game['score'] += 1
        food['position'] = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
    else:
        snake['body'].pop()

def draw_elements():
    screen.fill((0, 0, 0))

    for pos in snake['body']:
        pygame.draw.rect(screen,(0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food['position'][0], food['position'][1], 10, 10))
    show_score()
    pygame.display.flip()


def check_collision():
    if (snake['position'][0] < 0 or snake['position'][0] >= WIDTH or
        snake['position'][1] < 0 or snake['position'][1] >= HEIGHT):
        game["alive"] = False

    for block in snake['body'][1:]:
        if snake['position'] == block:
            game["alive"] = False

while True:

    if not game['alive']:
        show_death_screen()
        pygame.display.flip()

    else:
        update_snake()
        check_collision()

    handle_inputs()
    draw_elements()

    game['time'].tick(15)
