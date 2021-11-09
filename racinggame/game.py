import pygame
pygame.init()

wildth, height = 1280, 720
win = pygame.display.set_mode((wildth, height))

pygame.display.set_caption("ขี่ไม้กวาด")

bg = pygame.image.load("sprite/racing/bg/mountain.png").convert()
bg2 = pygame.image.load("sprite/racing/bg/forest1.jpg").convert()
bg3 = pygame.image.load("sprite/racing/bg/library.jpg").convert()
bg4 = pygame.image.load("sprite/racing/bg/forest1.jpg").convert()
bg_wildth, bg_height = bg.get_rect().size

start_scrolling = wildth/2
stage_wildth = 1280*2
stage_position_x = 0

circle_radius = 25
circle_posistion_x = circle_radius

bg_scrolling = 0

FONT = pygame.font.SysFont("Sans", 20)

def redrawGameWindow():
    global walkcount
    
    if walkcount + 1 >= 44: #กัน out of range
        walkcount = 0

    if right:
        win.blit(walkright[walkcount], (x, y))
        walkcount += 1
    
    elif left:
        win.blit(walkright[walkcount], (x, y))
        walkcount += 1
        
    else:
        win.blit(nowalk[walkcount], (x, y))
        walkcount += 1
    pygame.display.update()
    
def fadescreen():
    """blit fade screen"""
    fade = pygame.Surface((1280, 720))
    fade.fill((0,0,0))
    for alpha in range(0, 75):
        fade.set_alpha(alpha)
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def spawn_purbook(purbook_x, purbook_y):
    global sncount
    
    if sncount + 1 >= 14:
        sncount = 0
    
    win.blit(purbook[sncount], (purbook_x, purbook_y))
    sncount += 1

def spawn_bluebook(bluebook_x, bluebook_y):
    global bluebook1count

    if bluebook1count + 1 >= 14:
        bluebook1count = 0
        
    win.blit(bluebook[bluebook1count], (bluebook_x, bluebook_y))
    bluebook1count += 1
    
def spawn_bluebook2(bluebook_x2, bluebook_y2):
    global bluebook2count

    if bluebook2count + 1 >= 14:
        bluebook2count = 0
        
    win.blit(bluebook[bluebook2count], (bluebook_x2, bluebook_y2))
    bluebook2count += 1

def spawn_bluebook3(bluebook_x3, bluebook_y3):
    global bluebook3count
    
    if bluebook3count + 1 >= 14:
        bluebook3count = 0
        
    win.blit(bluebook[bluebook3count], (bluebook_x3, bluebook_y3))
    bluebook3count += 1

def spawn_redbook(redbook_x, redbook_y):
    global redbook1count
    
    if redbook1count + 1 >= 14:
        redbook1count = 0
        
    win.blit(redbook[redbook1count], (redbook_x, redbook_y))
    redbook1count += 1

def spawn_redbook2(redbook_x2, redbook_y2):
    global redbook2count
    
    if redbook2count + 1 >= 14:
        redbook2count = 0
        
    win.blit(redbook[redbook2count], (redbook_x2, redbook_y2))
    redbook2count += 1
    
def spawn_redbook3(redbook_x3, redbook_y3):
    global redbook3count
    
    if redbook3count + 1 >= 14:
        redbook3count = 0
        
    win.blit(redbook[redbook3count], (redbook_x3, redbook_y3))
    redbook3count += 1

def spawn_redbook4(redbook_x4, redbook_y4):
    global redbook4count
    
    if redbook4count + 1 >= 14:
        redbook4count = 0
        
    win.blit(redbook[redbook4count], (redbook_x4, redbook_y4))
    redbook4count += 1

def spawn_ghost(ghost_x, ghost_y):
    global ghost1count
    
    if ghost1count + 1 >= 16:
        ghost1count = 0
        
    win.blit(ghost[ghost1count], (ghost_x, ghost_y))
    ghost1count += 1

def spawn_ghost2(ghost_x2, ghost_y2):
    global ghost2count
    
    if ghost2count + 1 >= 16:
        ghost2count = 0
        
    win.blit(ghost[ghost2count], (ghost_x2, ghost_y2))
    ghost2count += 1

def spawn_bbubl(bbubl_x, bbubl_y):
    global bbubl1count
    
    if bbubl1count + 1 >= 15:
        bbubl1count = 0
        
    win.blit(bbubl[bbubl1count], (bbubl_x, bbubl_y))
    bbubl1count += 1
       
