import pygame
import random
import os
pygame.mixer.init()
pygame.init()
pygame.font.init()

# color
lightblue=(151,221,236)
red=(255,0,0)
black=(0,0,0)
green=(42,232,84)
white=(255,255,255)
blue=(0,0,255)
color1=(101,222,61)
color2=(172,255,151)
color3=(255,128,128)
color4=(217,63,165)
color5=(168,148,36)
color6=(243,235,225)
color7=(87,47,94)
color8=(168,149,190)
color9=(106,169,148)
color10=(7,68,189)
list1=[lightblue,color10,color3,color4,color5,color6,color7,color8,color9,color1,color2,black,green,blue,white]
# game variable
screen_height=400
screen_width=600

snake_height=15
snake_width=15

food_width=15
food_height=15
fps=90

pause=False
clock = pygame.time.Clock()

gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Hungry Snake")

bgimg=pygame.image.load("snake1.JPG")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

bgimg2=pygame.image.load("welcome.JPG")
bgimg2=pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha()

bgimg3=pygame.image.load("gameover.JPG")
bgimg3=pygame.transform.scale(bgimg3,(screen_width,screen_height)).convert_alpha()

bgimg4=pygame.image.load("pause.JPG")
bgimg4=pygame.transform.scale(bgimg4,(screen_width,screen_height)).convert_alpha()

bgimg5=pygame.image.load("instruction.JPG")
bgimg5=pygame.transform.scale(bgimg5,(screen_width,screen_height)).convert_alpha()
def button_outline(color,x,y,w,h):
    pygame.draw.ellipse(gameWindow, color, [x, y, w, h],10)

def border(color,x,y,w,h):
    pygame.draw.rect(gameWindow, color, [x, y, w, h], 8)



def screen_text(text,color,x,y,f):
    font = pygame.font.SysFont(None, f)
    text=font.render(text,True,color)
    gameWindow.blit(text,[x,y])

def retry(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//4
    txt_y=y+h//5
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green, x, y, w, h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)
        if click[0] == 1 and s!=None:
           if s=="retry":
                gameloop()
    screen_text(text, txt_color, txt_x, txt_y, f)

def highscore():
    exit_game=False
    if (not os.path.exists("HighScore.txt")):
        f = open("HighScore.txt", 'w')
        f.write('0')
    f = open("HighScore.txt", 'r')
    while not exit_game:
        f = open("HighScore.txt", 'r')
        highscore=f.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    welcome()
        gameWindow.fill(green)
        screen_text("HighScore :" +str(highscore),red,110,100,80)
        pygame.display.update()
    pygame.quit()
    quit()



def about():
    exit_game = False
    f = open("About.txt", 'r')
    while not exit_game:
        f = open("About.txt", 'r')
        about = f.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    welcome()
        gameWindow.fill(green)
        screen_text(str(about), blue, 15,20,35)
        pygame.display.update()
    pygame.quit()
    quit()
def instruction():
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                        welcome()
        gameWindow.fill(green)
        gameWindow.blit(bgimg5, (0, 0));
        # screen_text(str(about), blue, 15,20,35)
        pygame.display.update()
    pygame.quit()
    quit()



def game_exit():
    exit_game=True
    pygame.quit()
    quit()

def unpause():
    global  pause
    pause=False

def paused():
    while pause:
        gameWindow.fill(black)
        gameWindow.blit(bgimg4, (0, 0))
        resume_button(color2, 220, 140, 150, 50, color2, "Resume", red, 45, "resume")
        new_game(color2, 220, 200, 150, 50, color2, "New Game", red, 35, "newgame")
        exit_button(color2, 220, 260,150, 50, color2, "Exit", red, 45, "exit")

        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    unpause()


def resume_button(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//10
    txt_y=y+h//4
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green, x, y, w, h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)
        if click[0] == 1 and s!=None:
           if s=="resume":
                unpause()
    screen_text(text, txt_color, txt_x, txt_y, f)

def new_game(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//10
    txt_y=y+h//4
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green, x, y, w, h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)
        if click[0] == 1 and s!=None:
            if s=="newgame":
                gameloop()
    screen_text(text, txt_color, txt_x, txt_y, f)

def exit_button(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//4
    txt_y=y+h//5
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green, x, y, w, h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)
        if click[0] == 1 and s!=None:
            if s=="exit":
                game_exit()
    screen_text(text, txt_color, txt_x, txt_y, f)

