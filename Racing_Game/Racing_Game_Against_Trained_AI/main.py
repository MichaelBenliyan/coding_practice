from lib2to3 import pygram
import neat
import pygame
import time
import math
import os.path
from utils import scale_image, blit_rotate_center, blit_text_center, blit_text_subcenter, blit_text_abovecenter
import pickle
pygame.font.init()


'''Track Background Images'''
GRASS = scale_image(pygame.image.load("images/grass.jpg"), 1.8)
TRACK = pygame.image.load("images/my_track.png")
TRACK_BORDER = pygame.image.load("images/my_track_border.png")

FINISH_LINE = pygame.image.load("images/finish_line.png")
FINISH_LINE_POSITION = (37, 300)
bg_images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH_LINE, FINISH_LINE_POSITION)]

MAIN_MENU = pygame.image.load("images/main_menu.png")

'''Masks for Pixel Perfect Collisions'''
FINISH_LINE_MASK = pygame.mask.from_surface(FINISH_LINE)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)


'''Cars Images'''
PLAYER_CAR = scale_image(pygame.image.load("images/convertable_car.png"), 0.75)
AI_CAR = scale_image(pygame.image.load("images/cpu_convertable_car.png"), 0.75)


'''Window''' 
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")


'''Font'''
HEADER_FONT = pygame.font.SysFont("comicsans", 44)
SUBHEADER_FONT = pygame.font.SysFont("comicsans", 32)
BODY_FONT = pygame.font.SysFont("comicsans", 20)


'''Classes'''
class AbstractCar: 
    def __init__(self, max_velocity, rot_velocity):
        self.image = self.IMAGE
        self.cur_image = self.image
        self.mask = None
        self.max_velocity = max_velocity
        self.rot_velocity = rot_velocity
        self.velocity = max_velocity
        self.acceleration = max_velocity/30
        self.angle = 0
        self.x, self.y = self.START_POSITION
        self.cur_x, self.cur_y = self.x, self.y
        self.prev_x, self.prev_y = 0, 0
        self.time_since_bounce = 0
        self.laptime = 0

    def draw(self, window): 
        result = blit_rotate_center(window, self.image, (self.x, self.y), self.angle)
        self.cur_image = result[0]
        self.cur_x, self.cur_y = result[1]
        
    def move_forward(self): 
        self.velocity = min(self.velocity + self.acceleration/2, self.max_velocity)
        self.move()

    def move_backward(self): 
        self.velocity = max(self.velocity - self.acceleration, -self.max_velocity/2)
        self.move()

    def move(self): 
        radians = math.radians(self.angle)
        vertical_velocity = math.cos(radians) * self.velocity
        horizontal_velocity = math.sin(radians) * self.velocity
        self.y -= vertical_velocity
        self.x -= horizontal_velocity
        
    def collide(self, track_mask, x=0, y=0): 
        car_mask = pygame.mask.from_surface(self.cur_image)
        offset = (int(self.cur_x-x), int(self.cur_y-y))
        poi = track_mask.overlap(car_mask, offset)
        return poi
    
    def reset(self): 
        self.x, self.y = self.START_POSITION
        self.cur_x, self.cur_y = self.START_POSITION
        self.angle = 0
        self.velocity = 0
        self.laptime = 0
        self.time_since_update = 0
    
class PlayerCar(AbstractCar): 
    IMAGE = PLAYER_CAR
    START_POSITION = (75, 250)
    SPEEDS = [(1, 10), (1.5, 4), (2, 4), (2.5, 6), (3, 6)]
    level = 0
    # max_velocity = SPEEDS[level][0]
    # rot_velocity = SPEEDS[level][1]
    def reset(self, level): 
        super().reset()
        self.max_velocity = self.SPEEDS[level][0]
        self.rot_velocity = self.SPEEDS[level][1]

    def rotate(self, left=False, right=False): 
        if left: 
            self.angle += self.rot_velocity
        elif right: 
            self.angle -= self.rot_velocity

    def reduce_speed(self): 
        if self.velocity < 0: 
            self.velocity = max(self.velocity+self.acceleration, -self.max_velocity)
        else: 
            self.velocity = max(self.velocity - self.acceleration, 0)
        print(self.velocity)
        self.move()

    def bounce(self): 
        if self.velocity <= 0: 
            self.velocity = 3
        else: 
            self.velocity = -3
        self.move()

