#Feel free to use parts of the code below in your final project!

#The code below is for generating map5 as seen in the Maps folder in the Final Project Scaffold. You can edit it to your own liking!
purple = (160, 32, 240)
navy = (0, 47, 108)
black = (0,0,0)
import pygame, sys, os
from pygame.locals import *
import time
# import mixer
import random

player_hit_points = 3
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 750))
screen_width = 1000
screen_height = 750
pygame.display.set_caption('Final Project Scaffold')

tile_size = (25, 25)


# BACKGROUND = pygame.image.load('background.png').convert_alpha()
# BACKGROUND.blit(BACKGROUND, (900, 500))
# BACKGROUND = pygame.transform.scale(BACKGROUND, (800, 600))
class Enemy:

    def __init__(self,
                 x, 
                 y,
                 img,
                 width,
                 height,
                 pace_limit=20,
                 enemy_type='goblin',
                 health_points=1):
        # super().__init__(x,y,img, width, height)
        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.enemy_type = enemy_type
        if self.enemy_type == 'goblin':
            self.health_points = 1

        elif self.enemy_type == 'boss':
            self.health_points = 5

        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)

    def move(self, move_steps):
        self.rect.move_ip(move_steps)

    def draw(self, window):
        # if self.rect.x in range(0, window.get_width()) and self.rect.y in range(0, window.get_height()):
        window.blit(self.img, (self.rect.x, self.rect.y))


# PLAYER_rect.center = PLAYER.get_rect()

# load in the images for the other tiles


def load_map(path):
    '''Function to load the map file and split it into list.

    Inputs:
    path: the folder where the map is stored

    Outputs:
    game_map: the map on the screen
    
    '''
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


def collision_test(rect, tiles):
    '''
    Function to test if one rect collides with another.

    Inputs:
    rect: an objects rectangle that is going to be checked for collision
    tiles: a set of images used to make the map that is being checked for collison

    Outputs:
    hit_list: a list of tiles an object collides with
    
    '''

    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def enemy_collision(e, enemies, room, Sword_rect):
    try:
        if enemies[room][e][0].rect.colliderect(Sword_rect):
            # remove the enemy from the window
            enemies[room].remove(enemies[room][e])
    except:
        if e > len(enemies[room]):
            e = len(enemies[room] - 1)
            if enemies[room][e][0].rect.colliderect(Sword_rect):
                enemies[room].remove(enemies[room][e])

            return e

    return e


# movement function (up, down, left, right)
def move(rect, movement, tiles):
    '''
    Function that allows characters to falling through the ground.

    Inputs:
    rect: the rectangle of the player
    movement: a list of movements for the player
    tiles: a set of images used to make the map that is being checked for collison

    Outputs:
    rect: the rect of the player
    collision_types: what the player rect collides with
    
    '''
    collision_types = {
        'top': False,
        'bottom': False,
        'right': False,
        'left': False
    }
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True

    return rect, collision_types


star_collision = []
#Loads map file
def switch_map(room):
    if room == 0:
        room += 1

        PLAYER_rect = pygame.Rect(200, 200, 25, 25)
        Sword_rect = pygame.Rect(225, 205, 20, 25)
    elif room == 1:
        room += 1

        PLAYER_rect = pygame.Rect(950, 700, 25, 25)
        Sword_rect = pygame.Rect(975, 705, 20, 25)
    elif room == 2:
        room += 1
        PLAYER_rect = pygame.Rect(300, 90, 25, 25)
        Sword_rect = pygame.Rect(325, 95, 20, 25)
        # the new rectangle will be dependent on the map
    else:
        room += 1
        PLAYER_rect = pygame.Rect(300, 100, 25, 25)
        Sword_rect = pygame.Rect(325, 105, 20, 25)

    return room, PLAYER_rect, Sword_rect
# load_map('Maps/map2')
#Opens the map as listed in maps.txt in the Maps folder.

#Subtracts hitpoints
def hitpoints(player_hit_points):
    if player_hit_points == 3:
        player_hit_points -= 1

    if player_hit_points == 2:
        player_hit_points -= 1

    if player_hit_points == 1:
        player_hit_points -= 1

        print("GAME OVER")
        # white = (255, 255, 255)
        red = (255, 0, 0)
        game_over = font.render('GAME OVER', red, True)
        screen.blit(game_over, (450, 375))
    if room == 0:
        room += 1

        PLAYER_rect = pygame.Rect(200, 200, 25, 25)
        Sword_rect = pygame.Rect(225, 205, 20, 25)

    return player_hit_points








sword = pygame.image.load(
    'Game_Assets/Miscellaneous/sword.png').convert_alpha()
sword = pygame.transform.scale(sword, (25, 25))
Sword_rect = pygame.Rect(145, 120, 20, 25)

player_hit_points = 3
boss = pygame.image.load('Game_Assets/Character_Sprites/lava_boss.png').convert_alpha()
boss = pygame.transform.scale(boss, (50, 50))
goblin_enemy = pygame.image.load(
    'Game_Assets/Character_Sprites/goblin.png').convert_alpha()
