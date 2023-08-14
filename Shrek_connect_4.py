'''
Alright, this isn't some random old classic Connect 4 game. This is Shrek's Connect 4, designed after
Dreamworks' second best film series (after Puss in Boots). Now, the two-player game is a simple brawl--
Shrek vs. Donkey--to see who can win the Golden Onion Token. That's a friendly brawl. Now, the singleplayer
option is more serious. Here, you're in an adventure up against this Lord Farquaad buffoon. If you win, you
reclaim the swamp from Farquaad and regain Fiona from his possession. But don't lose, or else Farquaad seizes
the swamp and takes Fiona to the Duloc Kingdom. You think maybe he's compensating for something?
S
Think strategically and make wise moves.
'''
import random
import pygame
import numpy as np
import sys
pygame.mixer.init()
pygame.init()

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.font.init()

pygame.display.set_caption("Shrek's Connect 4")
screen = pygame.display.set_mode((900, 500), 0, 30)

# IMAGES BEING ADDED TO PROGRAM
shrekImg = pygame.image.load('shrek.jpeg')
donkeyImg = pygame.image.load('donkey.jpeg')
shrekfrownImg = pygame.image.load('shrekfrown.jpeg')
donkeyfrownImg = pygame.image.load('donkeyfrown.jpeg')
farquaadImg = pygame.image.load('farquaad.jpeg')
swampImg = pygame.image.load('swamp.jpeg')
dulaccastleImg = pygame.image.load('farquaadcastle.jpeg')
shreksmileImg = pygame.image.load('shreksmile.jpeg')
damagedswampImg = pygame.image.load('damagedswamp.jpeg')
triumphantfarquaadImg = pygame.image.load('triumphantfarquaad.jpeg')
shrekstandingImg = pygame.image.load('shrekstanding.jpeg')
greatswampImg = pygame.image.load('greatswamp.jpeg')
onionImg = pygame.image.load('onion.jpeg')
dreamworksImg = pygame.image.load('dreamworks.jpeg')
# RESCALING THE IMAGES
real_donkeyImg = pygame.transform.scale(donkeyImg, (330, 460))
real_shrekImg = pygame.transform.scale(shrekImg, (300, 439))
real_shrekfrownImg = pygame.transform.scale(shrekfrownImg, (360, 350))
real_donkeyfrownImg = pygame.transform.scale(donkeyfrownImg, (300, 350))
real_farquaadImg = pygame.transform.scale(farquaadImg, (300, 350))
real_swampImg = pygame.transform.scale(swampImg, (1000, 550))
real_dulaccastleImg = pygame.transform.scale(dulaccastleImg, (1000, 700))
real_shreksmileImg = pygame.transform.scale(shreksmileImg, (400, 350))
real_damagedswampImg = pygame.transform.scale(damagedswampImg, (500, 400))
real_triumphantfarquaadImg = pygame.transform.scale(triumphantfarquaadImg, (400, 800))
real_shrekstandingImg = pygame.transform.scale(shrekstandingImg, (500, 700))
real_greatswampImg = pygame.transform.scale(greatswampImg, (1000, 1000))
real_onionImg = pygame.transform.scale(onionImg, (300, 400))
real_dreamworksImg = pygame.transform.scale(dreamworksImg, (700, 900))
# FONTS
font2 = pygame.font.SysFont('Roboto', 50)
title_font = pygame.font.SysFont('Oswald', 100)
winning_font = pygame.font.SysFont('Oswald', 25)




# color assignment
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (80, 250, 120)

BROWN = (150, 75, 0)
RED = (178,34,34)
WHITE = (250, 250, 250)

def draw_text(text, font2, color, surface, x, y):
    textobj = font2.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# global setting for variable...for checking later
click = False