def spawn_bbubl2(bbubl_x2, bbubl_y2):
    global bbubl2count
    
    if bbubl2count + 1 >= 15:
        bbubl2count = 0
        
    win.blit(bbubl[bbubl2count], (bbubl_x2, bbubl_y2))
    bbubl2count += 1

def spawn_bbubl3(bbubl_x3, bbubl_y3):
    global bbubl3count
    
    if bbubl3count + 1 >= 15:
        bbubl3count = 0
        
    win.blit(bbubl[bbubl3count], (bbubl_x3, bbubl_y3))
    bbubl3count += 1

def spawn_rbubl(rbubl_x, rbubl_y):
    global rbubl1count
    
    if rbubl1count + 1 >= 14:
        rbubl1count = 0
        
    win.blit(rbubl[rbubl1count], (rbubl_x, rbubl_y))
    rbubl1count += 1
    
def spawn_rbubl2(rbubl_x2, rbubl_y2):
    global rbubl2count
    
    if rbubl2count + 1 >= 14:
        rbubl2count = 0
        
    win.blit(rbubl[rbubl2count], (rbubl_x2, rbubl_y2))
    rbubl2count += 1

def spawn_poisonbot(poisonbot_x, poisonbot_y):
    global poisonbotcount
    
    if poisonbotcount + 1 >= 24:
        poisonbotcount = 0
        
    win.blit(poisonbot[poisonbotcount], (poisonbot_x, poisonbot_y))
    poisonbotcount += 1

def spawn_broom(broom_x, broom_y):
    global broom1count
    
    if broom1count + 1 >= 16:
        broom1count = 0
        
    win.blit(broom[broom1count], (broom_x, broom_y))
    broom1count += 1

def spawn_broom2(broom_x2, broom_y2):
    global broom2count
    
    if broom2count + 1 >= 16:
        broom2count = 0
        
    win.blit(broom[broom2count], (broom_x2, broom_y2))
    broom2count += 1

def spawn_broom3(broom_x3, broom_y3):
    global broom3count
    
    if broom3count + 1 >= 16:
        broom3count = 0
        
    win.blit(broom[broom3count], (broom_x3, broom_y3))
    broom3count += 1

def spawn_pump(pump_x, pump_y):
    global pumpcount
    
    if pumpcount + 1 >= 4:
        pumpcount = 0
        
    win.blit(pump[pumpcount], (pump_x, pump_y))
    pumpcount += 1

def spawn_onefairy(onefairy_x, onefairy_y):
    global onefairy1count
    
    if onefairy1count + 1 >= 25:
        onefairy1count = 0
        
    win.blit(onefairy[onefairy1count], (onefairy_x, onefairy_y))
    onefairy1count += 1

def spawn_onefairy2(onefairy_x2, onefairy_y2):
    global onefairy2count
    
    if onefairy2count + 1 >= 25:
        onefairy2count = 0
        
    win.blit(onefairy[onefairy2count], (onefairy_x2, onefairy_y2))
    onefairy2count += 1

def spawn_twofairy(twofairy_x, twofairy_y):
    global twofairy1count
    
    if twofairy1count + 1 >= 18:
        twofairy1count = 0
        
    win.blit(twofairy[twofairy1count], (twofairy_x, twofairy_y))
    twofairy1count += 1
    
def spawn_twofairy2(twofairy_x2, twofairy_y2):
    global twofairy2count
    
    if twofairy2count + 1 >= 18:
        twofairy2count = 0
        
    win.blit(twofairy[twofairy2count], (twofairy_x2, twofairy_y2))
    twofairy2count += 1
    
def spawn_spider(spider_x, spider_y):
    global spidercount
    
    if spidercount + 1 >= 16:
        spidercount = 0
        
    win.blit(spider[spidercount], (spider_x, spider_y))
    spidercount += 1
   
def spawn_bat(bat_x, bat_y):
    global bat1count
    
    if bat1count + 1 >= 16:
        bat1count = 0
        
    win.blit(bat[bat1count], (bat_x, bat_y))
    bat1count += 1
    
def spawn_bat2(bat_x2, bat_y2):
    global bat2count
    
    if bat2count + 1 >= 16:
        bat2count = 0
        
    win.blit(bat[bat2count], (bat_x2, bat_y2))
    bat2count += 1
    
