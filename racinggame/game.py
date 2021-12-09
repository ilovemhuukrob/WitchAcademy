import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
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
    # elif left:
    #     win.blit(walkright[walkcount], (x, y))
    #     walkcount += 1
        
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

# crash = 0
# moncount = 0
# def spawn(monster, posx, posy):
#     global moncount
#     global crash
#     global x
#     global y
#     global heart

#     if moncount + 1 >= len(monster):
#         moncount = 0
#     wmon, hmon = monster[moncount].get_rect().size
#     print(wmon, hmon)
#     if posy-180 < y < posy-10 and posx-100 < x < posx-50:
#         crash += 1/3
#     if crash >= 1:
#         heart -= 1
#         crash = 0

#     win.blit(monster[moncount], (posx, posy))
#     moncount += 1


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

class mon:
    def __init__(self, posx, posy, monster):
        self.posx = posx
        self.posy = posy
        self.monster = monster
        self.moncount = 0
        self.crash = 0
        self.pas = False

    def spawn(self, sec, speedx, speedy, bounce=False):
        global x
        global y
        global heart
        global cooldown
        global hplay
        global wplay


        if time >= sec:

            if self.moncount + 1 >= len(self.monster):
                self.moncount = 0
            wmon, hmon = self.monster[self.moncount].get_rect().size
            # print(wmon, hmon)
            if y < self.posy < y+hplay-80 and x < self.posx < x+wplay-80 and cooldown > 2:
                heart -= 1
                cooldown = 0
            # if self.posy-180 < y < self.posy-10 and self.posx-100 < x < self.posx-50 and cooldown > 2:
            #     heart -= 1
            #     cooldown = 0

            win.blit(self.monster[self.moncount], (self.posx, self.posy))
            self.moncount += 1


            if bounce:
                if self.posy <= 0:
                    self.pas = True
                elif self.posy > 720:
                    self.pas = False
                if self.posy < 0 or self.pas:
                    self.posy += speedy
                else:
                    self.posy -= speedy
                self.posx -= speedx
            else:
                self.posx -= speedx
                self.posy += speedy


walkright, nowalk = readvar('front.txt', 'racing/broom'), readvar('front.txt', 'racing/broom')


heartimg = pygame.image.load('sprite/racing/broom/heart.png')

bbubl, rbubl = readvar('stage 1.txt', 'clocktower/bbubl'), readvar('stage 1.txt', 'clocktower/rbubl')
clock = readvar('stage 1.txt', 'clocktower/clock')
poisonbot, ghost = readvar('stage 1.txt', 'clocktower/poison'), readvar('stage 1.txt', 'clocktower/ghost')

onefairy, twofairy = readvar('stage 2.txt', 'onefairy'), readvar('stage 2.txt', 'twofairy')
broom, pump = readvar('stage 2.txt', 'broom'), readvar('stage 2.txt', 'pump')
spider, bat, bird = readvar('stage 2.txt', 'spider'), readvar('stage 2.txt', 'bat'), readvar('stage 2.txt', 'bird')

bluebook, purbook, redbook = readvar('stage 3.txt', 'bluebook'), readvar('stage 3.txt', 'purbook'), readvar('stage 3.txt', 'redbook')