class AICar(AbstractCar): 
    IMAGE = AI_CAR
    START_POSITION = (85, 250)
    def reset(self, level): 
        super().reset()
        

    def reduce_speed(self): 
        self.velocity = max(self.velocity - self.acceleration, 0)
        if self.velocity < 0: 
            self.velocity = max(self.velocity+self.acceleration, -self.max_velocity)
        self.move()

    def rotate(self, left=False, right=False): 
        if left: 
            self.angle += self.rot_velocity/2
        elif right: 
            self.angle -= self.rot_velocity

    def bounce(self): 
        if self.velocity <= 0: 
            self.velocity = 2
        else: 
            self.velocity = -2
        self.move()
    
    def radar_forward(self, angle, window): 
        length = 0
        x = int(self.x)
        y = int(self.y)
        angle = (angle+360)%360

        while length < 200 and not TRACK_BORDER.get_at((round(x), round(y)))[3] != 0:  
            length += 1
            x = x - math.sin(math.radians(self.angle))
            y = y - math.cos(math.radians(self.angle))
        
        # pygame.draw.line(window, (0, 0, 0), (self.x, self.y), (round(x), round(y)), 1)
        # pygame.draw.circle(window, (0, 255, 0), (x, y), 3)
        # pygame.display.update()
        return length

    def radar_right(self, angle, window): 
        length = 0
        x = int(self.x)
        y = int(self.y)
        angle = (angle+360)%360

        while length < 200 and not TRACK_BORDER.get_at((round(x), round(y)))[3] != 0:  
            length += 1
            x = x - math.sin(math.radians(self.angle-90))
            y = y - math.cos(math.radians(self.angle-90))
        
        # pygame.draw.line(window, (0, 0, 0), (self.x, self.y), (round(x), round(y)), 1)
        # pygame.draw.circle(window, (0, 255, 0), (x, y), 3)
        # pygame.display.update()
        return length

    def radar_left(self, angle, window): 
        length = 0
        x = int(self.x)
        y = int(self.y)
        angle = (angle+360)%360

        while length < 200 and not TRACK_BORDER.get_at((round(x), round(y)))[3] != 0: 
            length += 1
            x = x - math.sin(math.radians(self.angle+90))
            y = y - math.cos(math.radians(self.angle+90))
        
        # pygame.draw.line(window, (0, 0, 0), (self.x, self.y), (round(x), round(y)), 1)
        # pygame.draw.circle(window, (0, 255, 0), (x, y), 3)
        # pygame.display.update()
        return length
    
    def radar_forwardleft(self, angle, window): 
        length = 0
        x = int(self.x)
        y = int(self.y)
        angle = (angle+360)%360

        while length < 200 and not TRACK_BORDER.get_at((round(x), round(y)))[3] != 0: 
            length += 1
            x = x - math.sin(math.radians(self.angle+45))
            y = y - math.cos(math.radians(self.angle+45))
        
        # pygame.draw.line(window, (0, 0, 0), (self.x, self.y), (round(x), round(y)), 1)
        # pygame.draw.circle(window, (0, 255, 0), (x, y), 3)
        # pygame.display.update()
        return length

    def radar_forwardright(self, angle, window): 
        length = 0
        x = int(self.x)
        y = int(self.y)
        angle = (angle+360)%360

        while length < 200 and not TRACK_BORDER.get_at((round(x), round(y)))[3] != 0: 
            length += 1
            x = x - math.sin(math.radians(self.angle-45))
            y = y - math.cos(math.radians(self.angle-45))
        
        # pygame.draw.line(window, (0, 0, 0), (self.x, self.y), (round(x), round(y)), 1)
        # pygame.draw.circle(window, (0, 255, 0), (x, y), 3)
        # pygame.display.update()
        return length
        
class GameInfo: 
    LEVELS = 5

    def __init__(self, level=1):
        self.level = level
        self.started = True
        self.level_start_time = 0

    def next_level(self): 
        self.level += 1
        self.started = True

    def reset(self): 
        self.started = True
        self.level_start_time = 0
    
    def game_finished(self): 
        return self.level > self.LEVELS
    
    def start_level(self): 
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self): 
        if not self.started: 
            return 0
        else: 
            return round(time.time() - self.level_start_time)


'''Functions'''
def draw(window, images, ai_car, game_info, player_car=None, ): 
    for image, position in images:
        window.blit(image, position)

    if player_car is not None: 
        player_car.draw(window)
        velocity_text = BODY_FONT.render(f"Speed: {round(player_car.velocity, 1)}px/s", 1, (0, 0, 0))
        window.blit(velocity_text, (window.get_width()-window.get_width()/4.7, window.get_height() - velocity_text.get_height()-10))
    
    ai_car.draw(window)
    pygame.display.update()

