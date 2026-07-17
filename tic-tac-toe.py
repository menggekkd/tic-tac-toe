# Simple Tic-Tac-Toe
# By 萌哥坑坑哒（编程菜鸡）

# Used pygame-ce (pip install pygame-ce)
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic-Tac-Toe :3")
running = True
game_over = False


# ----- Game logic -----

# 0 = empty, 1 = X, 2 = O
board_data = [
        [0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0]
    ]

# Start with O
current_piece = 2

current_piece_display = 'O'

text_display = f'Current player: {current_piece_display}'

def update_current_piece_display():
    global current_piece_display
    if current_piece == 1:
        current_piece_display = 'X'
    elif current_piece == 2:
        current_piece_display = 'O'
    else:
        current_piece_display = 'None'

# check if a player has won
def check_win(c):
    if board_data[0][0] == c and board_data[0][1] == c and board_data[0][2] == c:
        return True
    if board_data[1][0] == c and board_data[1][1] == c and board_data[1][2] == c:
        return True
    if board_data[2][0] == c and board_data[2][1] == c and board_data[2][2] == c:
        return True
    if board_data[0][0] == c and board_data[1][0] == c and board_data[2][0] == c:
        return True
    if board_data[0][1] == c and board_data[1][1] == c and board_data[2][1] == c:
        return True
    if board_data[0][2] == c and board_data[1][2] == c and board_data[2][2] == c:
        return True
    if board_data[0][0] == c and board_data[1][1] == c and board_data[2][2] == c:
        return True
    if board_data[0][2] == c and board_data[1][1] == c and board_data[2][0] == c:
        return True
    return False

def check_draw():
    for row in board_data:
        for cell in row:
            if cell == 0:
                return False
    return True


# ----- Display -----

# Draw the grid
def draw_grid():
    screen.fill((15, 15, 15))
    pygame.draw.line(screen, (238, 238, 238), (200, 0), (200, 600), 3)
    pygame.draw.line(screen, (238, 238, 238), (400, 0), (400, 600), 3)
    pygame.draw.line(screen, (238, 238, 238), (0, 200), (600, 200), 3)
    pygame.draw.line(screen, (238, 238, 238), (0, 400), (600, 400), 3)

# Draw the pieces
def draw_x(x, y):
    pygame.draw.line(screen, (238, 238, 238), (x + 24, y + 24), (x + 176, y + 176), 6)
    pygame.draw.line(screen, (238, 238, 238), (x + 176, y + 24), (x + 24, y + 176), 6)

def draw_o(x, y):
        pygame.draw.circle(screen, (238, 238, 238), (x + 100, y + 100), 88, 6)

def draw_pieces():
    for y in range(3):
        for x in range(3):
            if board_data[y][x] == 1:
                draw_x(x * 200, y * 200)
            elif board_data[y][x] == 2:
                draw_o(x * 200, y * 200)

def draw_text():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 160, 24))
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render(text_display, True, (238, 238, 238))
    screen.blit(text,(4, 4))


# ----- Game loop -----
while running:
    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Game display
    draw_grid()
    draw_pieces()
    draw_text()

    # Player input
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                index_x = int(x / 200)
                index_y = int(y / 200)

                if board_data[index_y][index_x] == 0:
                    board_data[index_y][index_x] = current_piece
                    if (current_piece == 2):
                        current_piece = 1
                    else:
                        current_piece = 2
                    update_current_piece_display()

    # Check for win or draw
    if (check_win(1)):
        text_display = "X wins!"
        game_over = True
    elif (check_win(2)):
        text_display = "O wins!"
        game_over = True
    elif (check_draw()):
        text_display = "Draw!"
        game_over = True
    else:
        text_display = f'Current player: {current_piece_display}'
    
    pygame.display.flip()

pygame.quit()