#----------------------------------------------------------- stage 1 ----------------------------------------------------------------
bird1 = mon(1280,320,bird); bird8 = mon(1280,190,bird); bird15 = mon(1280,90,bird); bird22 = mon(1280,290,bird)
bird2 = mon(1280,100,bird); bird9 = mon(1280,290,bird); bird16 = mon(1280,450,bird)
bird3 = mon(1280,500,bird); bird10 = mon(1280,480,bird); bird17 = mon(1280,310,bird)
bird4 = mon(1280,450,bird); bird11 = mon(1280,310,bird); bird18 = mon(1280,70,bird)
bird5 = mon(1280,350,bird); bird12 = mon(1280,310,bird); bird19 = mon(1280,150,bird)
bird6 = mon(1280,100,bird); bird13 = mon(1280,310,bird); bird20 = mon(1280,500,bird)
bird7 = mon(1280,400,bird); bird14 = mon(1280,20,bird); bird21 = mon(1280,70,bird)
#--------------------------------------------------------- bounce ------------------------------------------------------------
bird_1b = mon(1280,0,bird)
bird_2b = mon(1280,720,bird)
bird_3b = mon(1280,0,bird)
bird_4b = mon(1280,720,bird)
bird_5b = mon(1280,0,bird)
#--------------------------------------------------------- disco ------------------------------------------------------------
bird01 = mon(1280,10,bird)
bird02 = mon(1280,610,bird)
bird03 = mon(1280,310,bird)
bird04 = mon(1280,90,bird)
bird05 = mon(1280,10,bird)
bird06 = mon(1280,10,bird)
bird07 = mon(1280,80,bird)
bird08 = mon(1280,610,bird)
bird09 = mon(1280,90,bird)
#----------------------------------------------------------- stage 2 ----------------------------------------------------------------
clock1 = mon(1280,310,clock)
clock2 = mon(1280,220,clock)
clock3 = mon(1280,70,clock)
clock4 = mon(1280,160,clock)
clock5 = mon(1280,370,clock)
clock6 = mon(1280,600,clock)
clock7 = mon(1280,130,clock)
clock8 = mon(1280,130,clock)
clock9 = mon(1280,340,clock)
clock10 = mon(1280,250,clock)
clock11 = mon(1280,438,clock)
clock12 = mon(1280,50,clock)
clock13 = mon(1280,150,clock)

clock14 = mon(1280,310,clock)
clock15 = mon(1280,600,clock)
clock16 = mon(1280,510,clock)
clock17 = mon(1280,84,clock)
clock18 = mon(1280,182,clock)

clock19 = mon(70,720,clock)
clock20 = mon(1190,0,clock)
clock21 = mon(70,720,clock)
clock22 = mon(1190,0,clock)
clock23 = mon(70,720,clock)
clock24 = mon(1190,0,clock)
clock25 = mon(70,720,clock)
clock26 = mon(1190,0,clock)

clock27 = mon(1280,26,clock)
clock28 = mon(1280,639,clock)
clock29 = mon(1280,0,clock)
#--------------------------------------------------------- bounce ------------------------------------------------------------
clock1b = mon(1280,0,clock)
clock2b = mon(1280,720,clock)
clock3b = mon(1280,0,clock)
clock4b = mon(1280,720,clock)
clock5b = mon(1280,0,clock)
clock6b = mon(1280,720,clock)
clock7b = mon(1280,0,clock)
clock8b = mon(1280,720,clock)
clock9b = mon(1280,0,clock)
clock10b = mon(1280,720,clock)