def spawn_bat3(bat_x3, bat_y3):
    global bat3count
    
    if bat3count + 1 >= 16:
        bat3count = 0
        
    win.blit(bat[bat3count], (bat_x3, bat_y3))
    bat3count += 1
 
def spawn_bird(bird_x, bird_y):
    global bird1count
    
    if bird1count + 1 >= 18:
        bird1count = 0
        
    win.blit(bird[bird1count], (bird_x, bird_y))
    bird1count += 1

def spawn_bird2(bird_x2, bird_y2):
    global bird2count
    
    if bird2count + 1 >= 18:
        bird2count = 0
        
    win.blit(bird[bird2count], (bird_x2, bird_y2))
    bird2count += 1
    
def spawn_bird3(bird_x3, bird_y3):
    global bird3count
    
    if bird3count + 1 >= 18:
        bird3count = 0
        
    win.blit(bird[bird3count], (bird_x3, bird_y3))
    bird3count += 1

def spawn_clock(clock_x, clock_y):
    global clockcount
    
    if clockcount + 1 >= 16:
        clockcount = 0
        
    win.blit(clock[clockcount], (clock_x, clock_y))
    clockcount += 1

def readvar(file, string):
    """readline variable"""
    f, mylist = open(file, 'r'), []
    while True:
        s = f.readline()
        if s == '':
            break
        d = s.split()
        if d[0].count(string) == 1:
            mylist.append(pygame.image.load(d[0]))
    return mylist

walkright, nowalk = readvar('front.txt', 'racing/broom'), readvar('front.txt', 'racing/broom')
heartimg = pygame.image.load('sprite/racing/broom/heart.png')

bbubl, rbubl = readvar('stage 1.txt', 'clocktower/bbubl'), readvar('stage 1.txt', 'clocktower/rbubl')
clock = readvar('stage 1.txt', 'clocktower/clock')
poisonbot, ghost = readvar('stage 1.txt', 'clocktower/poison'), readvar('stage 1.txt', 'clocktower/ghost')

onefairy, twofairy = readvar('stage 2.txt', 'onefairy'), readvar('stage 2.txt', 'twofairy')
broom, pump = readvar('stage 2.txt', 'broom'), readvar('stage 2.txt', 'pump')
spider, bat, bird = readvar('stage 2.txt', 'spider'), readvar('stage 2.txt', 'bat'), readvar('stage 2.txt', 'bird')

bluebook, purbook, redbook = readvar('stage 3.txt', 'bluebook'), readvar('stage 3.txt', 'purbook'), readvar('stage 3.txt', 'redbook')

#----------------------------------------------------------- stage 1 หอนาฬิกา ----------------------------------------------------------------

bbubl_x = 1280
bbubl_x2 = 1280
bbubl_x3 = 1280
bbubl_y = 525
bbubl_y2 = 350
bbubl_y3 = 450

rbubl_x = 1280
rbubl_x2 = 1280
rbubl_y = 160
rbubl_y2 = 220

clock_x = 1280
clock_y = 360
# ------------------------------------------------------------------------------------------------------------------------------
bluebook_x = 1280
bluebook_x2 = 1280
bluebook_x3 = 1280
bluebook_y2 = 100
bluebook_y3 = 180
bluebook_y = 260

redbook_x = 1280
redbook_x2 = 1280
redbook_x3 = 1280
redbook_x4 = 1280
redbook_y = 400
redbook_y2 = 480
redbook_y3 = 560
redbook_y4 = 640

purbook_x = 1280
purbook_y = 360

# -------------------------------------------------------------------------------------------------------------------------------
poisonbot_x = 1280
poisonbot_y = 280
pass_poison_x = False
pass_poison_y = False

ghost_x = 1280
ghost_x2 = 1280
ghost_y = 500
ghost_y2 = 150

onefairy_x = 1280
onefairy_x2 = 1280
onefairy_y = 340
onefairy_y2 = 480

twofairy_x = 1280
twofairy_x2 = 1280
twofairy_y = 400
twofairy_y2 = 600

broom_x = 1280
broom_x2 = 1280
broom_x3 = 1280
broom_y = 460
broom_y2 = 500
broom_y3 = 530

pump_x = 500
pump_y = 0

spider_x = 670
spider_y = 0

