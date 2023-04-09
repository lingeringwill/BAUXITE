import pygame, os, time, random
from pygame import mixer
import math

pygame.init()
pygame.font.init()

#Display window with set width and height
s_width = 1000
s_height = 700
screen = pygame.display.set_mode((s_width, s_height))


pygame.display.set_caption("Stop The Asteroids!")

# Road Object images
grandma = pygame.transform.scale(pygame.image.load("grandma.png").convert_alpha(), (75,75))
cardboard_box = pygame.transform.scale(pygame.image.load("box.png").convert_alpha(), (75,75))
dog = pygame.transform.scale(pygame.image.load("puppy.png").convert_alpha(), (75,75))
bottle = pygame.transform.scale(pygame.image.load("bottle.png").convert_alpha(), (75,75))
newspaper = pygame.transform.scale(pygame.image.load("newspaper.png").convert_alpha(), (75,75))

# User Character
trash_truck = pygame.transform.scale(pygame.image.load("trashTruck.png"), (180,120)).convert_alpha()

# Background
backg_img = pygame.transform.scale(pygame.image.load("retro-background.png"), (s_width, s_height))


class RoadObject:
    def __init__(self, x, y, img, name):
        self.name = name
        self.x=x
        self.y=y
        self.img=img
        self.mask=pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.x -= vel

    def off_screen(self, width):
        return not(self.x <= width and self.x>=0)

    def collision(self, obj):
        return collide(obj, self)
    
    def get_height(self):
        return self.img.get_height()
    
    def get_width(self):
        return self.img.get_width()


class Truck:
    def __init__(self,x,y,health=100):
        self.x=x
        self.y=y
        self.health=health
        self.tuck_img = trash_truck

    def draw(self, window):
        window.blit(self.tuck_img, (self.x, self.y))

    def get_width(self):
        return self.tuck_img.get_width()

    def get_height(self):
        return self.tuck_img.get_height()


class Player(Truck):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.truck_img = trash_truck
        self.mask = pygame.mask.from_surface(self.truck_img)
        self.max_health = health

        def draw(self, screen):
            super().draw(screen)
            self.healthbar(screen)

        def healthbar(self, screen):
            pygame.draw.rect(screen, (255,0,0), (self.x, self.y + self.truck_img.get_height()+10, self.truck_img.get_width(), 10))
            pygame.draw.rect(screen, (0,255,0), (self.x, self.y + self.truck_img.get_height()+10, self.truck_img.get_width() * (self.health/self.max_health), 10))


# Sound
#mixer.music.load('Arcane_Battle.ogg.mp3')
#mixer.music.play(-1)

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    #game loop
    running = True
    FPS = 60
    clock = pygame.time.Clock()

    level = 0
    lives = 10
    main_font = pygame.font.SysFont("arial", 20)
    lost_font = pygame.font.SysFont("arial", 30)

    player = Player(55,350)
    player_vel = 5
    laser_vel = 8

    enemies = []
    wave_length = 5

    lost = False
    lost_count = 0

    def redraw_window():
        #Draw background image
        screen.blit(backg_img, (0,0))
        #Draw lives and level labels
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        screen.blit(lives_label, (880, 8))
        screen.blit(level_label, (880, 35))
        
        for enemy in enemies:
            enemy.draw(screen)

            #draw main player
        player.draw(screen)

        if lost:
            lost_label = lost_font.render("You Have Lost. Earth Cannot Take So Many Asteroids", 1, (255,255,255))
            screen.blit(lost_label, (s_width/2 - lost_label.get_width()/2, 350))

        pygame.display.update()


    while running:
        clock.tick(FPS)

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

            if lost_count > FPS*5:
                running = False
            else:
                redraw_window()
                continue

        if len(enemies) ==0:
            level+=1
            wave_length += 3
            num_avoid = math.floor(wave_length / 2)
            for i in range(wave_length):
                if num_avoid > 0:
                    enemy = RoadObject(random.randrange(1200, 2000), random.randrange(100, s_height-100), random.choice([grandma, dog]), 'bad')
                    num_avoid -= 1
                else:
                    enemy = RoadObject(random.randrange(1200, 2000), random.randrange(100, s_height-100), random.choice([cardboard_box, bottle, newspaper]), 'good')
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        #if keys[pygame.K_LEFT] and player.x - player_vel > 0:
        #    player.x -= player_vel
        #if keys[pygame.K_RIGHT] and player.x + player_vel+player.get_width() < s_width:
        #    player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel+player.get_height() < s_height:
            player.y += player_vel

        for enemy in enemies[:]:
            enemy.move(0.8)
            if collide(enemy, player):
                if enemy.name == 'bad':
                    lives -= 1
                enemies.remove(enemy)
            elif enemy.x + enemy.get_width() < 25:
                if enemy.name == 'good':
                    lives -= 1
                enemies.remove(enemy)

        redraw_window()

def main_menu():
    title_font = pygame.font.SysFont("arial", 70)
    run = True
    while run:
        screen.blit(backg_img, (0,0))
        title_label = title_font.render("Press the Mouse to Start", 1, (255, 255, 255))
        screen.blit(title_label, (s_width/2 - title_label.get_width()/2, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()
