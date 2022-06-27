import pygame
import sys
import random

from snake import DOWN, GRID_HEIGHT, GRID_WIDTH, GRIDSIZE, LEFT, RIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, UP

# player character
class SNAKE(object):
    def __init__(self):
        """this initializes the snake"""
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random. choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)

    def get_head_position(self):
        """this updates your head location"""
        return self.positions[0]

    def turn(self, point):
        """this allows you to turn"""
        if self.length > 1 and (point[0] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        """this makes you move even when not pressing anything"""
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x* GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert[0, new]
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        """this makes your position and length go back to their initial states when you die"""
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        """ draws the snake"""
        for p in self.positions:
            r = pygame.rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228),r,1)

    def handle_input(self):
        """ makes movement with arrow keys function and exiting the game by hittinh the exit button"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


# the concept of food
class FOOD (object):
    def __init__(self):
        """initializes the food"""
        self.position = [0, 0]
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        "puts the foood in a random location on the grid"
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

class grid(object):
    def drawGrid(surface):
        """draws the grid pattern in the game"""
        for y in range(0, int(GRID_HEIGHT)):
            for x in range(0, int(GRID_WIDTH)):
                if (x + y) % 2 == 0:
                    r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                    pygame.draw.rect(surface, (93, 216, 228), r)
                else:
                    rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                    pygame.draw.rect(surface, (84, 194, 205), rr)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    """main game loop"""
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    grid.drawGrid(surface)

    snake = snake()
    food = food()

    score = 0
    while (True):
        clock.tick(10)
        #handle events
        screen.blit(surface, (0, 0))
        pygame.display.update()


main()