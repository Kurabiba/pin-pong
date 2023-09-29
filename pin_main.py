from pygame import *



FPS = 60
clock = time.Clock()
setWinn = [700, 500]
window = display.set_mode(setWinn)
display.set_caption("Пинг понг")
#background = transform.scale(image.load("galaxy.jpg"), (setWinn))

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)




