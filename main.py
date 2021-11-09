import pygame
import random

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 0)

class Life(object):
    def __init__(self, screen):
        _, _, self.width, self.height = screen.get_rect()
        self.screen = screen
        self.firstTime = True
    
    def clear(self):
        self.screen.fill((0, 0, 0))

    def pixel(self, x, y, color = WHITE):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_screen = pygame.surfarray.array2d(self.screen)

    def initialPoints(self):
        for i in range(0, 1000):
            self.pixel(random.randint(0, 500), random.randint(0, 500))

    def blinker(self):
        for i in range(0, 150):
            initialPointX = random.randint(0, 500)
            initialPointY = random.randint(0, 500)
            self.pixel(initialPointX, initialPointY)
            self.pixel(initialPointX, initialPointY-1)
            self.pixel(initialPointX, initialPointY-2)

    def toad(self):
        for i in range(0, 150):
            initialPointX = random.randint(0, 500)
            initialPointY = random.randint(0, 500)
            self.pixel(initialPointX, initialPointY)
            self.pixel(initialPointX+1, initialPointY)
            self.pixel(initialPointX+2, initialPointY)
            self.pixel(initialPointX-1, initialPointY-1)
            self.pixel(initialPointX, initialPointY-1)
            self.pixel(initialPointX+1, initialPointY-1)
            self.pixel(initialPointX+2, initialPointY-1)

    def pentaDecathlon(self):
        for i in range(0, 100):
            initialPointX = random.randint(0, 500)
            initialPointY = random.randint(0, 500)

            self.pixel(initialPointX, initialPointY)
            self.pixel(initialPointX-1, initialPointY)
            self.pixel(initialPointX+1, initialPointY)

            self.pixel(initialPointX-1, initialPointY-1)
            self.pixel(initialPointX+1, initialPointY-1)

            self.pixel(initialPointX, initialPointY-2)
            self.pixel(initialPointX-1, initialPointY-2)
            self.pixel(initialPointX+1, initialPointY-2)

            self.pixel(initialPointX, initialPointY-3)
            self.pixel(initialPointX-1, initialPointY-3)
            self.pixel(initialPointX+1, initialPointY-3)

            self.pixel(initialPointX, initialPointY-4)
            self.pixel(initialPointX-1, initialPointY-4)
            self.pixel(initialPointX+1, initialPointY-4)

            self.pixel(initialPointX, initialPointY-5)
            self.pixel(initialPointX-1, initialPointY-5)
            self.pixel(initialPointX+1, initialPointY-5)

            self.pixel(initialPointX+1, initialPointY-6)
            self.pixel(initialPointX+1, initialPointY-6)

            self.pixel(initialPointX, initialPointY-7)
            self.pixel(initialPointX-1, initialPointY-7)
            self.pixel(initialPointX+1, initialPointY-7)

    def render(self):
        if self.firstTime:
            self.blinker()
            self.toad()
            self.pentaDecathlon()
            self.firstTime = False
        else:
            
            for i in range(0, self.width):
                for j in range(0, self.height):
                    neighborCount = 0
                    try:
                        if self.prev_screen[i+1][j] == 16777215:
                            neighborCount+=1
                        if self.prev_screen[i-1][j] == 16777215:
                            neighborCount+=1
                        if self.prev_screen[i][j+1] == 16777215:
                            neighborCount+=1
                        if self.prev_screen[i][j-1] == 16777215:
                            neighborCount+=1
                        if self.prev_screen[i-1][j+1] == 16777215:
                            neighborCount+=1
                        if self.prev_screen[i+1][j+1] == 16777215:
                            neighborCount+=1
                        if self.prev_screen[i-1][j-1] == 16777215:
                            neighborCount+=1
                        if self.prev_screen[i+1][j-1] == 16777215:
                            neighborCount+=1
                        if self.prev_screen[i][j] == 16777215:   
                            if neighborCount < 2:
                                self.pixel(i, j, BLACK)
                            if neighborCount == 2 or neighborCount == 3:
                                self.pixel(i, j, WHITE)
                            if neighborCount > 3:
                                self.pixel(i, j, BLACK)                            
                        else:
                            if neighborCount == 3:
                                self.pixel(i, j)
                    except Exception as e:
                        pass

pygame.init()
screen = pygame.display.set_mode((500, 500), pygame.HWSURFACE | pygame.DOUBLEBUF)

r = Life(screen)

while True:
    pygame.event.pump()
    r.copy()
    r.render()

    pygame.display.flip()