# main menu function
def main_menu():
    while True:
        global screen, label
        # global assignment to screen and label--will come in handy

        screen.fill((0, 190, 100))
        screen.blit(real_swampImg, (0, 0))
        draw_text("SHREK'S CONNECT 4", title_font, (50, 200, 90), screen, 110, 30)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(330, 167, 260, 60)
        button_2 = pygame.Rect(330, 310, 260, 60)

        if button_1.collidepoint((mx, my)):
            # If the player clicks this button, button_1, game starts
            global click
            if click:
                screen.fill((0, 190, 100))

                mx, my = pygame.mouse.get_pos()


                pygame.quit()
                SQUARE_SIZE = 100

                ROWS = 6
                COLS = 7

                # Below is a large set of functions assigned to specific tasks


                def create_board():
                    board = np.zeros((ROWS, COLS))
                    return board
                # creating the board
                def print_board(board):
                    print(np.flipud(board))
                # displaying the board
                def is_valid_location(board, col):
                    return board[5][col] == 0
                # when a spot on the board is clicked
                def get_next_open_row(board, col):
                    for r in range(ROWS):
                        if board[r][col] == 0:
                            return r

                # whatever row is available, acknowledging taken spaces
                def drop_piece(board, row, col, turn):
                    board[row][col] = turn
                # function to drop the piece

                # Here is a large function to be called when someone has connected 4
                def winning_move(board, turn):
                    # diagonal up right
                    for r in range(ROWS - 3):
                        for c in range(COLS - 3):
                            if board[r][c] == turn and board[r + 1][c + 1] == turn and board[r + 2][c + 2] == turn and \
                                    board[r + 3][
                                        c + 3] == turn:
                                return True
                    # horizontal
                    for r in range(ROWS):
                        for c in range(COLS - 3):
                            if board[r][c] == turn and board[r][c + 1] == turn and board[r][c + 2] == turn and board[r][
                                c + 3] == turn:
                                return True
                    # vertical
                    for r in range(ROWS - 3):
                        for c in range(COLS):
                            if board[r][c] == turn and board[r + 1][c] == turn and board[r + 2][c] == turn and \
                                    board[r + 3][c] == turn:
                                return True
                    # diagonal down
                    for r in range(ROWS - 3):
                        for c in range(COLS - 3):
                            if board[r][c] == turn and board[r - 1][c + 1] == turn and board[r - 2][c + 2] == turn and \
                                    board[r - 3][
                                        c + 3] == turn:
                                return True
                    # diagonal up left
                    for r in range(ROWS - 3):
                        for c in range(3, COLS):
                            if board[r][c] == turn and board[r + 1][c - 1] == turn and board[r + 2][c - 2] == turn and \
                                    board[r + 3][
                                        c - 3] == turn:
                                return True
                    return False





                # size of square
                SQUARE_SIZE = 100

                # piece radius
                RADIUS = (SQUARE_SIZE / 2) - 5

                # function to display the board when a move is played
                def draw_board(board):
                    for c in range(COLS):
                        for r in range(ROWS):
                            pygame.draw.rect(screen, (1, 50, 32),
                                             (SQUARE_SIZE * c, SQUARE_SIZE * (r + 1), SQUARE_SIZE, SQUARE_SIZE))
                            pygame.draw.circle(screen, BLACK, (
                            SQUARE_SIZE * c + SQUARE_SIZE // 2, SQUARE_SIZE * (r + 1) + SQUARE_SIZE // 2), RADIUS)
                    for c in range(COLS):
                        for r in range(ROWS):
                            if board[r][c] == 1:
                                pygame.draw.circle(screen, GREEN, (
                                SQUARE_SIZE * c + SQUARE_SIZE // 2, h - (SQUARE_SIZE * r + SQUARE_SIZE // 2)), RADIUS)
                            if board[r][c] == 2:
                                pygame.draw.circle(screen, BROWN, (
                                SQUARE_SIZE * c + SQUARE_SIZE // 2, h - (SQUARE_SIZE * r + SQUARE_SIZE // 2)), RADIUS)
                            if board[r][c] == 2 and ComputerPlay:
                                pygame.draw.circle(screen, RED, (
                                SQUARE_SIZE * c + SQUARE_SIZE // 2, h - (SQUARE_SIZE * r + SQUARE_SIZE // 2)), RADIUS)

                '''
                AI PART (SINGLE-PLAYER)
                '''

                def AI_make_move_rand(board, turn):
                    # Make a list of all legal moves
                    legal_moves = []

                    for col in range(COLS):
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            legal_moves.append((row, col))
                    # Choose one randomly
                    move = random.randrange(0, len(legal_moves))
                    return legal_moves[move]

                def AI_make_move_win_one_not_lose_two(board, turn):
                    legal_moves = []
                    for col in range(COLS):
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            legal_moves.append((row, col))

                    optional_moves = []  # Will include all moves which are not losing moves
                    for move in legal_moves:
                        r, c = move
                        # execute the move on the board
                        board[r][c] = turn
                        # check if this board is winning
                        is_winning = winning_move(board, turn)
                        # if winning, return this move
                        if is_winning:
                            # undo move on board

                            board[r][c] = 0
                            print(f'Found Winning Move: {move}')
                            return move
                        # Check if losing move
                        # Everything will be with _2
                        losing_move = False

                        if turn == 1:
                            turn_2 = 2
                        else:
                            turn_2 = 1
                        legal_moves_2 = []
                        for col_2 in range(COLS):
                            if is_valid_location(board, col_2):
                                row_2 = get_next_open_row(board, col_2)
                                legal_moves_2.append((row_2, col_2))

                        for move_2 in legal_moves_2:
                            r_2, c_2 = move_2
                            # execute the move on the board
                            board[r_2][c_2] = turn_2
                            # check if this board is winning
                            is_winning = winning_move(board, turn_2)
                            # if winning, return this move
                            if is_winning and game_over == False:


                                losing_move = True
                                # print(f'Found a losing move: move1 = {move}, move2 = {move_2}')
                                # undo move on board
                            board[r_2][c_2] = 0

                        # undo move on board
                        board[r][c] = 0
                        if not (losing_move):
                            optional_moves.append(move)

                    # if no winning moves, do random move out of optional ones
                    if len(optional_moves) == 0:
                        pygame.draw.rect(screen, BLACK, (500, 700, 400, 300))
                        optional_moves.append(move)


                    move = random.randrange(0, len(optional_moves))
                    return optional_moves[move]

                pygame.init()

                w = COLS * SQUARE_SIZE
                h = (ROWS + 1) * SQUARE_SIZE
                screen = pygame.display.set_mode((1000, h))
                real_input = True
                while real_input == True:
                # single or two player?

                    ComputerPlay = input('Single Player (Swamp/Fiona Duel) or Two Player (Friendly Shrek vs. Donkey Brawl? S/T')
                    two_player = ComputerPlay.upper() == "T"
                    ComputerPlay = ComputerPlay.upper() == "S"

                # if player chooses two player (Brawl for the Onion Token)
                    real_input = False
                    if two_player:
                        pygame.display.set_caption("Shrek's Connect 4 - Friendly Onion Brawl")
                        screen.blit(real_swampImg, (700, 300))

                # if player chooses single player, it's the swamp/Fiona duel
                    elif ComputerPlay:
                        real_input = False
                        pygame.display.set_caption("Shrek's Connect 4 - Duel for the Swamp (and Fiona)")
                        screen.blit(real_damagedswampImg, (600, 300))
                    else:
                        print('You goofball, you have to type either "S" or "T" for the gamemode')
                        real_input = True

                board = create_board()  # 2D array (matrix)
                print_board(board)
                draw_board(board)
                pygame.display.update()

                # setting fonts
                my_font = pygame.font.SysFont('Comic Sans', 40)
                winning_font = pygame.font.SysFont('Oswald', 40)

                game_over = False
                #global assignment for game_over
                turn = 1
                # starts off with turn 1

                move_was_made = False
                #another assignment for checking later

                while game_over == False:
                    # Just means "while the game is going:"
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                            # if the player wants to quit, refer to the quit event type
                        if event.type == pygame.MOUSEMOTION:
                            pygame.draw.rect(screen, BLACK, (0, 0, w, SQUARE_SIZE))
                            posx = event.pos[0]

                            # print(posx)

                            # This is a piece and turn headline. If turn is 2, it's Donkey's.
                            if turn == 2:
                                pygame.draw.circle(screen, BROWN, (posx, SQUARE_SIZE // 2), RADIUS)
                                screen.blit(real_donkeyfrownImg, (700, 0))
                                label = my_font.render(f"Donkey's Turn", False, BROWN)
                                screen.blit(label, (30, 10))
                            # Now headline and piece color for Shrek
                            else:
                                pygame.draw.circle(screen, GREEN, (posx, SQUARE_SIZE // 2), RADIUS)
                                label = my_font.render(f"Shrek's Turn", False, GREEN)
                                screen.blit(label, (30, 6))
                            pygame.display.update()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            posx = event.pos[0]
                            col = int(posx / SQUARE_SIZE)
                            if col > 6:

                                continue
                            # calling functions for when moves are made--if it's a valid location
                            if is_valid_location(board, col):
                                row = get_next_open_row(board, col)
                                pygame.draw.rect(screen, BLACK, (0, 0, 2000, SQUARE_SIZE))
                                drop_piece(board, row, col, turn)
                                move_was_made = True
                    if turn == 2 and ComputerPlay:

                        screen.blit(real_donkeyfrownImg, (700, 0))

                        label = my_font.render(f"Farquaad Played", False, RED)
                        screen.blit(label, (340, 0))

                        # row, col = AI_make_move_win_one(board, turn)
                        row, col = AI_make_move_win_one_not_lose_two(board, turn)
                        drop_piece(board, row, col, turn)
                        move_was_made = True



                    if turn == 2 and ComputerPlay:
                        pygame.time.wait(1400)
                        screen.blit(real_farquaadImg, (700, 0))
                    elif turn == 2 and not ComputerPlay:
                        screen.blit(real_donkeyfrownImg, (700, 0))
                    elif turn == 1 and ComputerPlay:
                        screen.blit(real_shrekfrownImg, (700, 0))
                    else:
                        screen.blit(real_shreksmileImg, (700, 0))

                    if move_was_made:
                        move_was_made = False

                        if winning_move(board, turn):
                            '''
                            if statement that calls the winning_move function to check if someone
                            connected 4
                            '''

                            # if it was against Farquaad's AI and Shrek won
                            if turn == 1 and ComputerPlay:
                                pygame.display.flip()
                                pygame.time.wait(500)
                                screen.fill((0, 0, 0))
                                screen.blit(real_shrekImg, (700, 0))
                                screen.blit(real_greatswampImg, (0, 0))
                                screen.blit(real_shrekstandingImg, (686, 0))
                                label = winning_font.render(f"SHREK WON BACK THE SWAMP!", False, WHITE)
                                screen.blit(label, (10, 30))
                                label = winning_font.render(f'(and Fiona)', False, WHITE)
                                screen.blit(label, (200, 60))

                            # OR if it was against player 2 (donkey) and Shrek won
                            elif turn == 1 and not ComputerPlay:
                                pygame.display.flip()
                                screen.fill((0, 0, 0))
                                screen.blit(real_dreamworksImg, (0, 0))
                                screen.blit(real_shrekImg, (700, 0))
                                pygame.time.wait(1000)
                                label = my_font.render(f"SHREK WON THE ONION TOKEN!", False, WHITE)
                                screen.blit(label, (20, 10))
                                screen.blit(real_onionImg, (700, 430))
                            # OR if it was Donkey who won against Shrek
                            elif turn == 2 and not ComputerPlay:
                                pygame.display.flip()
                                screen.fill((0, 0, 0))
                                screen.blit(real_dreamworksImg, (0, 0))
                                screen.blit(real_donkeyImg, (700, -20))
                                screen.blit(real_onionImg, (700, 430))
                                label = my_font.render(f"DONKEY WON THE ONION TOKEN!", False, BROWN)
                                screen.blit(label, (-1.8, 10))
                            # And, lastly, if it was Farquaad winning
                            elif turn == 2 and ComputerPlay:
                                pygame.display.flip()
                                screen.fill((0, 0, 0))
                                screen.blit(real_dulaccastleImg, (0, 0))
                                screen.blit(real_triumphantfarquaadImg, (660, 0))
                                label = winning_font.render(f"FARQUAAD SEIZED THE SWAMP (and got Fiona).", False, RED)
                                screen.blit(label, (0, 30))
                                label = winning_font.render(f"YOU LOST!", False, RED)
                                screen.blit(label, (0, 60))
                            '''
                            This set of if/elif/else statements checks who won and broadcasts images/headlines
                            based off that
                            '''
                            game_over = True
                            '''
                            This now sets game_over to the True boolean, which rules out code from the 
                            if game_over == False
                            '''
                        print_board(board)
                        draw_board(board)
                        pygame.display.update()

                        # changing turns
                        if turn == 1:
                            turn = 2
                        else:
                            turn = 1
                    if game_over:
                        pygame.time.wait(10000)
                        sys.exit()
                    '''
                    if the game is over, checked by the winning function, then wait
                    to give the player time to see how he lost/won, then close
                    '''
        # If the player clicks button_2, or the Quit button, the game closes.
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        # The text that goes atop the buttons
        draw_text('PLAY', font2, (255, 255, 255), screen, 420, 180)
        draw_text('QUIT', font2, (255, 255, 255), screen, 420, 325)

        # setting click globally
        click = False

        # This is a safe set of lines to allow the player to close the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)



pygame.display.update()
mainClock.tick(60)


main_menu()




