bat_x = 1280
bat_x2 = 1280
bat_x3 = 1280
bat_y = 150
bat_y2 = 200
bat_y3 = 250

bird_x = 1280
bird_x2 = 1280
bird_x3 = 1280
bird_y = 140
bird_y2 = 190
bird_y3 = 240

#-----------------music-------------------------------
# music = pygame.mixer.Sound("testbg.mp3")
# crash = pygame.mixer.Sound("Crash1_.mp3")
#-----------------------------------------------------------------
x = 50
y = 355
vel = 30
left = False
right = False
walkcount = 0
check = ''
mate = 0
bestscore = 0
heart = 5
cooldown = 0

speed_slow = 7
speed_12 = 12
speed_low = 15
speed_mid = 20
speed_mid25 = 25
speed_high = 30

fadebg2 = False
fadebg3 = False
fadebg4 = False
# ----------------------------------------------------- 1 หอนาฬิกา --------------------------------------
bbubl1count, bbubl1_show = 0, False
bbubl2count, bbubl2_show = 0, False
bbubl3count, bbubl3_show = 0, False
rbubl1count, rbubl1_show = 0, False
rbubl2count, rbubl2_show = 0, False
clockcount, clock_show = 0, False
ghost1count, ghost1_show = 0, False
ghost2count, ghost2_show = 0, False
poisonbotcount, poisonbot_show = 0, False
# -------------------------------------------------------- 2 ป่า --------------------------------------

onefairy1count, onefairy1_show = 0, False
onefairy2count, onefairy2_show = 0, False
twofairy1count, twofairy1_show = 0, False
twofairy2count, twofairy2_show = 0, False

broom1count, broom1_show = 0, False
broom2count, broom2_show = 0, False
broom3count, broom3_show = 0, False
pumpcount, pump_show = 0, False
spidercount, spider_show = 0, False

bat1count, bat1_show = 0, False
bat2count, bat2_show = 0, False
bat3count, bat3_show = 0, False
bird1count, bird1_show = 0, False
bird2count, bird2_show = 0, False
bird3count, bird3_show = 0, False

# ----------------------------------------------------- 3 ห้องสมุด --------------------------------------
sncount, purbook_show = 0, False
bluebook1count, bluebook1_show = 0, False
bluebook2count, bluebook2_show = 0, False
bluebook3count, bluebook3_show = 0, False
redbook1count, redbook1_show = 0, False
redbook2count, redbook2_show = 0, False
redbook3count, redbook3_show = 0, False
redbook4count, redbook4_show = 0, False

# pygame.mixer.Sound.play(music)
run = True
while run:
    pygame.time.delay(30)
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif keys[pygame.K_ESCAPE]:
            run = False

    if heart <= 0:
        if bestscore <= int(mate):
            bestscore = int(mate)
    bg_scrolling -= 1
    
    if mate >= 180:
        if fadebg4 == False:
            fadescreen()
            fadebg4 = True
        win.blit(bg4, (bg_scrolling, 0))
        win.blit(bg4, (bg_scrolling+1280, 0))
    
    elif mate >= 120:
        if fadebg3 == False:
            fadescreen()
            fadebg3 = True
        win.blit(bg3, (bg_scrolling, 0))
        win.blit(bg3, (bg_scrolling+1280, 0))
    
    elif mate >= 60:
        if fadebg2 == False:
            fadescreen()
            fadebg2 = True
        win.blit(bg2, (bg_scrolling, 0))
        win.blit(bg2, (bg_scrolling+1280, 0))

    elif mate >= 0:
        win.blit(bg, (bg_scrolling, 0))
        win.blit(bg, (bg_scrolling+1280, 0))
    if bg_scrolling <= -1280:
        bg_scrolling = 0
    mate += 0.05
    # y += 5
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        print(mx, my)
    # print(x, y)
    
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and x > 10:
        x -= vel
        left = True
        right = False
        check = 'LEFT'
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT] and x < bg_wildth-150:
        x += vel
        right = True
        left = False
        check = 'RIGHT'
    # elif keys[pygame.K_SPACE] and y >= 0:
    #     y -= vel
    elif keys[pygame.K_w] or keys[pygame.K_UP] and y > 5:
        y -= vel
        right = True
        left = False
        check = 'RIGHT'
    elif keys[pygame.K_s] or keys[pygame.K_DOWN] and y < bg_height-250:
        y += vel
        right = True
        left = False
        check = 'RIGHT'
    else:
        right = False
        left = False