def move_player(player_car): 
    keys = pygame.key.get_pressed()
    moved = False
    if player_car.time_since_bounce > 10:
        if keys[pygame.K_LEFT] and player_car.velocity >0: 
            player_car.rotate(left=True)
        if keys[pygame.K_RIGHT] and player_car.velocity >0: 
            player_car.rotate(right=True)
        if keys[pygame.K_UP] and player_car.collide(TRACK_BORDER_MASK) == None: 
            moved = True
            player_car.move_forward()
        if keys[pygame.K_DOWN]: 
            moved = True
            player_car.move_backward()

    if not moved: 
        player_car.reduce_speed()

def main_menu(genomes, config): 
    
    '''Start Menu'''
    WINDOW.blit(GRASS, (0,0))
    WINDOW.blit(TRACK, (0,0))
    WINDOW.blit(MAIN_MENU, (WIDTH/2-WIDTH/4, HEIGHT/2-HEIGHT/6)) 
    pygame.display.update()
    run_menu = True
    while run_menu: 
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_q:
                    run_menu = False
                    break
                elif event.key == pygame.K_a: 
                    print(pygame.mouse.get_pos())
        
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  
            if 196 <= mouse[0] <= 279 and 449<= mouse[1] <=483:
                print("Easy")  
                difficulty = 0.5
                run_genomes(genomes, config, difficulty)
                pygame.quit()
                quit()
            elif 312 <= mouse[0] <= 396 and 449<= mouse[1] <=483:
                print("Medium")
                difficulty = 0.35
                run_genomes(genomes, config, difficulty)
                pygame.quit()
                quit()
            elif 426 <= mouse[0] <= 510 and 449<= mouse[1] <=483:
                print("Hard")
                difficulty = 0.20
                run_genomes(genomes, config, difficulty)
                pygame.quit()
                quit()

def lose_screen(genomes, config, difficulty, player_car, ai_car):
    pass

def win_screen(genomes, config, difficulty, player_car, ai_car): 
    '''Win Screen'''
    WINDOW.blit(GRASS, (0,0))
    WINDOW.blit(TRACK, (0,0))
    #display GOOD JOB!
    # WINDOW.blit(MAIN_MENU, (WIDTH/2-WIDTH/4, HEIGHT/2-HEIGHT/6)) 
    pygame.display.update()
    win_screen = True
    while win_screen: 
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_q:
                    win_screen = False
                    break
                elif event.key == pygame.K_a: 
                    print(pygame.mouse.get_pos())
        
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  
            if 196 <= mouse[0] <= 279 and 449<= mouse[1] <=483:
                '''Repeat Level'''  
                player_car.reset()
                ai_car.reset()
                countdown(genomes, config, difficulty, player_car, ai_car)
                pygame.quit()
                quit()
            elif 312 <= mouse[0] <= 396 and 449<= mouse[1] <=483:
                '''Next Level'''
                player_car.reset()
                ai_car.reset()
                countdown(genomes, config, difficulty, player_car, ai_car)
                pygame.quit()
                quit()
            elif 426 <= mouse[0] <= 510 and 449<= mouse[1] <=483:
                '''Main Menu'''
                main_menu(genomes, config)
                pygame.quit()
                quit()
    pass 

