import pygame
import datetime
import time
from pygame.locals import *
import sys

pygame.init()
pygame.mouse.set_visible(0)

size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 600))
fps = pygame.time.Clock()
title_font = pygame.font.SysFont("Arial", 50)


def update_time():
    _now = datetime.datetime.now()
    today = _now.strftime("%m / %d")
    nowtime = _now.strftime("%H:%M:%S")
    weelday = _now.strftime("%a")

    time = title_font.render(
        today + " " + nowtime + " (" + weelday + ")", True, (255, 255, 255)
    )
    screen.blit(time, (50, 100))


if __name__ == "__main__":
    while True:
        screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
        update_time()
        pygame.display.update()
        fps.tick(1000)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