#---------------------------------------------------- stage1 หอนาฬิกา [1 - 60] -------------------------------------------------------------------------

    if 7 <= mate <= 11.5 or 18 <= mate <= 22.5 or 31 <= mate <= 35.5 or 38 <= mate <= 42.5:
        rbubl1_show = True
        rbubl_x -= speed_low
        spawn_rbubl(rbubl_x, rbubl_y)
        if rbubl_x <= -10 and rbubl1_show:
            rbubl_x = 1350
            rbubl1_show = False

    if 17 <= mate <= 21.5 or 42 <= mate <= 46.5 or 53 <= mate <= 57.5:
        rbubl2_show = True
        rbubl_x2 -= speed_low
        spawn_rbubl2(rbubl_x2, rbubl_y2)
        if rbubl_x2 <= -10 and rbubl2_show:
            rbubl_x2 = 1350
            rbubl2_show = False

    if 10.5 <= mate <= 15 or 31 <= mate <= 35.5 or 48 <= mate <= 52.5:
        bbubl1_show = True
        bbubl_x -= speed_low
        spawn_bbubl(bbubl_x, bbubl_y)
        if bbubl_x <= -10 and bbubl1_show:
            bbubl_x = 1350
            bbubl1_show = False        
            
    if 13 <= mate <= 15.7 or 22 <= mate <= 24.7 or 35 <= mate <= 37.7:
        ghost2_show = True
        ghost_x2 -= speed_mid25
        spawn_ghost2(ghost_x2, ghost_y2)
        if ghost_x2 <= -10 and ghost2_show:
            ghost_x2 = 1350
            ghost2_show = False
    
    if 25 <= mate <= 29.5 or 33 <= mate <= 37.4 or 46 <= mate <= 50.5:
        bbubl2_show = True
        bbubl_x2 -= speed_low
        spawn_bbubl2(bbubl_x2, bbubl_y2)
        if bbubl_x2 <= -10 and bbubl2_show:
            bbubl_x2 = 1350
            bbubl2_show = False
            
    if 27 <= mate <= 29.7 or 41 <= mate <= 43.7 or 48 <= mate <= 50.7:
        bbubl3_show = True
        bbubl_x3 -= speed_mid25
        spawn_bbubl3(bbubl_x3, bbubl_y3)
        if bbubl_x3 <= -10 and bbubl3_show:
            bbubl_x3 = 1350   
            bbubl3_show = False
                 
    if 20 <= mate <= 22.2:
        ghost1_show = True
        ghost_x -= speed_high
        spawn_ghost(ghost_x, ghost_y)
        if ghost_x <= -10 and ghost1_show:
            ghost_x = 1350
            ghost1_show = False

    if  55 <= mate <= 59.3: 
        poisonbot_show = True
        poisonbot_x -= speed_low
        spawn_poisonbot(poisonbot_x, poisonbot_y)
        if (poisonbot_x <= -10 or poisonbot_y <= -10) and poisonbot_show:
            poisonbot_x = 1280
            poisonbot_show = False

        if pass_poison_y == True:
            poisonbot_y -= speed_low
        else:
            poisonbot_y += speed_low
        if poisonbot_y >= 720:
            pass_poison_y = True
        # elif poisonbot_y <= 0:
        #     pass_poison_y = False
        
    # 5 16 39 52
    if 16 <= mate <= 19.2 or 39 <= mate <= 42.2 or 52 <= mate <= 55.2:
        clock_show = True
        clock_x -= speed_mid
        spawn_clock(clock_x, clock_y)
        if clock_x <= -10 and clock_show:
            clock_x = 1280
            clock_show = False
