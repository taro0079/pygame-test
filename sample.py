import pygame
import datetime
import signal
import time
from os import listdir
from pygame.locals import *
import sys

pygame.init()
pygame.mouse.set_visible(0)

size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 600))
fps = pygame.time.Clock()
title_font = pygame.font.SysFont("Meiryo", 50)


def update_image(counter, pic_num):
    path = "./images/"
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    list = listdir(path)
    image = pygame.image.load(path + list[pic_num])
    image = pygame.transform.scale(image, (size[0], size[1]))
    screen.blit(image, (0, 0))


def update_time():
    _now = datetime.datetime.now()
    today = _now.strftime("%m / %d")
    nowtime = _now.strftime("%H:%M:%S")
    weelday = _now.strftime("%a")

    time = title_font.render(
        today + " " + nowtime + " (" + weelday + ")", True, (255, 255, 255)
    )
    screen.blit(time, (50, 100))


def update_picnum(pic_num):
    if pic_num == size_image - 1:
        pic_num = 0
    else:
        pic_num += 1

    return pic_num


if __name__ == "__main__":
    counter = 0
    pic_num = 0
    path = "./images/"
    size_image = len(listdir(path))
    last_time = 0
    while True:
        now_time = pygame.time.get_ticks()
        if now_time - last_time > 4000:
            last_time = now_time
            pic_num = update_picnum(pic_num)

        update_image(1, pic_num)
        update_time()
        pygame.display.update()
        fps.tick(1000)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