goblin_enemy = pygame.transform.scale(goblin_enemy, (20, 20))

dirt = pygame.image.load('Game_Assets/Map_Tiles/dirt0.png').convert_alpha()
dirt = pygame.transform.scale(dirt, tile_size)  # (fence, (16,16))

brick = pygame.image.load('Game_Assets/Map_Tiles/brick0.png').convert_alpha()
brick = pygame.transform.scale(brick, tile_size)

grass = pygame.image.load('Game_Assets/Map_Tiles/grass1.png').convert_alpha()
grass = pygame.transform.scale(grass, tile_size)

sand = pygame.image.load('Game_Assets/Map_Tiles/Sand1.png').convert_alpha()
sand = pygame.transform.scale(sand, tile_size)

door = pygame.image.load('Game_Assets/Map_Tiles/door.png').convert_alpha()
door = pygame.transform.scale(door, tile_size)

water = pygame.image.load('Game_Assets/Map_Tiles/water1.png').convert_alpha()
water = pygame.transform.scale(water, tile_size)

toxicwater = pygame.image.load(
    'Game_Assets/Map_Tiles/toxicwater.png').convert_alpha()
toxicwater = pygame.transform.scale(toxicwater, tile_size)

lava = pygame.image.load('Game_Assets/Map_Tiles/lava.jpg').convert_alpha()
lava = pygame.transform.scale(lava, tile_size)

restart_door = pygame.image.load('Game_Assets/Map_Tiles/door(restart).png').convert_alpha()
restart_door = pygame.transform.scale(restart_door, tile_size)
PLAYER = pygame.image.load(
    'Game_Assets/Character_Sprites/budget link.png').convert_alpha()
PLAYER = pygame.transform.scale(PLAYER, (25, 25))

PLAYER_rect = pygame.Rect(120, 115, 25, 25)
img_width, img_height = 20, 20
boss_img_width, boss_img_height = 50, 50
enemies = [
    [[Enemy(130, 370, goblin_enemy, img_width, img_height), [3, 3]],
     [Enemy(290, 350, goblin_enemy, img_width, img_height), [3, 3]]],
    [[Enemy(100, 700, goblin_enemy, img_width, img_height), [3, 3]],
     [Enemy(300, 240, goblin_enemy, img_width, img_height), [3, 3]],
     [Enemy(50, 500, goblin_enemy, img_width, img_height), [3, 3]]],
    [[Enemy(340, 123, goblin_enemy, img_width, img_height), [3, 3]],
     [Enemy(590, 420, goblin_enemy, img_width, img_height), [3, 3]],
     [Enemy(360, 120, goblin_enemy, img_width, img_height), [3, 3]],
     [Enemy(280, 460, goblin_enemy, img_width, img_height), [3, 3]]],
    [[Enemy(100, 400, boss, boss_img_width, boss_img_height, 'Boss'), [5, 5]]
    ]
    ]
game_maps = [
    load_map('Maps/tyler_map'),
    load_map('Maps/owen_map'),
    load_map('Maps/matt_map'),
    load_map('Maps/mason_map')
]

PLAYER_right = False
PLAYER_left = False
PLAYER_up = False
PLAYER_down = False
sword_right = False
sword_left = False
sword_up = False
sword_down = False
enemies_remaining = True

# 1st room, we then collide with the door, room will now be 1, 2, 3
# background song:
# change these to true respectively when a player gets hit, and check if the whole list is true

# 2nd step
# Create a Font object using font.Font() method of pygame.
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('Game_Assets/Fonts/timesnewroman.ttf', 32)

room = 0