#------------------------------------------------------- stage 2 ป่า [61 - 120] ------------------------------------------------

    if 68 <= mate <= 72.5 or  84 <= mate <= 88.5 or 104.5 <= mate <= 109:
        bird1_show = True
        bird_x -= speed_low
        spawn_bird(bird_x, bird_y)
        if bird_x <= -10 and bird1_show:
            bird_x = 1350
            bird1_show = False
    
    if 68.5 <= mate <= 73 or 84.5 <= mate <= 89 or 105 <= mate <= 109.5:
        bird2_show = True
        bird_x2 -= speed_low
        spawn_bird2(bird_x2, bird_y2)
        if bird_x2 <= -10 and bird2_show:
            bird_x2 = 1350
            bird2_show = False
    
    if 71 <= mate <= 75.5 or 105.5 <= mate <= 110 or 111.5 <= mate <= 116:
        bird3_show = True
        bird_x3 -= speed_low
        spawn_bird3(bird_x3, bird_y3)
        if bird_x3 <= -10 and bird3_show:
            bird_x3 = 1350
            bird3_show = False
    
    if 74.6 <= mate <= 79.7 or 89 <= mate <= 94.1:
        spider_show = True
        spider_y += speed_slow
        spawn_spider(spider_x, spider_y)
        if spider_y >= 730 and spider_show:
            spider_y = 0
            spider_show = False

    if 82 <= mate <= 84.4 or 89 <= mate <= 91.4  or 96 <= mate <= 98.4 or 107.6 <= mate <= 110:
        pump_show = True
        pump_y += speed_low
        spawn_pump(pump_x, pump_y)
        if pump_y >= 730 and pump_show:
            pump_y = 0
            pump_show = False
    
    if 80 <= mate <= 83.2 or 96 <= mate <= 99.3:
        bat1_show = True
        bat_x -= speed_mid
        spawn_bat(bat_x, bat_y)
        if bat_x <= -10 and bat1_show:
            bat_x = 1350
            bat1_show = False
            
    if 83.8 <= mate <= 87:
        bat2_show = True
        bat_x -= speed_mid25
        spawn_bat2(bat_x2, bat_y2)
        if bat_x2 <= -10 and bat2_show:
            bat_x2 = 1350
            bat2_show = False

    if 98 <= mate <= 102.5:
        onefairy1_show = True
        onefairy_x -= speed_low
        spawn_onefairy(onefairy_x, onefairy_y)
        if onefairy_x <= -10 and onefairy1_show:
            onefairy_x = 1350
            onefairy1_show = False
            
    if 75 <= mate <= 79.5 or 94.5 <= mate <= 99:
        onefairy2_show = True
        onefairy_x2 -= speed_low
        spawn_onefairy2(onefairy_x2, onefairy_y2)
        if onefairy_x2 <= -10 and onefairy2_show:
            onefairy_x2 = 1350
            onefairy2_show = False

    if 80 <= mate <= 89.5 or 107.5 <= mate <= 117:
        twofairy_show = True
        twofairy_x -= speed_slow
        spawn_twofairy(twofairy_x, twofairy_y)
        if twofairy_x <= -10 and twofairy1_show:
            twofairy_x = 1350
            twofairy1_show = False
            
    if 69.5 <= mate <= 79 or 88 <= mate <= 97.5:
        twofairy2_show = True
        twofairy_x2 -= speed_slow
        spawn_twofairy2(twofairy_x2, twofairy_y2)
        if twofairy_x2 <= -10 and twofairy2_show:
            twofairy_x2 = 1350
            twofairy2_show = False
    
    if 94 <= mate <= 97.2 or 105 <= mate <= 108.2 :
        broom2_show = True
        broom_x2 -= speed_mid
        spawn_broom2(broom_x2, broom_y2)
        if broom_x2 <= -10 and broom2_show:    
            broom_x2 = 1300 
            broom2_show = False      
            
    if 70 <= mate <= 73.2 or 90 <= mate <= 93.2 or 110 <= mate <= 113.2:
        broom3_show = True
        broom_x3 -= speed_mid
        spawn_broom3(broom_x3, broom_y3)
        if broom_x3 <= -10 and broom3_show:    
            broom_x3 = 1300
            broom3_show = False

