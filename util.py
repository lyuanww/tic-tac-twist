import os
import sys
import pygame
from constants import *


class Util:

    @staticmethod
    def draw_text(screen, font, text, pos):
        font = pygame.font.SysFont(FONT, FONT_SIZE)
        text = font.render(text, True, FONT_COLOR)
        screen.blit(text, pos)

    @staticmethod
    def draw_small_text(screen, font, text, pos):
        font = pygame.font.SysFont(FONT, SMALL_FONT_SIZE)
        text = font.render(text, True, FONT_COLOR)
        screen.blit(text, pos)

    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)