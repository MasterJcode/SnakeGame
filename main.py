import pygame
import random
pygame.init()

#Grid Screen Setup
cell_number = 50
cell_size = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number*cell_size))
last = pygame.Vector2(0,0)

#SetUp for fruit
class Fruit: 
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = pygame.Vector2(self.x,self.y)

    def drawFruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen,(0,255,0),fruit_rect)

    def randomMize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = pygame.Vector2(self.x,self.y)
        

#SetUp for snake
movement = "left"
class Snake:
    def __init__(self):
        self.body = [pygame.Vector2(5,10),pygame.Vector2(6,10),pygame.Vector2(7,10)]
    def drawSnake(self):
        for item in self.body:
            body_rect = pygame.Rect(int(item.x * cell_size), int(item.y * cell_size),cell_size,cell_size)
            pygame.draw.rect(screen,(0,102,0),body_rect)
    def moveLeft(self):   
        global last     
        tmp = self.body[0].copy()
        self.body[0] += pygame.Vector2(-1,0)
        for i in range(1,len(self.body)):
            tmp1 = self.body[i]
            self.body[i] = tmp
            tmp = tmp1 
        last = tmp  
    def moveRight(self):
        global last
        tmp = self.body[0].copy()
        self.body[0] += pygame.Vector2(1,0)
        for i in range(1,len(self.body)):
            tmp1 = self.body[i]
            self.body[i] = tmp
            tmp = tmp1
        last = tmp
    def moveUp(self):
        global last
        tmp = self.body[0].copy()
        self.body[0] -= pygame.Vector2(0,1)
        for i in range(1,len(self.body)):
            tmp1 = self.body[i]
            self.body[i] = tmp
            tmp = tmp1
        last = tmp
    def moveDown(self):
        global last
        tmp = self.body[0].copy()
        self.body[0] += pygame.Vector2(0,1)
        for i in range(1,len(self.body)):
            tmp1 = self.body[i]
            self.body[i] = tmp
            tmp = tmp1
        last = tmp
    def isDead(self):
        if self.body[0].x > cell_size*(cell_number - 1) or self.body[0].x < 0 or self.body[0].y > cell_size*(cell_number - 1) or self.body[0].y < 0:
            return True
        for i in range(1,len(self.body)):
            if self.body[0] == self.body[i]:
                print(self.body[0],self.body[i])
                return True
        return False

########################
###   MAIN PROGRAM  ####
fruit = Fruit()
snake = Snake()
#Creating FPS
clock = pygame.time.Clock()
FPS = 10
flag = False
running = True

### Game Over ###
font = pygame.font.Font("freesansbold.ttf",64)
gameOverText = font.render("Game Over",True,(255,255,255))

while running:
    clock.tick(FPS)
    screen.fill((153,255,153))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and movement != "right":
                movement = "left"
            elif event.key == pygame.K_RIGHT and movement != "left":
                movement = "right"
            elif event.key == pygame.K_UP and movement != "down":
                movement = "up"
            elif event.key == pygame.K_DOWN and movement != "up":
                movement = "down"
    
    if movement == "right":
        snake.moveRight()
    if movement == "left":
        snake.moveLeft()
    if movement == "up":
        snake.moveUp()
    if movement == "down":
        snake.moveDown()
    if snake.body[0] == fruit.pos: 
        snake.body.append(last)
        fruit.randomMize()
        
    if snake.isDead() == True:
        flag = True
    if flag == False:
        fruit.drawFruit()
        snake.drawSnake()
    else:
        screen.blit(gameOverText,(cell_size*5,cell_size*10))
        
    pygame.display.update()
    