#------------------------------------------------------ stage 3 ห้องสมุด [121 - 180] -----------------------------------------------------
    
    if 129 <= mate <= 133.5 or 134 <= mate <= 138.5 or 145.5 <= mate <= 150 or 152 <= mate <= 156.5 or 162.5 <= mate <= 167 or 167.5 <= mate <= 172 or 172.5 <= mate <= 177:
        bluebook2_show = True
        bluebook_x2 -= speed_low
        spawn_bluebook2(bluebook_x2, bluebook_y2)
        if bluebook_x2 <= -10 and bluebook2_show:
            bluebook_x2 = 1350
            bluebook2_show = False
            
    if 130 <= mate <= 134.5 or 135 <= mate <= 139.5 or 145 <= mate <= 149.5 or 154.5 <= mate <= 159 or 162 <= mate <= 166.5 or 168.5 <= mate <= 173 or 173.5 <= mate <= 178:
        bluebook3_show = True
        bluebook_x3 -= speed_low
        spawn_bluebook3(bluebook_x3, bluebook_y3)
        if bluebook_x3 <= -10 and bluebook3_show:
            bluebook_x3 = 1350
            bluebook3_show = False
     
     # speed_mid (3.2)
    if 133 <= mate <= 136.2 or 149.8 <= mate <= 153 or 154.9 <= mate <= 158 or 164.9 <= mate <= 168:
        bluebook1_show = True
        bluebook_x -= speed_mid
        spawn_bluebook(bluebook_x, bluebook_y)
        if bluebook_x <= -10 and bluebook1_show:
            bluebook_x = 1300
            bluebook1_show = False

    if 165 <= mate <= 168.2 or 156 <= mate <= 159.2:
        purbook_show = True
        purbook_x += speed_mid
        spawn_purbook(purbook_x, purbook_y)
        if purbook_x >= 1300 and purbook_show:
            purbook_x = 0
            purbook_show = False
            
    if 143 <= mate <= 147.5 or 159 <= mate <= 163.5 or 164 <= mate <= 168.5:
        redbook1_show = True
        redbook_x -= speed_low
        spawn_redbook(redbook_x, redbook_y)
        if redbook_x <= -10 and redbook1_show:
            redbook_x = 1350
            redbook1_show = False
            
    if 126 <= mate <= 130.5 or 132 <= mate <= 136.5 or 149 <= mate <= 143.5 or 145.5 <= mate <= 150 or 151.5 <= mate <= 156:
        redbook2_show = True
        redbook_x2 -= speed_low
        spawn_redbook2(redbook_x2, redbook_y2)
        if redbook_x2 <= -10 and redbook2_show:
            redbook_x2 = 1350
            redbook2_show = False
            
    if 125.5 <= mate <= 130 or 139 <= mate <= 143.5 or 144 <= mate <= 148.5 or 149 <= mate <= 153.5 or 155.5 <= mate <= 160:
        redbook3_show = True
        redbook_x3 -= speed_low
        spawn_redbook3(redbook_x3, redbook_y3)
        if redbook_x3 <= -10 and redbook3_show:
            redbook_x3 = 1350
            redbook3_show = False
            
    if 127 <= mate <= 132.5 or 137 <= mate <= 142.5 or 152 <= mate <= 157.5:
        redbook4_show = True
        redbook_x4 -= speed_12
        spawn_redbook4(redbook_x4, redbook_y4)
        if redbook_x4 <= -10 and redbook4_show:
            redbook_x4 = 1350
            redbook4_show = False
            

    if  121 <= mate <= 180:
        poisonbot_show = True
        spawn_poisonbot(poisonbot_x, poisonbot_y)
        if poisonbot_x < 0:
            pass_poison_x = True
        elif poisonbot_x > 1200:
            pass_poison_x = False

        if poisonbot_y <= -10:
            pass_poison_y = True
        elif poisonbot_y > 620:
            pass_poison_y = False

        if poisonbot_x < 0 or pass_poison_x == True:
            poisonbot_x += speed_low
        else:
            poisonbot_x -= speed_low
        if poisonbot_y < 0 or pass_poison_y == True:
            poisonbot_y += speed_low
        else:
            poisonbot_y -= speed_low

    cooldown += 0.05
    
