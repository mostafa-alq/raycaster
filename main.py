import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        # lock mouse
        # pg.event.set_grab(True)
        # make movement speed independent of FPS
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    # function to display fps as name of the window
    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        # can be displayed to 1 decimal place if I put ": 1f" inside the brackets but i just like looking at a long number for the fps
        pg.display.set_caption(f'{self.clock.get_fps() :.3f}')

    def draw(self):
        self.screen.fill('black')
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    # main game loop
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
