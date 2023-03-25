import time
import math
import pygame
from pygame import font

import math
from pygame import mixer
pygame.init()
tic = 0

#loop-true
run = True
game = False
menu = True
pygame.display.set_caption('Ping Pong')
airun = False
tworun = False

#mouse-games
hover1 = False
hover2 = False

#display
screen = pygame.display.set_mode((600, 600))
icon = pygame.image.load("logo.png")
titleico = pygame.image.load('pong.png')
titleicon = pygame.transform.smoothscale(titleico,(670,372  ))
pygame.display.set_icon(icon)
screen_menu = pygame.display.set_mode((600,600))

#music
mixer.music.load('smooth_waters.mp3')
mixer.music.set_volume(0.2)

#characters
speedxp = 0
speedxc = 0
health = 10
turns = 0
turn_plus = True

paddle_p = pygame.image.load('paddle.png')
paddle_px = 265
paddle_py = 571

paddle_c = pygame.image.load('paddle.png')
paddle_cx = 265
paddle_cy = 6



#ball
ball = pygame.image.load('ball.png')
speedb_x = 0.3
speedb_y = 0.08
ballx = 280
bally = 300
pong = mixer.Sound('pingpong.mp3')
#score

score1 = 0
score2 = 0
game_font = pygame.font.Font('undertale.ttf',24)
game_fonts = pygame.font.Font('undertale.ttf',12)
game_fonts2 = pygame.font.Font('undertale.ttf',16)
big_font = pygame.font.Font('undertale.ttf',40)
big_font1 = pygame.font.Font('undertale.ttf',20)
winners = game_font.render('WINNER', True, (78, 32, 56))
alpha = 0
winner = 0

increment = True
set1 = 0
set2 = 0
#colours
orange = (255,136,75)
white = (255,255,255)

#trophy

trophy = pygame.image.load('trophy1.png')
trophy1 = pygame.transform.smoothscale(trophy,(112.5,112.5))
#functions

def dist(x1,y1,x2,y2):
    dist = math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))
    return dist

#countdown
countdown = False
countdown = mixer.Sound('countdown.mp3')

tic = time.perf_counter()

mixer.music.play(-1)

#score records
ai_scr = open('ai_scr.txt','w+')
two_scr = open('two_scr.txt','r+')
ai_rec = False
two_scr = False

