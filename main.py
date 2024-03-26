# This file was created by: Owen Pence
# Works cited: Chris Cozort & OpenAi
# chat.openai.com
# https://github.com/ccozort


import pygame as pg
from settings import *
from sprites import *
import sys
from random import randint
from os import path
import pygame
import os 
import sys

 
# game class 
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Pencys Game! ') # name of game
        self.clock = pg.time.Clock()
        self.load_data()
        self.start_time = pg.time.get_ticks()  # time intilization
        self.time_limit = 20  # timer countdown - seconds
    
        # MUSIC 
        # sources; Chapt GPT- Open Ai
        # Question- how do I add music file to pygame
        music_file = "bestmates.mp3.mp3"  # music file name
        pg.mixer.music.load(os.path.join("music", music_file)) # music folder 
        # music loop (until timer runs out) 
        pg.mixer.music.play(-1)  
    
    
    # load data with map.txt file
    # map.txt file configures map
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []

        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
                print(self.map_data)
    
    # tiles and their location 4       
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.Negative = pg.sprite.Group()
        # sprites for walls, coins, negatives
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                # location of wall 
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                # location of Player
                if tile == 'P':
                    self.player = Player(self, col, row)
                # location of Coin
                if tile == 'C':
                    Coin(self, col, row)
                # location of Negative
                if tile == 'N':
                    Negative(self, col, row)
    # game run
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # frame rate of game
            # game input
            self.events()
            # game processing
            self.update()
            # game output
            self.draw()
    # game quit
    def quit(self):
        pg.quit()
        sys.exit()
    # methods
    def input(self): 
        pass
    def update(self):
        self.all_sprites.update()
    
    
    # grid of the game 
    # pygame map H/W
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, GREEN, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, GREEN, (0, y), (WIDTH, y))
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('Times new roman')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, BLUE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)
    # drawing of score board (top left corner)
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1) # location
        pg.display.flip()
    
    

    
    def events(self):
            # events list
            for event in pg.event.get():
                # how to quit game - via X in the top right corner
                if event.type == pg.QUIT:
                    self.quit()
                    print("game over!")
                # keyboard events
                # W = up
                # D - right
                # S - Down
                # A - Left
            
    # start screen
    def show_start_screen(self):
        pass
    # end screen
    def show_go_screen(self):
        pass

g = Game()
# g.show_go_screen()
# game run
while True:
    g.new()
    g.run()
    # g.show_go_screen()