clock11b = mon(1280,0,clock)
clock12b = mon(0,207,clock)
clock13b = mon(1280,234,clock)
clock14b = mon(0,452,clock)
clock15b = mon(1280,310,clock)
clock16b = mon(0,100,clock)
clock17b = mon(1280,720,clock)
clock18b = mon(0,0,clock)
# #--------------------------------------------------------- disco ------------------------------------------------------------
clock01 = mon(1280,386,clock)
clock02 = mon(1280,50,clock)
clock03 = mon(1280,310,clock)
clock04 = mon(1280,40,clock)
clock05 = mon(1280,611,clock)
# ----------------------------------------------------------- stage 3 ----------------------------------------------------------------
bluebook1 = mon(1280, 260, bluebook); bluebook2 = mon(1280, 260, bluebook); bluebook3 = mon(1280, 260, bluebook)
bluebook4 = mon(1280, 260, bluebook); bluebook5 = mon(1280, 260, bluebook); bluebook6 = mon(1280, 260, bluebook)
bluebook7 = mon(1280, 260, bluebook); bluebook8 = mon(1280, 100, bluebook); bluebook9 = mon(1280, 100, bluebook)
bluebook10 = mon(1280, 100, bluebook); bluebook11 = mon(1280, 100, bluebook); bluebook12 = mon(1280, 100, bluebook)
bluebook13 = mon(1280, 100, bluebook); bluebook14 = mon(1280, 100, bluebook); bluebook15 = mon(1280, 180, bluebook)
bluebook16 = mon(1280, 180, bluebook); bluebook17 = mon(1280, 180, bluebook); bluebook18 = mon(1280, 180, bluebook)
redbook1 = mon(1280, 400, redbook); redbook2 = mon(1280, 400, redbook); redbook3 = mon(1280, 400, redbook)
redbook4 = mon(1280, 480, redbook); redbook5 = mon(1280, 480, redbook); redbook6 = mon(1280, 480, redbook)
redbook7 = mon(1280, 480, redbook); redbook8 = mon(1280, 480, redbook); redbook9 = mon(1280, 560, redbook)
redbook10 = mon(1280, 560, redbook); redbook11 = mon(1280, 560, redbook); redbook12 = mon(1280, 560, redbook)
redbook13 = mon(1280, 560, redbook); redbook14 = mon(1280, 640, redbook); redbook15 = mon(1280, 640, redbook); redbook16 = mon(1280, 640, redbook)
purbook1 = mon(-10, 360, purbook); purbook2 = mon(-10, 360, purbook)
# #--------------------------------------------------------- bounce ------------------------------------------------------------
bluebook_1b = mon(1280,0,bluebook)
bluebook_2b = mon(1280,720,bluebook)
bluebook_3b = mon(1280,0,bluebook)
bluebook_4b = mon(1280,720,bluebook)
bluebook_5b = mon(1280,0,bluebook)
bluebook_6b = mon(1280,720,bluebook)
bluebook_7b = mon(1280,0,bluebook)
bluebook_8b = mon(1280,720,bluebook)
bluebook_9b = mon(1280,0,bluebook)
bluebook_10b = mon(1280,720,bluebook)
bluebook_11b = mon(1280,0,bluebook)
bluebook_12b = mon(1280,720,bluebook)
bluebook_13b = mon(1280,0,bluebook)
bluebook_14b = mon(1280,720,bluebook)
bluebook_15b = mon(1280,0,bluebook)
bluebook_16b = mon(1280,720,bluebook)
bluebook_17b = mon(1280,0,bluebook)
bluebook_18b = mon(1280,720,bluebook)
# #--------------------------------------------------------- disco -------------------------------------------------------------
bluebook01 = mon(1280,50,bluebook)
bluebook02 = mon(1280,50,bluebook)
bluebook03 = mon(1280,550,bluebook)
bluebook04 = mon(1280,100,bluebook)
# -------------------------------------------------------------------------------------------------------------------------------


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
time = 0
heart = 5
cooldown = 0

hplay, wplay = walkright[walkcount].get_rect().size

fadebg2 = False
fadebg3 = False
fadebg4 = False

# pygame.mixer.Sound.play(music)
run = True
while run:
    pygame.time.delay(30)
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
        elif keys[pygame.K_ESCAPE]:
            run = False

    bg_scrolling -= 1
    
    if time >= 180:
        if fadebg4 == False:
            fadescreen()
            fadebg4 = True
        win.blit(bg4, (bg_scrolling, 0))
        win.blit(bg4, (bg_scrolling+1280, 0))

    elif time >= 120:
        if fadebg3 == False:
            fadescreen()
            fadebg3 = True
        win.blit(bg3, (bg_scrolling, 0))
        win.blit(bg3, (bg_scrolling+1280, 0))
    
    elif time >= 60:
        if fadebg2 == False:
            fadescreen()
            fadebg2 = True
        win.blit(bg2, (bg_scrolling, 0))
        win.blit(bg2, (bg_scrolling+1280, 0))

    elif time >= 0:
        win.blit(bg, (bg_scrolling, 0))
        win.blit(bg, (bg_scrolling+1280, 0))
    if bg_scrolling <= -1280:
        bg_scrolling = 0
    time += 0.05
    # y += 5

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 10:
        x -= vel
        left = True
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < bg_wildth-150:
        x += vel
        right = True
    elif (keys[pygame.K_w] or keys[pygame.K_UP]) and y > 5:
        y -= vel
        right = True
    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y < bg_height-250:
        y += vel
        right = True
    else:
        right = False

