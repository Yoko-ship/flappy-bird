import pygame,os,time,math,random,sys
from threading import Thread


pygame.init()
screen_width = 1200
screen_heigth = 700
fps = 60
screen = pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption("Flib Bird")
my_font = pygame.font.SysFont("Times New Roman",20)
clock = pygame.time.Clock()
flib_bird_image = pygame.image.load("hqdefault_pixian_ai.png").convert_alpha()
background_fon = pygame.image.load("fb-game-background.png").convert_alpha()
bottom_background_fon = pygame.image.load("bottom-background.png").convert_alpha()
object_image = pygame.image.load("flappybird-pipe.png")
object_image_horizon = pygame.image.load("flappybird-pipe1.png")
small_object = pygame.image.load("flappybird-pipe2.png")
big_object = pygame.image.load("flappybird-pipe3.png")
som = pygame.image.load("s-l400_pixian_ai.png")
main_menu_image = pygame.image.load("tumblr_static_tbg.png")
grac = pygame.image.load("party-popper.png")



#* Scrolling bk
scrolling = 0

#* Sprite Groups
all_players = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
obstacle_group_horizon = pygame.sprite.Group()
money_group = pygame.sprite.Group()


  

 
jump_strength = -15
gravity = 0.6
score = 0
class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (400,screen_heigth / 2)
        self.is_jump = False
        self.speedy = 0

    def update(self):
        global run
        self.rect.y += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jump:
            self.speedy = jump_strength
            self.is_jump = True
        
        self.speedy += gravity
        self.rect.y += self.speedy

        if self.is_jump == True:
            self.speedy = 0
            self.is_jump = False
        
        

        if self.rect.bottom >= 700:
            run = False

 
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

  

    def update(self):
        if self.rect.x <= 0:
            self.kill()
        
        self.rect.x -= 5

class ObstacleHorizon(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        if self.rect.x <= 0:
            self.kill()

        self.rect.x -= 5
 

class Money(pygame.sprite.Sprite):
    def __init__(self,image,x,):
        super().__init__()
        self.direction = random.randint(150,600)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,self.direction)
    
 
    def update(self):
        if self.rect.x <= 0:
            self.kill()

        self.rect.x -= 5
 
     


player = Player(flib_bird_image)
all_players.add(player)
#* BC SCROLLING
background_width = background_fon.get_width()
tiles = math.ceil(screen_width / background_width) + 1


background_bottom_width = bottom_background_fon.get_width()
numbers = math.ceil(screen_width / background_bottom_width) +1

#*Button Settings
text_font = pygame.font.SysFont("Times New Roman",25)
button_surface = pygame.Surface((150,50))
button_text = text_font.render("Start game",False,(0,0,0))
button_text_rect = button_text.get_rect(center = (button_surface.get_width() /2 , button_surface.get_height()/ 2))
button_rect = pygame.Rect(300,200,400,900)

quit_surface = pygame.Surface((150,50))
quit_text = text_font.render("Quit game",False,(0,0,0))
quit_text_rect = quit_text.get_rect(center = (quit_surface.get_width()  /2, quit_surface.get_height() /2 ))
quit_rect = pygame.Rect(800,200,400,900)


main_menu = False
while (main_menu == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                main_menu = True
            if quit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

            
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface,(127,127,212),(1,1,148,48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
        

        if quit_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(quit_surface,(192,192,192),(1,1,148,48))
        else:
            pygame.draw.rect(quit_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(quit_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(quit_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(quit_surface, (0, 100, 0), (1, 48, 148, 10), 2)

    screen.blit(main_menu_image,(0,0))
    button_surface.blit(button_text,button_text_rect)
    screen.blit(button_surface,(button_rect.x,button_rect.y))
    
    quit_surface.blit(quit_text,quit_text_rect)
    screen.blit(quit_surface,(quit_rect.x,quit_rect.y))
    pygame.display.flip()


run = True
paused = False
while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if pygame.sprite.groupcollide(all_players,obstacle_group,False,False):
                run = False           
            
            if pygame.sprite.groupcollide(all_players,obstacle_group_horizon,False,False):
                run = False
  
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
        
        if not paused:

            #*Adding sprites 
            if len(all_players) == 0:
                player = Player(flib_bird_image)
                all_players.add(player)
            all_players.update()

            if len(obstacle_group) <= 2:
                obstacles = Obstacle(object_image,1300,620)
                small_obstacle = Obstacle(object_image,1800,770)
                big_obstacle = Obstacle(big_object,2300,670)
                obstacle_group.add(big_obstacle)
                obstacle_group.add(small_obstacle)
                obstacle_group.add(obstacles)
            obstacle_group.update()       
                

            if len(obstacle_group_horizon) <= 2:
                obstacles_horizon = ObstacleHorizon(object_image_horizon,1300,40)
                small_obstacle_horizon = ObstacleHorizon(small_object,1800,130)
                big_horizon  = ObstacleHorizon(object_image,2300,80)
                obstacle_group_horizon.add(obstacles_horizon)
                obstacle_group_horizon.add(small_obstacle_horizon)
                obstacle_group_horizon.add(big_horizon)
            obstacle_group_horizon.update()
                
            if len(money_group) == 0:
                som_money = Money(som,2000)
                money_group.add(som_money)
            money_group.update()

            
            
                #*Collide
                

            if pygame.sprite.groupcollide(all_players,money_group,True,True):
                score += 10
                
 


                #*Endlessly Scrolling
            for i in range(0,tiles):
                screen.blit(background_fon,(i * background_width + scrolling,0))
                
                #*scrolling 
            scrolling -= 5
                #*reset scrolling 
            if abs(scrolling) > background_width:
                scrolling = 0

                

            for j in range(0,numbers):
                screen.blit(bottom_background_fon,(j * background_bottom_width + scrolling,575))

            #*Score
            

                

            score_text = my_font.render(f"Score: {score}",True,(0,0,0))
            screen.blit(score_text,(10,20))
            all_players.draw(screen)
            obstacle_group.draw(screen)
            obstacle_group_horizon.draw(screen)
            money_group.draw(screen)
            pygame.display.flip()
pygame.quit()
