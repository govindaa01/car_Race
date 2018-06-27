import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600
crash_sound = pygame.mixer.Sound("Crash.wav")
#pygame.mixer.music.load('Coupe.mp3')
gameIcon = pygame.image.load('gameIcon.png')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
pygame.display.set_icon(gameIcon)
black = (0,0,0)
white = (255,255,255)
blue= (0,0,255)
green=(0,200,0)
red=(200,0,0)
bright_green=(0,255,0)
bright_red=(255,0,0)
car_width=45
clock = pygame.time.Clock()
logo = pygame.image.load('logo.png')
carImg = pygame.image.load('car race.png')
crashedCar=pygame.image.load('crashedcar.png')
pause=False

def paused():
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged:"+str(count),True,black)
    gameDisplay.blit(text,(0,0))
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def crashed_car(x,y):
    gameDisplay.blit(crashedCar,(x,y))
    

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#def message_display(text):
    #largeText=pygame.font.Font('freesansbold.ttf',115)
    #TextSurf,TextRect=text_objects(text,largeText)
    #TextRect.center=((display_width/2),(display_height/2))
    #gameDisplay.blit(TextSurf,TextRect)
    #pygame.display.update()

    time.sleep(2)

    game_loop()
    
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause=False

def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()   
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    pygame.mixer.music.load('Coupe.wav')
    pygame.mixer.music.play(-1)
    intro = True
    global pause
    while intro:
        for event in pygame.event.get():
           # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        gameDisplay.blit(logo,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2+110))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO!",150,500,100,50,green,bright_green,game_loop)
        button("QUIT",550,500,100,50,red,bright_red,quitgame)
       
        
        
        pygame.display.update()
        clock.tick(15)
        
        
    
def game_loop():
    pygame.mixer.music.load('Coupe.wav')
    pygame.mixer.music.play(-1)
    x=display_width*0.45
    y=display_height-100
    x_change=0
    movement=5
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width-thing_width)
    thing_starty = -600
    thing_speed = 3
    dodged=0
    global pause
    
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-1*movement
                if event.key==pygame.K_RIGHT:
                    x_change=movement
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
                

        x+=x_change   
        gameDisplay.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_height,blue)
        thing_starty+=thing_speed
        
        car(x,y)
        if x>display_width-car_width or x<0:
            crashed_car((display_width/2)-100,(display_height/2)-200)
            crash()
        if thing_starty>display_height:
            thing_starty=-100
            thing_startx = random.randrange(0, display_width-thing_width)
            dodged+=1
            movement+=.5
            thing_speed+=.8

        if y < thing_starty+thing_height-thing_speed:
           

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                
                crashed_car((display_width/2)-100,(display_height/2)-200)
                things_dodged(dodged)
                pygame.display.update()
                crash()
        things_dodged(dodged)
        pygame.display.update()
        clock.tick(60)

game_intro()        
game_loop()     
pygame.quit()
quit()