#----------------------------------------------------------- stage 1 ----------------------------------------------------------------
    bird2.spawn(9,7,0); bird9.spawn(22,7,0); bird16.spawn(33,20,0)
    bird3.spawn(10,7,0); bird10.spawn(25,7,0); bird17.spawn(47,15,0)
    bird4.spawn(14,7,0); bird11.spawn(27,7,0)
    bird5.spawn(14.5,7,0); bird12.spawn(29,7,0)
    bird6.spawn(17,7,0); bird13.spawn(33,7,0)
    bird7.spawn(20,7,0); bird14.spawn(33,7,0)
    bird18.spawn(49,12,0)
    bird19.spawn(49,12,0)
    bird20.spawn(49,12,0)
    bird21.spawn(49,12,0)
    bird22.spawn(49,12,0)
#--------------------------------------------------------- bounce ------------------------------------------------------------
    bird_1b.spawn(41,13,20,bounce=True)
    bird_2b.spawn(41,13,20,bounce=True)
    bird_3b.spawn(43,13,20,bounce=True)
    bird_4b.spawn(43,13,20,bounce=True)
    bird_5b.spawn(52,13,20,bounce=True)

#--------------------------------------------------------- disco ------------------------------------------------------------
    bird01.spawn(18,20,0)
    bird02.spawn(20,20,0)
    bird03.spawn(24,20,0)
    bird04.spawn(40,20,0)
    bird05.spawn(25,20,0)
    bird06.spawn(30,20,0)
    bird07.spawn(35,20,0)
    bird08.spawn(29,20,0)
    bird09.spawn(50,20,0)
#----------------------------------------------------------- stage 2 ----------------------------------------------------------------
    clock1.spawn(69,10,0)
    clock2.spawn(69.3,10,0)
    clock3.spawn(72,10,0)
    clock4.spawn(72.3,10,0)
    clock5.spawn(74,10,0)
    clock6.spawn(74,10,0)
    clock7.spawn(75,10,0)
    clock8.spawn(75.3,10,0)
    clock9.spawn(77,10,0)
    clock10.spawn(77.3,10,0)
    clock11.spawn(77.8,10,0)
    clock12.spawn(78,10,0)
    clock13.spawn(78.3,10,0)

    clock14.spawn(87,10,0)
    clock15.spawn(88,10,0)
    clock16.spawn(88.3,10,0)
    clock17.spawn(89,10,0)
    clock18.spawn(89.3,10,0)

    clock19.spawn(96,0,-10)
    clock20.spawn(96,0,10)
    clock21.spawn(100,0,-10)
    clock22.spawn(100,0,10)
    clock23.spawn(104,0,-10)
    clock24.spawn(104,0,10)
    clock25.spawn(108,0,-10)
    clock26.spawn(108,0,10)
