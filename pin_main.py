from pygame import *
from random import *



class GameSprate(sprite.Sprite):
    def __init__(self, image_l, speed, x_p, y_p, x_ast, y_ast, speedx, speedy):
        super().__init__()
        self.image  = transform.scale(image.load(image_l), (x_ast, y_ast))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_p
        self.rect.y = y_p  
        self.speedx = speedx
        self.speedy = speedy 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprate):
    def __init__(self, image_l, speed, x_p, y_p, x_ast, y_ast, speedx, speedy):
        super().__init__(image_l, speed, x_p, y_p, x_ast, y_ast,  speedx, speedy)
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500-75 :
            self.rect.y += self.speed

    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500-75 :
            self.rect.y += self.speed

class Enemy(GameSprate):
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx 

        if self.rect.y > 460:
            self.speedy *= -1
        if self.rect.y < 40:
            self.speedy *= -1
        if self.rect.x < 20 or self.rect.x > 680:
            global end 
            end = False 
        if sprite.collide_rect(self, rocketL) or sprite.collide_rect(self, rocketR):
            self.speedx *= -1

FPS = 60
clock = time.Clock()
setWinn = [700, 500]
window = display.set_mode(setWinn)
display.set_caption("Пинг понг")
background = transform.scale(image.load("galaxy.jpg"), (setWinn))

ball = Enemy("ball.png", 3, 300, 250, 35, 35, 3, 3)
rocketL = Player("racket.png", 10, 30, 200, 65, 65, 3, 3)
rocketR = Player("racket.png", 10, 600, 200, 65, 65, 3, 3)

game = True
end = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if end:
        window.blit(background, (0, 0))
        rocketL.updateL()
        ball.update()
        rocketR.updateR()
        rocketL.reset()
        rocketR.reset()
        ball.reset()
        

        display.update()
        clock.tick(FPS)