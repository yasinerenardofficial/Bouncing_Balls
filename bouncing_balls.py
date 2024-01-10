import pygame, sys, random
from pygame.locals import QUIT

pygame.init()
screenwidth, screenheight = 1440,800
DISPLAYSURF = pygame.display.set_mode((screenwidth, screenheight/2))
pygame.display.set_caption('Hello World!')
timer = pygame.time.Clock()

class bouncing_ball():
    all = []
    def __init__(self):
        bouncing_ball.all.append(self)
        self.x = screenwidth/2
        self.y = 11
        self.x_speed = 0
        self.y_speed = random.randint(1 , 10)
        self.radius = 10
        self.color = (random.randint(50 , 200),random.randint(50 , 200),random.randint(50 , 200))

    def draw(self):
        pygame.draw.circle(DISPLAYSURF,self.color, (self.x, self.y), self.radius)
        self.y += self.y_speed
        if self.y < 10 :
          self.y_speed *= -1
        if self.y > screenheight-10 :
          self.y_speed *= -1
          create_new_ball()
  
def create_new_ball():
    ball = bouncing_ball()
    ball.x = random.randint(10 , screenheight-10)
    
def draw_all_from(a):
    for _ in a:
        _.draw()    
      
ball1 = bouncing_ball()
drawables = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                bouncing_ball.all = []
        

    pygame.display.set_caption(f'press R to reset   Balls: {len(bouncing_ball.all)}')
    timer.tick(60)
    DISPLAYSURF.fill("black")
    draw_all_from(bouncing_ball.all)
    ball1.draw()
    pygame.display.update()