'''Main Game Function'''
def run_genomes(genomes, config, difficulty):
    
    '''Setup Player Car'''
    player_car = (PlayerCar(1, 2))
    print(player_car.velocity)
    '''Setup AI Car'''
    net = neat.nn.FeedForwardNetwork.create(genomes[0][1], config)
    ai_car = (AICar(0.85, 2))
    print(ai_car.velocity)

    '''Game Details'''
    game_info = GameInfo()
    clock = pygame.time.Clock()
    FPS = 60
    run = True
    countdown = FPS*3 + 20
    while countdown > 0: 
        while countdown > countdown - FPS: 
            clock.tick(FPS) 
            countdown -= 1
            # display 3
        while countdown > countdown - FPS*2:
            clock.tick(FPS) 
            countdown -= 1
            #display 2 
        while countdown > countdown - FPS*3: 
            clock.tick(FPS) 
            countdown -= 1
            #display 1
        clock.tick(FPS)
        countdown -= 1
        #display GO!

    
    '''Main Game / Event Loop'''
    while run:
        '''Game Clock'''
        #Makes sure clock is consistent. Ticks FPS times per second
        clock.tick(FPS) 

        '''Update Screen'''
        #draw all background images and update window to reflect all changes
        draw(WINDOW, bg_images, ai_car, game_info, player_car=player_car)
        pygame.display.update()

        '''Pygame Commands'''
        for event in pygame.event.get(): 
            #if you close game window the game will quit
            if event.type == pygame.QUIT: 
                run = False
                pygame.quit()
                quit()
            #print (x, y) coordinate of mouse position in window. Useful for debugging.
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_l:
                    x, y = pygame.mouse.get_pos()
                    print(x, y) 
                elif event.key == [pygame.K_r]: 
                    game_info.reset()
                    player_car.reset(game_info.level)
                    ai_car.reset(game_info.level)            

        '''Inriment Laptimes'''           
        #incriment laptime. Happens once per car per tick and 60 times per second. 
        ai_car.laptime += 1
        player_car.laptime += 1
        player_car.time_since_bounce += 1
            
        '''AI and Player Movement'''
        #Car is always moving forward and turning left, AI only controls when to turn right. 
        ai_car.move_forward()
        ai_car.rotate(left=True)
        move_player(player_car)
        
        '''Distance Radars for AI'''
        #Send out 5 radars so the car knows distance from itself to walls
        distance_forward = ai_car.radar_forward(ai_car.angle, WINDOW)
        distance_right = ai_car.radar_right(ai_car.angle, WINDOW)
        distance_left = ai_car.radar_left(ai_car.angle, WINDOW)
        distance_forwardleft = ai_car.radar_forwardleft(ai_car.angle, WINDOW)
        distance_forwardright = ai_car.radar_forwardright(ai_car.angle, WINDOW)
                
        '''NEAT Inputs (What information NEAT will have to make decisions)'''
        #Passing in 5 distance rays and the cars angle
        output = net.activate((distance_forward, distance_left, distance_right, distance_forwardleft, distance_forwardright, (ai_car.angle+360)%360))
        
        '''NEAT Outputs aka AI controling car options'''
        if output[0] > 0: 
            ai_car.rotate(right=True)

        '''Check if Car Should be Removed'''
        ai_finish_line_poi_collide = ai_car.collide(FINISH_LINE_MASK, *FINISH_LINE_POSITION)
        player_finish_line_poi_collide = player_car.collide(FINISH_LINE_MASK, *FINISH_LINE_POSITION)
        
        #If AI Finished First
        if ai_finish_line_poi_collide != None:
            #if from the correct side
            if ai_finish_line_poi_collide[1] != 0:  
                print("You Lost")
                lose_screen(genomes, config, difficulty, player_car, ai_car)
                run = False
                pygame.quit()
                quit()
        
        #If player hit Wall/Finish
        if player_car.time_since_bounce > 10:
            if player_car.collide(TRACK_BORDER_MASK) != None: 
                player_car.bounce()
                player_car.time_since_bounce = 0
            if player_finish_line_poi_collide != None:
                if player_finish_line_poi_collide[1] == 0: 
                    player_car.bounce()
                    player_car.time_since_bounce = 0
                else: 
                    win_screen(genomes, config, difficulty, player_car, ai_car)
                    run = False
                    pygame.quit()
                    quit()
                    blit_text_center(WINDOW, HEADER_FONT, "You Won!")
                    blit_text_abovecenter(WINDOW, SUBHEADER_FONT, f"LapTime: {game_info.get_level_time()}s")
                    blit_text_subcenter(WINDOW, SUBHEADER_FONT, f"TopSpeed: {player_car.top_speed}px/s")
                    pygame.display.update()
                    stay_on_screen = True
                    while stay_on_screen: 
                        for event in pygame.event.get(): 
                            if event.type == pygame.QUIT: 
                                pygame.quit()
                                break
                            if event.type == pygame.KEYDOWN: 
                                if event.key == pygame.K_SPACE:
                                    stay_on_screen = False
                    game_info.next_level()
                    player_car.reset(game_info.level)
                    ai_car.reset(game_info.level)

        '''Next generation if no cars left'''
        if ai_car is None: 
            run = False
            break           


'''Play_Game'''
def play_game(config_path, genome_path="Prev_Winners/20_92__5_2_0042.pkl"):
    # Load requried NEAT config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Unpickle saved winner
    with open(genome_path, "rb") as f:
        genome = pickle.load(f)

    # Convert loaded genome into required data structure
    genomes = [(1, genome)]

    # Call game with only the loaded genome
    main_menu(genomes, config)

if __name__ == "__main__": 
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "feed_forward_config.txt")
    # run(config_path) 
    play_game(config_path)