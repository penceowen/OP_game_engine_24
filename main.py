# This file was created by: Owen Pence
# Works cited: Chris Cozort & OpenAi

# 
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
        pg.display.set_caption('Pencys Game! ')
        self.clock = pg.time.Clock()
        self.load_data()
        self.start_time = pg.time.get_ticks()  # Start time initialization
        self.time_limit = 20  # Countdown timer limit in seconds
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
        # clock display
        time_left = max(0, self.time_limit - (pg.time.get_ticks() - self.start_time) // 1000)  # Timer calculation
        self.draw_clock(self.screen, time_left, BLUE, WIDTH // 20, 40, 20)  # clock drawing
        pg.display.flip()
    def check_time(self):
        # once time runs out the game resets
        if pg.time.get_ticks() - self.start_time >= self.time_limit * 1000:  
            print("Time's up! Resetting game...")
            self.new()  # Restart the game
            self.start_time = pg.time.get_ticks()  # Reset the timer

        # MUSIC 
        music_file = "bestmates.mp3.mp3"  # music file name
        pg.mixer.music.load(os.path.join("music", music_file)) # music folder 

        # music loop
        # music loops until timer runs out 
        pg.mixer.music.play(-1)  
    

    



    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []

        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
                print(self.map_data)
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
                # Tile location of wall
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                # Tile location of Player
                if tile == 'P':
                    self.player = Player(self, col, row)
                # Tile location of Coin
                if tile == 'C':
                    Coin(self, col, row)
                # Tile location of Negative
                if tile == 'N':
                    Negative(self, col, row)
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            # this is input
            self.events()
            # this is processing
            self.update()
            # this output
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()
    # methods
    def input(self): 
        pass
    def update(self):
        self.all_sprites.update()
    
    
    # Grid drawn for the game
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
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
        pg.display.flip()
     

    def events(self):
            # listening for events
            for event in pg.event.get():
                # when you hit the red x the window closes the game ends
                if event.type == pg.QUIT:
                    self.quit()
                    print("the game has ended..")
                # keyboard events
                # W = up
                # D - right
                # S - Down
                # A - Left
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
# g.show_go_screen()
while True:
    g.new()
    g.run()
    # g.show_go_screen()

