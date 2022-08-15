import pygame

pygame.init()

start_second = 40.0

music = pygame.mixer.music.load('D:/Thomas/Allgemeines/Technik-Projekte/Jonglierball_19/LED_Ball_Sequenz_Tool/Schnitt2.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_pos(start_second)

time_adjustment = pygame.time.get_ticks() - start_second*1000

screenwidth = 1200
screenheight = 680
win = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("Name des Fensters")

#bg = pygame.image.load("D:/Thomas/Uni/Master/WS1920/Pygametutorial/bg.jpg")



clock = pygame.time.Clock()

class ball(object):
    def __init__(self, x, y, ballnumber):
        self.x = x
        self.y = y
        self.color = [0, 0, 0]
        self.radius = 30
        self.sequence = []
        self.sequence_idx = 0
        self.ballnumber = ballnumber
        self.output_txt = '//Ball' + str(self.ballnumber) + '\n'
        
    def change_color(self, color, time):
        offset_shift_time = 40000
        self.sequence.append(['change', color, time+time_adjustment +offset_shift_time])
        self.output_txt = self.output_txt + 'aufleuchten(' + str(color[0]) +', ' + str(color[1]) +', ' + str(color[2]) +', ' + str(time+offset_shift_time) + ');\n'

    def fade_color(self, color1, color2, time1, time2):
        offset_shift_time = 40000
        self.sequence.append(['fade', color1, color2, time1+time_adjustment+offset_shift_time, time2+time_adjustment+offset_shift_time])
        self.output_txt = self.output_txt + 'fading(' + str(color1[0]) +', ' + str(color1[1]) +', ' + str(color1[2]) +', ' + str(color2[0]) +', ' + str(color2[1]) +', ' + str(color2[2]) +', ' + str(time1+offset_shift_time) +', ' + str(time2+offset_shift_time) + ');\n'


    def run_sequence(self):
        command = self.sequence[self.sequence_idx][0]
        
        # einfaches aufleuchten ausführen
        if command == 'change':
            color = self.sequence[self.sequence_idx][1]
            time = self.sequence[self.sequence_idx][2]

            if pygame.time.get_ticks() >= time:
                self.color = color
                if self.sequence_idx+1 < len(self.sequence):
                    self.sequence_idx = self.sequence_idx+1
                else:
                    print('Ball' +str(self.ballnumber) + '-Sequence beendet')
        # faden ausführen
        elif command == 'fade':
            color1 = self.sequence[self.sequence_idx][1]
            color2 = self.sequence[self.sequence_idx][2]
            time1 = self.sequence[self.sequence_idx][3]
            time2 = self.sequence[self.sequence_idx][4]
            currenttime = pygame.time.get_ticks()

            if currenttime >= time1 and currenttime <= time2:
                self.color[0] = color1[0] + (color2[0]-color1[0])*(currenttime-time1)/(time2-time1)
                self.color[1] = color1[1] + (color2[1]-color1[1])*(currenttime-time1)/(time2-time1)
                self.color[2] = color1[2] + (color2[2]-color1[2])*(currenttime-time1)/(time2-time1)
                self.color = [ round(x) for x in self.color ]
            if currenttime >= time2 and self.sequence_idx+1 < len(self.sequence):
                self.sequence_idx = self.sequence_idx+1
            else:
                print('Ball' +str(self.ballnumber) + '-Sequence beendet')

    def print_arduino_code(self):
        with open("Ball" + str(self.ballnumber) + ".txt", "w") as output:
            output.write(self.output_txt)

    def draw(self):
        pygame.draw.circle(win, self.color, [self.x, self.y], self.radius)

def redrawGameWindow():
    # global walkcnt
    #win.blit(bg, (0, 0))
    pygame.draw.rect(win, [100, 200, 100], [0, 0, screenwidth, screenheight])
    
    #pygame.draw.circle(win, [100, 0, 100], [100, 100], 100)

    time = pygame.time.get_ticks() - time_adjustment

    text = font.render('Time: ' + str(time), 1, (0,0,0))
    win.blit(text, (10, 30))

    Ball1.draw()
    Ball2.draw()
    Ball3.draw()
    Ball4.draw()
    Ball5.draw()
    Ball6.draw()

    pygame.display.update()
    pass

# Mainloop
font = pygame.font.SysFont('comicsans', 30, True)
#pygame.draw.rect(win, [100, 200, 100], [0, 0, screenwidth, screenheight])

Ball1 = ball(200, 300, 1)
Ball2 = ball(600, 500, 2)
Ball3 = ball(1000, 300, 3)
Ball4 = ball(500, 200, 4)
Ball5 = ball(600, 200, 5)
Ball6 = ball(700, 200, 6)


#Ball1
Ball1.change_color([0, 0, 0], 0)
Ball1.change_color([0, 0, 255], 7450)
for i in range(46):
    Ball1.change_color([0, 0, 0], 13000 + 480*i) # blinkend rot
    Ball1.change_color([255, 0, 0], 13100 + 480*i)
Ball1.fade_color([255,0,0],[100,100,255],13000 + 480*46, 13000 + 480*50)
Ball1.fade_color([100,100,255],[255,50,50],51400 + 480*0, 51400 + 480*2)
Ball1.change_color([255, 255, 255], 59000)
Ball1.change_color([0, 0, 0], 60000)
Ball1.change_color([255, 255, 255], 62000)
Ball1.change_color([0, 0, 0], 63000)
Ball1.change_color([255, 255, 255], 64100)
Ball1.change_color([0, 0, 0], 64200)
Ball1.change_color([255, 255, 255], 64400)
Ball1.change_color([0, 0, 0], 64500)
Ball1.change_color([255, 255, 255], 64700)

Ball1.change_color([0, 0, 0], 65000)
Ball1.change_color([255, 255, 255], 65100)
Ball1.change_color([0, 0, 0], 65500)
Ball1.change_color([255, 255, 255], 65600)
Ball1.change_color([0, 0, 0], 66000)
Ball1.change_color([255, 255, 255], 66100)

for i in range(8):
    Ball1.fade_color([255,255,255],[0,0,0], 70000+2*960*(i*2) , 70000+2*960*(i*2+1))
    Ball1.fade_color([0,0,0],[255,255,255], 70000+2*960*(i*2+1), 70000+2*960*(i*2+2))

Ball1.fade_color([255,255,255],[0,0,0], 112800, 114000)

#Ball2
Ball2.change_color([0, 0, 0], 0)
Ball2.change_color([0, 0, 255], 5300)
Ball2.change_color([255, 0, 0], 11100)
for i in range(8, 46):
    Ball2.change_color([0, 0, 0], 13000 + 480*i) # blinkend rot
    Ball2.change_color([255, 0, 0], 13100 + 480*i)
Ball2.fade_color([255,0,0],[100,100,255],13000 + 480*46, 13000 + 480*50)
Ball2.fade_color([100,100,255],[255,50,50],51400 + 480*0, 51400 + 480*2)
Ball2.change_color([255, 255, 255], 60000)
Ball2.change_color([0, 0, 0], 61000)
Ball2.change_color([255, 255, 255], 63000)
Ball2.change_color([0, 0, 0], 64000)
Ball2.change_color([255, 255, 255], 64200)
Ball2.change_color([0, 0, 0], 64300)
Ball2.change_color([255, 255, 255], 64500)
Ball2.change_color([0, 0, 0], 64600)
Ball2.change_color([255, 255, 255], 64800)
Ball2.change_color([0, 0, 0], 65000)
Ball2.change_color([255, 255, 255], 65100)
Ball2.change_color([0, 0, 0], 65500)
Ball2.change_color([255, 255, 255], 65600)
Ball2.change_color([0, 0, 0], 66000)
Ball2.change_color([255, 255, 255], 66100)

for i in range(8):
    Ball2.fade_color([255,255,255],[0,0,0], 70640+2*960*(i*2) , 70640+2*960*(i*2+1))
    Ball2.fade_color([0,0,0],[255,255,255], 70640+2*960*(i*2+1), 70640+2*960*(i*2+2))

Ball2.fade_color([255,255,255],[0,0,0], 112800, 114000)

#Ball3
Ball3.change_color([0, 0, 0], 0)
Ball3.change_color([0, 0, 255], 9200)
for i in range(4, 46):
    Ball3.change_color([0, 0, 0], 13000 + 480*i) # blinkend rot
    Ball3.change_color([255, 0, 0], 13100 + 480*i)
Ball3.fade_color([255,0,0],[100,100,255],13000 + 480*46, 13000 + 480*50)
Ball3.fade_color([100,100,255],[255,50,50],51400 + 480*0, 51400 + 480*2)
Ball3.change_color([255, 255, 255], 61000)
Ball3.change_color([0, 0, 0], 62000)
Ball3.change_color([255, 255, 255], 64000)
Ball3.change_color([0, 0, 0], 64100)
Ball3.change_color([255, 255, 255], 64300)
Ball3.change_color([0, 0, 0], 64400)
Ball3.change_color([255, 255, 255], 64600)
Ball3.change_color([0, 0, 0], 64700)
Ball3.change_color([255, 255, 255], 64900)
Ball3.change_color([0, 0, 0], 65000)
Ball3.change_color([255, 255, 255], 65100)
Ball3.change_color([0, 0, 0], 65500)
Ball3.change_color([255, 255, 255], 65600)
Ball3.change_color([0, 0, 0], 66000)
Ball3.change_color([255, 255, 255], 66100)

for i in range(8):
    Ball3.fade_color([255,255,255],[0,0,0], 71280+2*960*(i*2) , 71280+2*960*(i*2+1))
    Ball3.fade_color([0,0,0],[255,255,255], 71280+2*960*(i*2+1), 71280+2*960*(i*2+2))

Ball3.fade_color([255,255,255],[0,0,0], 112800, 114000)

#Ball4
Ball4.change_color([0, 0, 0], 0)
Ball4.change_color([255, 0, 0], 410)
Ball4.change_color([0, 255, 100], 3410)
for i in range(12, 24):
    Ball4.change_color([0, 0, 0], 13000 + 480*i) # blinkend rot
    Ball4.change_color([255, 0, 0], 13100 + 480*i)
for i in range(24, 48):
    Ball4.change_color([0, 0, 0], 13000 + 480*i) # blinkend blau
    Ball4.change_color([100, 100, 255], 13100 + 480*i)



Ball4.fade_color([100,100,255],[0,250,0],13000 + 480*48, 13000 + 480*60)
Ball4.change_color([0, 250, 0], 43700)
Ball4.fade_color([0,250,0],[255,50,50],51400 + 480*0, 51400 + 480*2)

Ball4.change_color([20, 200, 100], 66700)
Ball4.change_color([255, 0, 0], 72700)

for i in range(13):
    if i%3 == 2:
        Ball4.change_color([255, 0, 0], 74700+950*i)
    elif i%3 == 1:
        Ball4.change_color([0, 255, 0], 74700+950*i)
    else:
        Ball4.change_color([0, 0, 255], 74700+950*i)

for i in range(4):
    Ball4.fade_color([0,0,255],[255,0,0], 86000+960*(i*2) , 86000+960*(i*2+1))
    Ball4.fade_color([255,0,0],[0,0,255], 86000+960*(i*2+1), 86000+960*(i*2+2))

Ball4.change_color([0, 255, 255], 97500)
Ball4.change_color([255, 255, 255], 99400)
Ball4.change_color([0, 255, 255], 101300)
Ball4.change_color([0, 0, 255], 105200)

Ball4.fade_color([0,0,255],[0,0,0], 112800, 114000)

#Ball5
Ball5.change_color([0, 0, 0], 0)
Ball5.change_color([255, 0, 0], 1410)
Ball5.change_color([0, 255, 100], 3410)
for i in range(12, 28):
    Ball5.change_color([0, 0, 0], 13000 + 480*i) # blinkend rot
    Ball5.change_color([255, 0, 0], 13100 + 480*i)
for i in range(28, 48):
    Ball5.change_color([0, 0, 0], 13000 + 480*i) # blinkend blau
    Ball5.change_color([100, 100, 255], 13100 + 480*i)
Ball5.fade_color([100,100,255],[0,250,0],13000 + 480*48, 13000 + 480*60)
Ball5.change_color([0, 0, 250], 43700)
Ball5.fade_color([0,0,250],[255,50,50],51400 + 480*0, 51400 + 480*2)

Ball5.change_color([0, 0, 255], 68700)

for i in range(13):
    if i%3 == 2:
        Ball5.change_color([0, 255, 0], 74700+950*i)
    elif i%3 == 1:
        Ball5.change_color([0, 0, 255], 74700+950*i)
    else:
        Ball5.change_color([255, 0, 0], 74700+950*i)

for i in range(4):
    Ball5.fade_color([255,0,0],[0,255,0], 86000+960*(i*2) , 86000+960*(i*2+1))
    Ball5.fade_color([0,255,0],[255,0,0], 86000+960*(i*2+1), 86000+960*(i*2+2))

Ball5.fade_color([255,0,0],[0,0,255], 94000, 96000)
Ball5.change_color([0, 255, 255], 97500)
Ball5.change_color([255, 255, 255], 99400)
Ball5.change_color([0, 255, 255], 101300)
Ball5.change_color([30, 100, 255], 105200)
Ball5.change_color([255, 0, 0], 111700)

Ball5.fade_color([255,0,0],[0,0,0], 112800, 114000)

#Ball6
Ball6.change_color([0, 0, 0], 0)
Ball6.change_color([255, 0, 0], 2410)
Ball6.change_color([0, 255, 100], 3410)
for i in range(12, 32):
    Ball6.change_color([0, 0, 0], 13000 + 480*i) # blinkend rot
    Ball6.change_color([255, 0, 0], 13100 + 480*i)
for i in range(32, 48):
    Ball6.change_color([0, 0, 0], 13000 + 480*i) # blinkend blau
    Ball6.change_color([100, 100, 255], 13100 + 480*i)
Ball6.fade_color([100,100,255],[0,250,0],13000 + 480*48, 13000 + 480*60)
Ball6.change_color([0, 250, 0], 43700)
Ball6.fade_color([0,250,0],[255,50,50],51400 + 480*0, 51400 + 480*8)

Ball6.change_color([0, 255, 0], 70700)

for i in range(13):
    if i%3 == 2:
        Ball6.change_color([0, 0, 255], 74700+950*i)
    elif i%3 == 1:
        Ball6.change_color([255, 0, 0], 74700+950*i)
    else:
        Ball6.change_color([0, 255, 0], 74700+950*i)

for i in range(4):
        Ball6.fade_color([0,255,0],[0,0,255], 86000+960*(i*2) , 86000+960*(i*2+1))
        Ball6.fade_color([0,0,255],[0,255,0], 86000+960*(i*2+1), 86000+960*(i*2+2))
#Ball6.fade_color([0,0,0],[255,255,255],2000,5000)

Ball6.fade_color([0,255,0],[0,0,255], 94000, 96000)
Ball6.change_color([0, 255, 255], 97500)
Ball6.change_color([255, 255, 255], 99400)
Ball6.change_color([0, 255, 255], 101300)
Ball6.change_color([0, 0, 255], 105200)

Ball6.fade_color([0,0,255],[0,0,0], 112800, 114000)


Ball1.print_arduino_code()
Ball2.print_arduino_code()
Ball3.print_arduino_code()
Ball4.print_arduino_code()
Ball5.print_arduino_code()
Ball6.print_arduino_code()


run = True
while run:
    # pygame.time.delay(30)
    clock.tick(27)
    

    Ball1.run_sequence()
    Ball2.run_sequence()
    Ball3.run_sequence()
    Ball4.run_sequence()
    Ball5.run_sequence()
    Ball6.run_sequence()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        pass

    if keys[pygame.K_LEFT]:
        pass

    redrawGameWindow()
    
pygame.quit()