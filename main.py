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
import sys




# game class 
class Game:
    # behold the methods...
    def __init__(self):
        pg.init()
        # Display
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # Name of game
        pg.display.set_caption("Pency's Game!")
        # Timer clock countdown
        self.load_data()
        WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer Example")

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Timer variables
start_time = pygame.time.get_ticks()  # Get the initial time in milliseconds
timer_duration = 60 * 1000  # Timer duration in milliseconds (1 minute in this case)

# Main loop
while True:
    screen.fill(WHITE)
    
    #elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    
    # remaining time
    remaining_time = max(0, timer_duration - elapsed_time)
    seconds = remaining_time // 20

    
    # Display timer
    timer_text = f"{seconds:02}"
    timer_render = font.render(timer_text, True, BLACK)
    timer_rect = timer_render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(timer_render, timer_rect)
    
    # Update the display
    pg.display.flip()
    
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # when time is up
    if elapsed_time >= timer_duration:
        # Game Over!
        print("Game Over!")
        break

    #  frame rate
    pg.time.delay(100)  

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
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

