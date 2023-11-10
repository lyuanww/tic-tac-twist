from ai import Ai
from board import Board
from constants import *
import pygame
from util import Util

class Game:

    def __init__(self, screen):
        self.board = Board()
        self.ai = Ai()
        self.player = 1 # 1 - cross  2 - circle
        self.gamemode = 'ai' #pvp or ai
        self.running = False
        self.show_lines(screen)

    def start(self, screen, gamemode, level):
        self.gamemode = gamemode
        self.board = Board()
        self.ai = Ai()
        if self.gamemode == 'ai':
            self.ai.level = level
        self.running = True
        self.show_lines(screen)
    
    def reset(self, screen):
        current_level = self.ai.level
        self.board = Board()
        self.ai = Ai()
        if self.gamemode == 'ai':
            self.ai.level = current_level
        self.player = 1
        self.running = True
        self.show_lines(screen)

    def resume(self, screen):
        self.show_lines(screen)
        for square_row in range(ROWS):
            for square_col in range(COLS):
                if self.board.squares[square_row][square_col] == 1:
                    # draw cross
                    start_desc = (square_col * SQUARE_SIZE + OFFSET, square_row * SQUARE_SIZE + OFFSET)
                    end_desc = (square_col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, square_row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
                    pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

                    start_asc = (square_col * SQUARE_SIZE + OFFSET, square_row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
                    end_asc = (square_col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, square_row * SQUARE_SIZE + OFFSET)
                    pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
                elif self.board.squares[square_row][square_col] == 2:
                    # draw circle
                    center = (square_col * SQUARE_SIZE + SQUARE_SIZE // 2, square_row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

        self.running = True

    def make_move(self, row, col, screen):
        self.board.mark_square(row, col, self.player)
        self.draw_fig(row, col, screen)
        self.next_turn()

        
    def show_lines(self, screen):
        # bg
        screen.fill(BG_COLOR)
        
        # vertical
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQUARE_SIZE, 0), (WIDTH - SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQUARE_SIZE), (WIDTH, HEIGHT - SQUARE_SIZE), LINE_WIDTH)

    def draw_fig(self, row, col, screen):
    
        if self.player == 1:
            # draw cross
            start_desc = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET)
            end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            start_asc = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        elif self.player == 2:
            # draw circle
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)
    
    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_game_mode(self):
        self.gamemode = 'pvp' if self.gamemode == 'ai' else 'ai'

    def is_over(self, screen):
        return self.board.final_state(screen, show=True) != 0 or self.board.is_full()
    
    def pause(self):
        self.running = False

 


        