def button1(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//4
    txt_y=y+h//5
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green,x,y,w,h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)

        if click[0] == 1 and s!=None:
           if s=="play":
                gameloop()
    screen_text(text, txt_color, txt_x, txt_y, f)

def button2(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//10
    txt_y=y+h//4
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green, x, y, w, h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)
        if click[0] == 1 and s!=None:
            if s=="highscore":
                highscore()
    screen_text(text, txt_color, txt_x, txt_y, f)

def button3(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//5
    txt_y=y+h//5
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green, x, y, w, h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)
        if click[0] == 1 and s!=None:
            if s=="about":
                about()
    screen_text(text, txt_color, txt_x, txt_y, f)

def button5(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//3
    txt_y=y+h//5
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green, x, y, w, h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)
        if click[0] == 1 and s!=None:
            if s=="exit":
                game_exit()
    screen_text(text, txt_color, txt_x, txt_y, f)

def button4(color,x,y,w,h,sec_c,text,txt_color,f,s=None):
    txt_x=x+w//10
    txt_y=y+h//5
    pygame.draw.ellipse(gameWindow,color,[x,y,w,h])
    # button_outline(green, x, y, w, h)
    mouse=pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x< mouse[0] < x+w and y< mouse[1] < y+h:
        pygame.draw.ellipse(gameWindow,sec_c, [x, y, w, h])
        button_outline(green, x, y, w, h)
        if click[0] == 1 and s!=None:
            if s=="Instruction":
                instruction()
    screen_text(text, txt_color, txt_x, txt_y, f)


def inc_snake(gamewindow,color,snk_list,snake_width,snake_height):

    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_width,snake_height])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgimg2, (0, 0))
        button1(color2, 240, 115, 150, 50, color2, "Start", red, 45, "play")
        button2(color2, 240, 170, 150, 50, color2, "HighScore", red, 35, "highscore")
        button4(color2, 240, 225, 150, 50, color2, "Instruction", red, 35, "Instruction")
        button3(color2, 240, 280, 150, 50, color2, "About", red, 45, "about")
        button5(color2, 240,335, 150, 50, color2, "Exit", red, 45, "exit")


        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True


def gameloop():
    global  pause
    score = 0
    fps = 60

    snk_list = []
    snk_lenght = 1
    exit_game = False
    game_over = False
    snake_x = random.randint(50, screen_width // 2)
    snake_y = random.randint(50, screen_width // 2)

    velocity_x = 0
    velocity_y = 0
    game_speed=0
    c=0
    food_x = random.randint(30, screen_width // 2)
    food_y = random.randint(60, screen_width // 2)
    if (not os.path.exists("HighScore.txt")):
        f = open("HighScore.txt", 'w')
        f.write('0')
    f = open("HighScore.txt", 'r')
    highscore = f.read()
    while not exit_game:
        if game_over:
            f=open("HighScore.txt",'w')
            f.write(str(highscore))
            gameWindow.fill(black)
            gameWindow.blit(bgimg3, (0, 0))
            retry(color2, 220, 220, 150, 50, color2, "Retry", red, 45, "retry")
            button4(color2, 220, 300, 150, 50, color2, "Exit", red, 45, "exit")
            screen_text(str(score), red, 350, 25,60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        paused()
                    if event.key==pygame.K_RIGHT:
                        velocity_x = 3 +game_speed
                        velocity_y = 0
                    if event.key==pygame.K_LEFT:
                        velocity_x = -3-game_speed
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_y = -3-game_speed
                        velocity_x = 0
                    if event.key==pygame.K_DOWN:
                        velocity_y = 3+game_speed
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) <= 10 and abs(snake_y - food_y) <= 10:
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                food_x = random.randint(100, screen_width // 2)
                food_y = random.randint(100, screen_width // 2)
                score += 10
                c+=1
                if c>=5:
                    c=0
                    game_speed+=1
                    inc_snake(gameWindow, blue, snk_list, snake_width, snake_height)


                # itne se length badani hai
                snk_lenght+=4
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(color1)
            gameWindow.blit(bgimg,(0,40))
            border(black,0,40,600,360)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_lenght:
                del snk_list[0]
            if snake_x<8 or snake_x>screen_width-8 or snake_y<40 or snake_y>screen_height-8:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_over=True
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
            inc_snake(gameWindow,random.choice(list1) ,snk_list,snake_width,snake_height)
            pygame.draw.rect(gameWindow, red, [food_x,food_y,food_width,food_height])
            screen_text("    Score : "+str(score) + "            HighScore : " +str(highscore),red,5,5,40)


        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()