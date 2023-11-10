from enum import Enum
import sys
import pygame
from constants import *
from game import Game
from util import Util
from button import Button
import os

# PYGAME SETUP
pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)


# GAME ENUMS
class GameState(Enum):
    MAIN = 1
    PAUSED = 2
    RUNNING = 3
    SETTINGS = 4
    HELP = 5

current_state = GameState.MAIN
clicked = False

# Load button images
resume_img = pygame.image.load(Util.resource_path('Resume.png')).convert_alpha()
settings_img = pygame.image.load(Util.resource_path('Settings.png')).convert_alpha()
exit_img = pygame.image.load(Util.resource_path('Exit.png')).convert_alpha()
smart_ai_img = pygame.image.load(Util.resource_path('SmartAI.png')).convert_alpha()
random_ai_img = pygame.image.load(Util.resource_path('RandomAI.png')).convert_alpha()
pvp_img = pygame.image.load(Util.resource_path('PVP.png')).convert_alpha()
help_img = pygame.image.load(Util.resource_path('Help.png')).convert_alpha()
main_menu_img = pygame.image.load(Util.resource_path('MainMenu.png')).convert_alpha()

# Main menu buttons
smart_ai_button = Button(143 , 100, smart_ai_img, 0.4)
random_ai_button = Button(130 , 200, random_ai_img, 0.4)
pvp_button = Button(150 , 300, pvp_img, 0.4)
help_button = Button(150 , 400, help_img, 0.4)
mm_exit_button = Button(150 , 500, exit_img, 0.4)

# Settings buttons
main_menu_button = Button(120, 500, main_menu_img, 0.5)

# Pause menu buttons
resume_button = Button(120 , 150, resume_img, 0.5)
exit_button = Button(120 , 300, exit_img, 0.5)
pm_main_menu_button = Button(120 , 450, main_menu_img, 0.5)



def main():
    global current_state
    global clicked
    game = Game(screen)


    while True:
        if current_state == GameState.PAUSED:
            screen.fill(BG_COLOR)
            if not clicked:
                if resume_button.draw(screen):
                    current_state = GameState.RUNNING
                    clicked = True
                    game.resume(screen)
                # elif settings_button.draw(screen):
                #     current_state = GameState.SETTINGS
                #     clicked = True
                elif pm_main_menu_button.draw(screen):
                    current_state = GameState.MAIN
                    clicked = True

                elif exit_button.draw(screen):
                    pygame.quit()
                    sys.exit()

        if current_state == GameState.SETTINGS:
            screen.fill(BG_COLOR)

            if main_menu_button.draw(screen):
                current_state = GameState.MAIN
                

        if current_state == GameState.MAIN:
            screen.fill(BG_COLOR)
            pygame.draw.rect(screen, RECT_COLOR, (0,80, WIDTH, HEIGHT))
            
            Util.draw_text(screen, FONT, 'Tic Tac Twist', (73, 10))
            if not clicked:
                if smart_ai_button.draw(screen):
                    
                    current_state = GameState.RUNNING
                    game.start(screen, 'ai', 1)
                    clicked=True

                elif random_ai_button.draw(screen):
                    current_state = GameState.RUNNING
                    game.start(screen, 'ai', 0)
                    clicked=True

                elif pvp_button.draw(screen):
                    current_state = GameState.RUNNING
                    game.start(screen, 'pvp', 0)
                    clicked=True

                # elif mm_settings_button.draw(screen):
                #     current_state = GameState.SETTINGS
                #     clicked=True

                elif help_button.draw(screen):
                    current_state = GameState.HELP
                    clicked=True

                elif mm_exit_button.draw(screen):
                    pygame.quit()
                    sys.exit()

        if current_state == GameState.HELP:
        
            screen.fill(BG_COLOR)

            Util.draw_small_text(screen, FONT, 'Space during game - Pause menu', (50, 200))
            Util.draw_small_text(screen, FONT, 'Space after game - Restart', (50, 250))

            if main_menu_button.draw(screen):
                if not clicked:
                    current_state = GameState.MAIN
                    clicked = True
       
        
            
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False

            if event.type == pygame.KEYDOWN:
                # space - pause
                if event.key == pygame.K_SPACE:
                    if current_state == GameState.RUNNING:
                        if game.running:
                            game.pause()
                            current_state = GameState.PAUSED
                        else:
                            game.reset(screen)

       

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE 

                if game.board.empty_square(row, col) and game.running:
                    game.make_move(row, col, screen)

                    if game.is_over(screen):
                        game.running = False
                       
                    

        if game.gamemode == 'ai' and game.player == game.ai.player and game.running:
            # update the screen
            pygame.display.update()

            # ai methods
            row, col = game.ai.eval(game.board)

            game.make_move(row, col, screen)

            if game.is_over(screen):
                game.running = False
                

        pygame.display.update()



main()