#------------------------------------ เช็คชน --------------------------- 175 165
    if ((x <= purbook_x+120 <= x+175 and y <= purbook_y+70 <= x+165 and purbook_show) or \
        (x <= bluebook_x+110 <= x+175 and y <= bluebook_y+70 <= x+165 and bluebook1_show) or \
        (x <= bluebook_x2+110 <= x+175 and y <= bluebook_y2+70 <= x+165 and bluebook2_show) or \
        (x <= bluebook_x3+110 <= x+175 and y <= bluebook_y3+70 <= x+165 and bluebook3_show) or \
        (x <= redbook_x+115 <= x+175 and y <= redbook_y+60 <= x+165 and redbook1_show) or \
        (x <= redbook_x2+115 <= x+175 and y <= redbook_y2+60 <= x+165 and redbook2_show) or \
        (x <= redbook_x3+115 <= x+175 and y <= redbook_y3+60 <= x+165 and redbook3_show) or \
        (x <= redbook_x4+115 <= x+175 and y <= redbook_y4+60 <= x+165 and redbook4_show) or \
        (x <= ghost_x+80 <= x+175 and y <= ghost_y+60 <= x+165 and ghost1_show) or \
        (x <= ghost_x2+80 <= x+175 and y <= ghost_y2+90 <= x+165 and ghost2_show) or \
        (x <= bbubl_x+125 <= x+175 and y <= bbubl_y+40 <= x+165 and bbubl1_show) or \
        (x <= bbubl_x2+125 <= x+175 and y <= bbubl_y2+40 <= x+165 and bbubl2_show) or \
        (x <= bbubl_x3+125 <= x+175 and y <= bbubl_y3+40 <= x+165 and bbubl3_show) or \
        (x <= rbubl_x+100 <= x+175 and y <= rbubl_y+30 <= x+165 and rbubl1_show) or \
        (x <= rbubl_x2+100 <= x+175 and y <= rbubl_y2+30 <= x+165 and rbubl2_show) or \
        (x <= poisonbot_x+100 <= x+175 and y <= poisonbot_y+110 <= x+165 and poisonbot_show) or \
        (x <= broom_x+140 <= x+175 and y <= broom_y+70 <= x+165 and broom1_show) or \
        (x <= broom_x2+140 <= x+175 and y <= broom_y2+70 <= x+165 and broom2_show) or \
        (x <= broom_x3+140 <= x+175 and y <= broom_y3+70 <= x+165 and broom3_show) or \
        (x <= pump_x+45 <= x+175 and y <= pump_y+45 <= x+165 and pump_show) or \
        (x <= onefairy_x+80 <= x+175 and y <= onefairy_y+80 <= x+165 and onefairy1_show) or \
        (x <= onefairy_x2+80 <= x+175 and y <= onefairy_y2+80 <= x+165 and onefairy2_show) or \
        (x <= twofairy_x+80 <= x+175 and y <= twofairy_y+80 <= x+165 and twofairy1_show) or \
        (x <= twofairy_x2+80 <= x+175 and y <= twofairy_y2+80 <= x+165 and twofairy2_show) or \
        (x <= spider_x+50 <= x+175 and y <= spider_y+85 <= x+165 and spider_show) or \
        (x <= bat_x+40 <= x+175 and y <= bat_y+50 <= x+165 and bat1_show) or \
        (x <= bat_x2+40 <= x+175 and y <= bat_y2+50 <= x+165 and bat2_show) or \
        (x <= bat_x3+40 <= x+175 and y <= bat_y3+50 <= x+165 and bat3_show) or \
        (x <= bird_x+60 <= x+175 and y <= bird_y+55 <= x+165 and bird1_show) or \
        (x <= bird_x2+60 <= x+175 and y <= bird_y2+55 <= x+165 and bird2_show) or \
        (x <= bird_x3+60 <= x+175 and y <= bird_y3+55 <= x+165 and bird3_show) or \
        (x <= clock_x+45 <= x+175 and y <= clock_y+65 <= x+165 and clock_show)) and int(cooldown) > 2:
        heart -= 1
        cooldown = 0
    
    #     pygame.mixer.Sound.play(crash)
    
    if heart == 5:
        win.blit(heartimg, (920, 25))
        win.blit(heartimg, (985, 25))
        win.blit(heartimg, (1050, 25))
        win.blit(heartimg, (1115, 25))
        win.blit(heartimg, (1180, 25))        
    if heart == 4:
        win.blit(heartimg, (985, 25))
        win.blit(heartimg, (1050, 25))
        win.blit(heartimg, (1115, 25))
        win.blit(heartimg, (1180, 25))
    if heart == 3:
        win.blit(heartimg, (1050, 25))
        win.blit(heartimg, (1115, 25))
        win.blit(heartimg, (1180, 25))
    if heart == 2:
        win.blit(heartimg, (1115, 25))
        win.blit(heartimg, (1180, 25))
    if heart == 1:
        win.blit(heartimg, (1180, 25))    
    win.blit(FONT.render("Score : "+str(int(mate)), True, (255,255,255)), (20,20))
    # win.blit(FONT.render("Heart : "+ "<3"*(int(heart)), True, (255,255,255)), (900,20))
    redrawGameWindow()

pygame.quit()