#--------------------------------------------------------- bounce ------------------------------------------------------------
    clock1b.spawn(81,20,20,bounce=True)
    clock2b.spawn(81,20,20,bounce=True)
    clock3b.spawn(82,20,20,bounce=True)
    clock4b.spawn(82,20,20,bounce=True)
    clock5b.spawn(83,20,20,bounce=True)
    clock6b.spawn(83,20,20,bounce=True)
    clock7b.spawn(84,20,20,bounce=True)
    clock8b.spawn(84,20,20,bounce=True)
    clock9b.spawn(85,20,20,bounce=True)
    clock10b.spawn(85,20,20,bounce=True)

    clock11b.spawn(97,10,10,bounce=True)
    clock12b.spawn(97,-10,10,bounce=True)
    clock13b.spawn(103,10,10,bounce=True)
    clock14b.spawn(103,-10,10,bounce=True)
    clock15b.spawn(109,10,10,bounce=True)
    clock16b.spawn(109,-10,10,bounce=True)
#--------------------------------------------------------- disco ------------------------------------------------------------
    clock01.spawn(73,20,0)
    clock02.spawn(75,20,0)
    clock03.spawn(78,20,0)
    clock04.spawn(88,20,0)
    clock05.spawn(89,20,0)
#------------------------------------------------------ stage 3 ห้องสมุด [121 - 180] -----------------------------------------------------
    bluebook1.spawn(129, 10, 0); bluebook2.spawn(134, 10, 0); bluebook3.spawn(145, 10, 0)
    bluebook4.spawn(152, 10, 0); bluebook5.spawn(162, 10, 0); bluebook6.spawn(167, 10, 0)
    bluebook7.spawn(172, 10, 0); bluebook8.spawn(130, 10, 0); bluebook9.spawn(135, 10, 0)
    bluebook10.spawn(145, 10, 0); bluebook11.spawn(154, 10, 0); bluebook12.spawn(162, 10, 0)
    bluebook13.spawn(168, 10, 0); bluebook14.spawn(173, 10, 0); bluebook15.spawn(133, 10, 0)
    bluebook16.spawn(149, 10, 0); bluebook17.spawn(154, 10, 0); bluebook18.spawn(164, 10, 0)
    redbook1.spawn(143, 10, 0); redbook2.spawn(147, 10, 0); redbook3.spawn(164, 10, 0)
    redbook4.spawn(126, 10, 0); redbook5.spawn(132, 10, 0); redbook6.spawn(149, 10, 0)
    redbook7.spawn(145, 10, 0); redbook8.spawn(151, 10, 0); redbook9.spawn(125, 10, 0)
    redbook10.spawn(139, 10, 0); redbook11.spawn(144, 10, 0); redbook12.spawn(149, 10, 0)
    redbook13.spawn(155, 10, 0); redbook14.spawn(127, 10, 0); redbook15.spawn(137, 10, 0); redbook16.spawn(152, 10, 0)
    purbook1.spawn(165, -10, 0); purbook2.spawn(156, -10, 0)
# #--------------------------------------------------------- bounce ------------------------------------------------------------
    bluebook_1b.spawn(132,20,20,bounce=True)
    bluebook_2b.spawn(137,20,20,bounce=True)
    bluebook_3b.spawn(142,20,20,bounce=True)
    bluebook_4b.spawn(147,20,20,bounce=True)
    bluebook_5b.spawn(152,20,20,bounce=True)
    bluebook_6b.spawn(157,20,20,bounce=True)
    bluebook_7b.spawn(162,20,20,bounce=True)
    bluebook_8b.spawn(167,20,20,bounce=True)
    bluebook_9b.spawn(172,20,20,bounce=True)
# #--------------------------------------------------------- disco -------------------------------------------------------------
    bluebook01.spawn(129,20,0)
    bluebook02.spawn(150,20,0)
    bluebook03.spawn(139,20,0)
    bluebook04.spawn(140,20,0)
#-------------------------------------------------------------------------------------------------------------------------------
    cooldown += 0.05

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
    if heart == 0:
        heart = 5
    win.blit(FONT.render("Score : "+str(int(time)), True, (255,255,255)), (20,20))
    # win.blit(FONT.render("Heart : "+ "<3"*(int(heart)), True, (255,255,255)), (900,20))
    redrawGameWindow()

pygame.quit()
