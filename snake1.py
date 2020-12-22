import pygame as pg
import random

pg.init()

A = 20
B = 0

red = (225, 0, 0)
green = (0, 225, 0)
blue = (0, 0, 225)
white = (225, 225, 225)
W = 800
H = 600

game_score = 0
speed = 10

surface = pg.display.set_mode((W, H))
pg.display.set_caption("Snake")

f = pg.font.SysFont('arial', 30)
class Head(pg.sprite.Sprite):
        def __init__(self, x, y, filename):
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load(filename)
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.center = (x,  y)
        def update(self, a, b):
            
            self.rect.x += a
            self.rect.y += b
            if self.rect.x +1 <= 0:
                self.rect.x = W  
            elif self.rect.x >= W :
                self.rect.x = 0
            elif self.rect.y +1 <=0:
                self.rect.y = H 
            elif self.rect.y >= H:
                self.rect.y = 0
            
        
class Apple(pg.sprite.Sprite):
    def __init__(self, x, y, filename):
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load(filename)
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.center = (x,  y)

        

class Body(pg.sprite.Sprite):
    def __init__(self, x, y, filename):
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load(filename)
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.center = (x,  y)
    def update(self, a, b):
        if self.rect.x +1 <= 0:
            self.rect.x = W  
        elif self.rect.x >= W :
            self.rect.x = 0
        elif self.rect.y +1 <=0:
            self.rect.y = H 
        elif self.rect.y >= H:
            self.rect.y = 0
        self.rect.x += a
        self.rect.y += b

apple_x = random.randint(1, W // 20) 
if apple_x % 2 != 1 :
    apple_x -= 1
apple_x *= 20
apple_y = random.randint(1, H // 20)
if apple_y % 2 != 1 :
    apple_y -= 1
apple_y *= 20
        
apple = Apple(apple_x, apple_y, "apple.png")
head = Head(30, 30, "head.png")


if __name__ == '__main__':
    while True:
        pg.time.Clock().tick(speed)
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            if A != 0 and B != 20: 
                A = 0
                B = -20

        elif keys[pg.K_RIGHT]:
            if A != -20 and B != 0:
                A = 20
                B = 0

        elif keys[pg.K_LEFT]:
            if A != 20 and B != 0:
                A = -20
                B = 0    

        elif keys[pg.K_DOWN]:
            if A != 0 and B != -20:
                A = 0
                B = 20
        
        if head.rect.x == apple_x and head.rect.y == apple_y:
            game_score +=1
            if game_score % 5 == 0 and game_score != 0:
                speed += 2
            apple_x = random.randint(1, W // 20) 
            if apple_x % 2 != 1 :
                apple_x -= 1
            apple_x *= 20
            apple_y = random.randint(1, H // 20)
            if apple_y % 2 != 1 :
                apple_y -= 1
            apple_y *= 20
        
        surface.fill(green)
        surface.blit(apple.image, (apple_x, apple_y))
        surface.blit(head.image, head.rect)
        sc_text = f.render('Score: ' + str(game_score), 1, white)
        surface.blit(sc_text, (0,0))
        head.update(A, B)

        pg.display.update()