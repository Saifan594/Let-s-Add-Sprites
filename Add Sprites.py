print("\033c")

import random
import pygame

pygame.init()

red = pygame.Color("red")
green = pygame.Color("green")
blue = pygame.Color("blue")

cyan = pygame.Color("cyan")
magenta = pygame.Color("magenta")
yellow = pygame.Color("yellow")

display_color = random.choice((cyan, magenta, yellow))
display_title = "Add Sprites"
display_size = (750, 500)
display = pygame.display.set_mode(display_size)

sprite_color_change = pygame.USEREVENT + 1
background_color_change = pygame.USEREVENT + 2

clock_framerate = 200
clock = pygame.time.Clock()

running = True

sprite_list = pygame.sprite.Group()

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((random.choice((50, 75)), random.choice((50, 75))))
        self.image.fill(random.choice((red, green, blue)))
        self.rect = self.image.get_rect()
        self.velocity = [random.choice((-1, 1)), random.choice((-1, 1))]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        touching_edge = False
        
        if self.rect.left <= 0 or self.rect.right >= display_size[0]:
            self.velocity[0] = -self.velocity[0]
            touching_edge = True
        
        if self.rect.top <= 0 or self.rect.bottom >= display_size[1]:
            self.velocity[1] = -self.velocity[1]
            touching_edge = True
        
        if touching_edge:
            pygame.event.post(pygame.event.Event(sprite_color_change))
            pygame.event.post(pygame.event.Event(background_color_change))
    
    def change_sprite_color(self):
        self.image.fill(random.choice((red, green, blue)))

def change_background_color():
    global display_color
    display_color = random.choice((cyan, magenta, yellow))

sprite1 = Sprite()
sprite1.rect.x = random.randint(0, display_size[0] - 100)
sprite1.rect.y = random.randint(0, display_size[1] - 100)
sprite_list.add(sprite1)

sprite2 = Sprite()
sprite2.rect.x = random.randint(0, display_size[0] - 100)
sprite2.rect.y = random.randint(0, display_size[1] - 100)
sprite_list.add(sprite2)

sprite3 = Sprite()
sprite3.rect.x = random.randint(0, display_size[0] - 100)
sprite3.rect.y = random.randint(0, display_size[1] - 100)
sprite_list.add(sprite3)

display.fill(display_color)
pygame.display.set_caption(display_title)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == sprite_color_change:
            sprite1.change_sprite_color()
            sprite2.change_sprite_color()
            sprite3.change_sprite_color()
        
        if event.type == background_color_change:
            change_background_color()
    
    display.fill(display_color)
    
    sprite_list.update()
    sprite_list.draw(display)
    
    pygame.display.flip()
    clock.tick(clock_framerate)

pygame.quit()