while run:
    if game:

        if airun:


            if math.ceil(bally) == 450 and turn_plus == True:
                turn_plus = False
                print(turns)

            #paddle-correction
                turns += 1
            if paddle_px >= 520:
                paddle_px = 520
            elif paddle_px <= 0:
                paddle_px = 0

            if paddle_cx >= 520:
                paddle_cx = 520
            elif paddle_cx <= 0:
                paddle_cx = 0

            #computer-ai
            if bally <= 80:
                if ballx > paddle_cx:
                    speedxc = 0.5
                elif ballx < paddle_cx:
                    speedxc = -0.5

                else:
                    speedxc = 0

            elif bally > 80:
                speedxc = 0

           #score txt

            score2_txt = game_font.render(str(health), True, (white))
            if turns > 0:
                set2_txt = game_font.render(str((turns - 1)), True, (orange))
            else:
                set2_txt = game_font.render(str((turns)), True, (orange))
            tut_txt = game_fonts.render('<A : D> ',True,(0,0,0))
            tut_txt.set_alpha(150)
            score_tut = game_font.render('Health           Turns',True,(55,55,55))
            lost = game_fonts2.render('You have survived for %d turns!' % (turns - 1),True,(0,0,0))
            screen.fill((130, 148, 96))
            #winner.set_alpha(alpha)


            #distance-flip
            if dist(ballx,bally,paddle_px,paddle_py) <= 40:
                speedb_y = -0.08
                speedb_y += -0.0001
                turn_plus = True
                print(turn_plus)
                pong.play()


            if dist(ballx,bally,paddle_cx,paddle_cy) <= 25:
                speedb_y = 0.08
                speedb_y += 0.0001

                pong.play()




            #events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        import sys

                        print("argv was", sys.argv)
                        print("sys.executable was", sys.executable)
                        print("restart now")

                        import os

                        os.execv(sys.executable, ['python'] + sys.argv)

                    elif event.key == pygame.K_a:
                        speedxp = -0.5
                    elif event.key == pygame.K_d:
                        speedxp = 0.5


                elif event.type == pygame.KEYUP:
                    speedxp = 0
                    speedxc = 0

            # movement
            ballx += speedb_x
            bally += speedb_y

            paddle_px += speedxp
            paddle_cx += speedxc



            if ballx >= 550 or ballx <= 0:
                speedb_x *= -1

            if bally >= 550 or bally <= 0:

                if bally >= 550:
                    speedb_y *= -1
                    speedb_y += -0.02
                    if speedb_x > 0:
                        speedb_x += 0.03
                    elif speedb_x > 0:
                        speedb_x += -0.03
                    health += -1
                    turn_plus = True
                elif bally <= 0:
                    speedb_y *= -1
                    speedb_y += 0.02
                    if speedb_x > 0:
                        speedb_x += 0.03
                    elif speedb_x > 0:
                        speedb_x += -0.03
                    score2 += 1




            #figures-aesthetics
            #pygame.draw.line(surface, color, start_pos, end_pos, width)
            pygame.draw.line(screen, (103,71,71), (0,300), (600,300), 4)
            #pygame.draw.circle(window, colour, circle_x_ & _y, circle_radius, border_width)
            pygame.draw.circle(screen, (103,71,71),(300,300), 50, 4)
            #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
            pygame.draw.rect(screen,(103,71,71),pygame.Rect(0,0,600,600),10)
            #characters
            screen.blit(paddle_c,(paddle_cx,paddle_cy))
            screen.blit(paddle_p, (paddle_px, paddle_py))
            screen.blit(ball,(ballx ,bally))

            #score
            screen.blit(score2_txt,(40,310))
            screen.blit(set2_txt, (525, 310))
            screen.blit(tut_txt,(285,590))
            screen.blit(score_tut,(80,310))

            if health < 1:
                score2_txt.set_alpha(0)
                set2_txt.set_alpha(0)
                screen.blit(lost,(70,50))
                bally = 275
                ballx = 278
                speedxp = 0
                paddle_px = 265
                paddle_py = 571
                paddle_cx = 265
                paddle_cy = 6
                mixer.music.fadeout(2000)


        elif tworun:
            if paddle_px >= 520:
                paddle_px = 520
            elif paddle_px <= 0:
                paddle_px = 0

            if paddle_cx >= 520:
                paddle_cx = 520
            elif paddle_cx <= 0:
                paddle_cx = 0

            # score txt
            score1_txt = game_font.render(str(score1), True, (white))
            score2_txt = game_font.render(str(score2), True, (white))
            set1_txt = game_font.render(str(set1), True, (orange))
            set2_txt = game_font.render(str(set2), True, (orange))
            tut_txt = game_fonts.render('FOR TOP <A : D> || FOR BOTTOM <J : L> ', True, (0, 0, 0))
            tut_txt.set_alpha(150)
            score_tut = game_font.render('Score               Sets', True, (55, 55, 55))
            screen.fill((130, 148, 96))
            winners = game_font.render('WINNER', True, (78, 32, 56))
            # winner.set_alpha(alpha)

            # distance-flip
            if dist(ballx, bally, paddle_px, paddle_py) <= 40:
                speedb_y = -0.08
                speedb_y += -0.0001

                pong.play()

            if dist(ballx, bally, paddle_cx, paddle_cy) <= 40:
                speedb_y = 0.08
                speedb_y += 0.0001

                pong.play()

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        import sys

                        print("argv was", sys.argv)
                        print("sys.executable was", sys.executable)
                        print("restart now")

                        import os

                        os.execv(sys.executable, ['python'] + sys.argv)

                    elif event.key == pygame.K_a:
                        speedxp = -0.5
                    elif event.key == pygame.K_d:
                        speedxp = 0.5
                    elif event.key == pygame.K_j:
                        speedxc = -0.5
                    elif event.key == pygame.K_l:
                        speedxc = 0.5
                    elif event.key == pygame.K_p:
                        speedb_y = 0
                        speedb_x = 0

                elif event.type == pygame.KEYUP:
                    speedxp = 0
                    speedxc = 0

            # movement
            ballx += speedb_x
            bally += speedb_y

            paddle_px += speedxp
            paddle_cx += speedxc

            if ballx >= 550 or ballx <= 0:
                speedb_x *= -1

            if bally >= 550 or bally <= 0:

                if bally >= 550:
                    speedb_y *= -1
                    speedb_y += -0.02
                    if speedb_x > 0:
                        speedb_x += 0.03
                    elif speedb_x > 0:
                        speedb_x += -0.03
                    score1 += 1
                elif bally <= 0:
                    speedb_y *= -1
                    speedb_y += 0.02
                    if speedb_x > 0:
                        speedb_x += 0.03
                    elif speedb_x > 0:
                        speedb_x += -0.03
                    score2 += 1

            # figures-aesthetics
            # pygame.draw.line(surface, color, start_pos, end_pos, width)
            pygame.draw.line(screen, (103, 71, 71), (0, 300), (600, 300), 4)
            # pygame.draw.circle(window, colour, circle_x_ & _y, circle_radius, border_width)
            pygame.draw.circle(screen, (103, 71, 71), (300, 300), 50, 4)
            # pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
            pygame.draw.rect(screen, (103, 71, 71), pygame.Rect(0, 0, 600, 600), 10)
            # characters
            screen.blit(paddle_c, (paddle_cx, paddle_cy))
            screen.blit(paddle_p, (paddle_px, paddle_py))
            screen.blit(ball, (ballx, bally))

            # score
            screen.blit(score1_txt, (40, 265))
            screen.blit(score2_txt, (40, 310))
            screen.blit(set1_txt, (500, 265))
            screen.blit(set2_txt, (500, 310))
            screen.blit(tut_txt, (120, 0))
            screen.blit(score_tut, (76, 273))

            # sets
            if score1 == 6 and score2 < 6:
                set1 += 1
                score1 = 0
                score2 = 0
                if speedb_x > 0:
                    speedb_x = 0.3
                elif speedb_x < 0:
                    speedb_x = -0.3
            elif score2 == 6 and score1 < 6:
                set2 += 1
                score2 = 0
                score1 = 0
                if speedb_x > 0:
                    speedb_x = 0.3
                elif speedb_x < 0:
                    speedb_x = -0.3

            if set1 >= 3:
                winner = 1
                bally = 275
                ballx = 278
                speedxp = 0
                speedxc = 0
                paddle_px = 265
                paddle_py = 571
                paddle_cx = 265
                paddle_cy = 6
            elif set2 >= 3:
                winner = 2
                bally = 275
                ballx = 278
                speedxp = 0
                speedxc = 0
                paddle_px = 265
                paddle_py = 571
                paddle_cx = 265
                paddle_cy = 6

            if winner == 1:
                screen.blit(winners, (240, 40))
                screen.blit(trophy1, (248, 80))
            elif winner == 2:
                screen.blit(winners, (240, 540))
                screen.blit(trophy1, (248, 400))


    elif menu:
        pos = pygame.mouse.get_pos()
        if pos[1] >= 200 and pos[1] <= 250:
            if pos[0] >= 200 and pos[0] <= 400:
                hover1 = True
        else:
            hover1 = False
        if pos[1] >= 290 and pos[1] <= 340:
            if pos[0] >= 200 and pos[0] <= 400:
                hover2 = True
        else:
            hover2 = False
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    import sys

                    print("argv was", sys.argv)
                    print("sys.executable was", sys.executable)
                    print("restart now")

                    import os

                    os.execv(sys.executable, ['python'] + sys.argv)


            if event.type == pygame.MOUSEBUTTONDOWN:
                print('k')
                pos = pygame.mouse.get_pos()
                print(pos)
                if menu:
                    if pos[1] >= 200 and pos[1] <= 250:
                        if pos[0] >= 200 and pos[0] <= 400:
                            game =True
                            menu = False
                            airun = True
                    if pos[1] >= 290 and pos[1] <= 340:
                        if pos[0] >=200 and pos[0] <= 400:
                            game= True
                            menu = False
                            tworun = True

        screen.fill((10, 150, 255))
        title = big_font.render('Ping-Pong',True,(0,0,0))
        screen.blit(title,(105,50))
        ai = pygame.draw.rect(screen,(183,62,62),pygame.Rect(200,200,200,50),0,10 )
        two = pygame.draw.rect(screen,(183,62,62),pygame.Rect(200,290,200,50),0,10 )
        if not hover1:
            ai_txt = big_font1.render('Survival',True,(225,200,172))
            ai = pygame.draw.rect(screen, (183, 62, 62), pygame.Rect(200, 200, 200, 50), 0, 10)

        if not hover2:
            two_txt = big_font1.render('PvP', True, (219, 200, 172))
            two = pygame.draw.rect(screen, (183, 62, 62), pygame.Rect(200, 290, 200, 50), 0, 10)
        if hover1:
            ai_txt = big_font1.render('Survival', True, (255, 87, 127))
            ai = pygame.draw.rect(screen, (150, 62, 62), pygame.Rect(200, 200, 200, 50), 0, 10)
        if hover2:
            two_txt = big_font1.render('PvP', True, (255, 87, 127))
            two = pygame.draw.rect(screen, (150, 62, 62), pygame.Rect(200, 290, 200, 50), 0, 10)
        screen.blit(ai_txt,(220,210))
        screen.blit(two_txt,(265,300))
        screen.blit(titleicon,(-35,280))

    # update-screen
    pygame.display.update()
'''
    #sets
    if score1 == 6 and score2 < 6 :
        set1 += 1
        score1 = 0
        score2 = 0
        if speedb_x > 0:
            speedb_x = 0.3
        elif speedb_x < 0:
            speedb_x = -0.3
    elif score2 == 6 and score1 < 6 :
        set2 += 1
        score2 = 0
        score1 = 0
        if speedb_x > 0:
            speedb_x = 0.3
        elif speedb_x < 0:
            speedb_x = -0.3
            

    if set1 >= 3:
        winner = 1
        bally = 275
        ballx = 278
        speedxp = 0
        speedxc = 0
    elif set2 >= 3:
        winner = 2
        bally = 275
        ballx = 278
        speedxp = 0
        speedxc = 0

    if winner == 1:
        screen.blit(winners,(240,40))
    elif winner ==2:
        screen.blit(winners,(240,540 ))
'''

# songs bySound Effect from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6082">Pixabay</a>
