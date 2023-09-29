from pygame import *



class GameSprate(sprite.Sprite):
    def __init__(self, image_l, speed, x_p, y_p, x_ast, y_ast):
        super().__init__()
        self.image  = transform.scale(image.load(image_l), (x_ast, y_ast))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_p
        self.rect.y = y_p   
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprate):
    def __init__(self, image_l, speed, x_p, y_p, x_ast, y_ast):
        super().__init__(image_l, speed, x_p, y_p, x_ast, y_ast)
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



FPS = 60
clock = time.Clock()
setWinn = [700, 500]
window = display.set_mode(setWinn)
display.set_caption("Пинг понг")
background = transform.scale(image.load("galaxy.jpg"), (setWinn))


rocketL = Player("racket.png", 10, 30, 200, 65, 65)
rocketR = Player("racket.png", 10, 600, 200, 65, 65)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    rocketL.updateL()
    rocketR.updateR()
    rocketL.reset()
    rocketR.reset()
    

    display.update()
    clock.tick(FPS)