run = True
while run:
  #if player_hit_points == 0:
    tile_rects = []
    door_rects = []
    restart_door_rects =[]
    screen.fill(
        (146, 244, 255))  # change this to a picture or a different color
    y = 0
    # second room -> increase room by 1, and load that new maps
    # room = 0
    for row in game_maps[room]:
        x = 0
        for tile in row:
            if tile == '1':
                screen.blit(dirt, (x * tile_size[0], y * tile_size[1]))

                tile_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
            # if the number in the map is 5 (door)
            if tile == '2':
                screen.blit(sand, (x * tile_size[0], y * tile_size[1]))

                tile_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
            if tile == '3':
                screen.blit(grass, (x * tile_size[0], y * tile_size[1]))

                tile_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
            if tile == '4':
                screen.blit(brick, (x * tile_size[0], y * tile_size[1]))

                tile_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
            if tile == '5':
                screen.blit(door, (x * tile_size[0], y * tile_size[1]))

                tile_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
                door_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
            if tile == '6':
                screen.blit(water, (x * tile_size[0], y * tile_size[1]))

            if tile == '7':
                screen.blit(toxicwater, (x * tile_size[0], y * tile_size[1]))
                tile_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
            if tile == '8':
                screen.blit(lava, (x * tile_size[0], y * tile_size[1]))
                tile_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
            if tile == '9':
                screen.blit(restart_door, (x * tile_size[0], y * tile_size[1]))
                restart_door_rects.append(
                    pygame.Rect(x * tile_size[0], y * tile_size[1],
                                tile_size[0], tile_size[1]))
            x += 1
        y += 1
    # PLAYER <- the image variable, not the rect
    if PLAYER_rect.right == restart_door_rects[0].left:
      player_hit_points = 3
      
    if PLAYER_rect.right == door_rects[0].left:
        # if PLAYER_rect.colliderect(door_rects[0]):  # [rect]
        # door_rects.append(PLAYER_rect)
        # door_rects[0]
        enemies_remaining = True
        

        room, PLAYER_rect, Sword_rect = switch_map(room)
        # room = 3
        # room = 0
        # room = 1

    if enemies_remaining == True:
        for e in range(len(enemies[room])):

            # print("Enemies in room: ", len(enemies[room]))
            # print("E:", e)
            # e = enemy_collision(e, enemies, room, Sword_rect)
            try:
                if enemies[room][e][0].rect.colliderect(Sword_rect):
                    enemies[room].remove(enemies[room][e])
            except:
                if e != 0:
                    e -= 1

            try:
                enemy_object = enemies[room][e][0]
                m = enemies[room][e][1]
            except:
                enemies_remaining = False

            enemy_object.draw(screen)
            enemy_object.move(m)
            if enemy_object.rect.left <= 0 or enemy_object.rect.right >= 800:
                m[0] *= -1
            if enemy_object.rect.top <= 0 or enemy_object.rect.bottom >= 600:
                m[1] *= -1

            if enemy_object.rect.colliderect(PLAYER_rect):
                player_hit_points = hitpoints(player_hit_points)
            if player_hit_points == 0:
                white = (255, 255, 255)
                red = (255, 0, 0)
                # X = 500
                # Y = 500
                screen.fill(red)
                game_over = font.render('GAME OVER', red, True)
                screen.blit(game_over, (500, 375))
                # pygame.display.set_caption(500, 500)
                # font = pygame.font.Font('')

                # 1. just close the game
                # 2. be to display a game over text, and then even further create like a try again button

    PLAYER_movement = [0, 0]
    sword_movement = [0, 0]
    if PLAYER_right:
        PLAYER_movement[0] += 2
    if PLAYER_left:
        PLAYER_movement[0] -= 2
    if PLAYER_up:
        PLAYER_movement[1] -= 2
    if PLAYER_down:
        PLAYER_movement[1] += 2

    if sword_right:
        sword_movement[0] += 2
    if sword_left:
        sword_movement[0] -= 2
    if sword_up:
        sword_movement[1] -= 2
    if sword_down:
        sword_movement[1] += 2
    # screen.blit(PLAYER, (PLAYER_rect.x, PLAYER_rect.y))
    PLAYER_rect, PLAYER_collisions = move(PLAYER_rect, PLAYER_movement,
                                          tile_rects)
    pygame.draw.rect(screen, (0, 0, 0), PLAYER_rect, 0)

    # 3rd step
    # Create a Text surface object i.e.surface object in which Text is drawn on it, using render() method of pygame font object.
    # create a text surface object,
    # on which text is drawn on it.
    #text = font.render('GeeksForGeeks', True, green, blue)
    health = font.render(f'Health points: {player_hit_points}', True, purple,
                         navy)
    level = font.render(f'Levels: {str(room + 1)}', True, purple, navy)

    # 4th step
    # Copying the Text surface object to the display surface object using blit() method of pygame display surface object.
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    # display_surface.blit(text, 12 387)
    # screen.blit(dirt, (x * tile_size[0], y * tile_size[1]))
    # x and y, are the column and row of the tile from the map file
    screen.blit(health, (700, 0))
    screen.blit(level, (500, 0))
    Sword_rect, sword_collisions = move(Sword_rect, sword_movement, tile_rects)
    pygame.draw.rect(screen, (255,0,0), Sword_rect, 0)

    screen.blit(PLAYER, (PLAYER_rect.x, PLAYER_rect.y))
    pygame.draw.rect(screen, (255, 0, 0), Sword_rect, 0)
    screen.blit(sword, (Sword_rect.x, Sword_rect.y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            WINDOW = pygame.display.set_mode(event.size)

        if event.type == KEYDOWN:
            if event.key == K_d:
                PLAYER_right = True
                sword_right = True
            if event.key == K_a:
                PLAYER_left = True
                sword_left = True
            if event.key == K_w:
                PLAYER_up = True
                sword_up = True
            if event.key == K_s:
                PLAYER_down = True
                sword_down = True
            # if event.key == pygame.K_r and player_hit_points == 0:
            #     main()

        if event.type == KEYUP:
            if event.key == K_d:
                PLAYER_right = False
                sword_right = False
            if event.key == K_a:
                PLAYER_left = False
                sword_left = False
            if event.key == K_w:
                PLAYER_up = False
                sword_up = False
            if event.key == K_s:
                PLAYER_down = False
                sword_down = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
