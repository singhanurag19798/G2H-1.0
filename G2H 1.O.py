'''
    Developed by ANURAG SINGH
        G2H 1.0
'''
#library used
import pygame as py
from sys import exit
from random import randint
#initial
py.init()
py.mixer.init()
screen = py.display.set_mode((900, 500))
py.display.set_caption("G2H 1.0")
p=py.image.load("bg\\bg3.jpg").convert()
p=py.transform.scale(p,(900, 400))
sky=p
ground = py.image.load("bg\\ground.png").convert()
ground = py.transform.scale(ground, (900,220))
black=(0,0,0)

blood=py.transform.scale(py.image.load("blood.png"),(60,60))
#camel
camel=[]
for i in range(1,33):
    p=py.transform.scale(py.image.load("camel\\camel ("+str(i)+").png"),(250,200))
    p.set_colorkey(black)
    camel.append(p)
#______________________________enemy______________________________________
#small enemy2
s2=[]
for i in range(12):
    p=py.transform.scale(py.image.load("enemy\\s2\\"+str(i)+".png"),(170,170))
    p.set_colorkey()
    s2.append(p)
#small enemy1

#run

s1r=[]
for i in range(15):
    p=py.transform.scale(py.image.load("enemy\\s1\\run\\"+str(i)+".png"),(350,250))
    p.set_colorkey(black)
    s1r.append(p)
    
#attack

s1a=[]
for i in range(15):
    p=py.transform.scale(py.image.load("enemy\\s1\\attack\\"+str(i)+".png"),(350,250))
    p.set_colorkey(black)
    s1a.append(p)
#burst1
burst1=[]
for i in range(16):
    p=py.transform.scale(py.image.load("explosion\\0\\"+str(i)+".png"),(350,250))
    p.set_colorkey(black)
    burst1.append(p)

#burst2
burst2=[]
for i in range(39):
    p=py.transform.scale(py.image.load("explosion\\2\\"+str(i)+".png"),(240,300))
    p.set_colorkey(black)
    burst2.append(p)

#blast
blast=[]
for i in range(1,48):
    p=py.transform.scale(py.image.load("explosion\\e3\\e ("+str(i)+").png"),(420,400))
    p.set_colorkey(black)
    blast.append(p)

#eblast
eblast=[]
for i in range(38):
    p=py.transform.scale(py.image.load("explosion\\1\\"+str(i)+".png"),(170,220))
    p.set_colorkey(black)
    eblast.append(p)
    
#_______________________________________gun_______________________________________________________
    
bullet=py.transform.scale(py.image.load("gun\\bullet.png"),(70,20))
bullet.set_colorkey(black)

#_________________________________player______________________________________

#forward stand

stand=[]
for i in range(40):
    p=py.transform.scale(py.image.load("player\\1\\fstand\\"+str(i)+".png"),(240,255))
    p.set_colorkey(black)
    stand.append(p)

#backward stand
    
bstand=[]
for i in range(40):
    p=py.transform.scale(py.image.load("player\\1\\bstand\\"+str(i)+".png"),(240,255))
    p.set_colorkey(black)
    bstand.append(p)

#forward run
frun=[]
for i in range(18):
    p=py.transform.scale(py.image.load("player\\1\\forward run\\"+str(i)+".png"),(240,255))
    p.set_colorkey(black)
    frun.append(p)

#background run
brun=[]
for i in range(18):
    p=py.transform.scale(py.image.load("player\\1\\backward run\\"+str(i)+".png"),(240,255))
    p.set_colorkey(black)
    brun.append(p)

#forward to backward jump
ftb=[]
for i in range(50):
    p=py.transform.scale(py.image.load("player\\1\\ftb jump\\"+str(i)+".png"),(320,400))
    p.set_colorkey(black)
    ftb.append(p)

#backward to forward jump
btf=[]
for i in range(30):
    p=py.transform.scale(py.image.load("player\\1\\btf jump\\"+str(i)+".png"),(320,400))
    p.set_colorkey(black)
    btf.append(p)

#________________________________game start window________________________________

start_window=py.transform.scale(py.image.load("main\\main.png"),(900,500))
end_window=py.transform.scale(py.image.load("main\\game over.jpg"),(900,500))
p_item=[]
e_item=[]
time_run=[0]
for i in range(119):
    p=py.transform.scale(py.image.load("enemy\\b2\\"+str(i)+".png"),(400,410))
    p.set_colorkey(black)
    e_item.append(p)
for i in range(312):
    p=py.transform.scale(py.image.load("player\\2\\"+str(i)+"p.png"),(520,500))
    p.set_colorkey(black)
    p_item.append(p)
def game_start():
    d=True
    i=311
    while True:
        time_run[0]=py.time.get_ticks()
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            if event.type==py.KEYDOWN:
                if event.key==py.K_RETURN:
                    game_play()
                    d=False
        if d:     
            screen.blit(start_window,(0,0))
            screen.blit(e_item[(py.time.get_ticks()//50)%119],(500,110))
            screen.blit(p_item[int(i)],(-60,40))
            i-=0.6
        if i<=0: i=311
        py.display.flip()

#________________________________game_over_window_________________________

def game_over():
    while True:
        time_run=py.time.get_ticks()
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            if event.type==py.KEYDOWN:
                if event.key==py.K_RETURN:
                    game_play()
                if event.key==py.K_SPACE:
                    game_start()
        screen.blit(end_window,(0,0))
        py.display.flip()
                          
#________________________________main game_______________________________________
clock = py.time.Clock()
def game_play():
    def gun_fire(gun_list,deads1_count):
        check=True
        for rect in gun_list:
            ch=True
            rect.x+=20
            if enemys1_x-player_x<200: x,bx=110,150
            else: x,bx=90,130
            if rect.x>enemys1_x+x:
                gun_list.remove(rect)
                ch=False
            if ch and rect.x>enemys2_x+20:
                gun_list.remove(rect)
                deads2_count[0]-=1
                ch=False
            if ch: screen.blit(bullet, rect)
            if 50<rect.x-enemys1_x<100:
                screen.blit(blood,(enemys1_x+bx,enemys1_y+140))
                deads1_count[0]-=1
            if (rect.x>900 or rect.x<-10) and ch:
                gun_list.remove(rect)
        return gun_list
    #______________________________score_________________________________________

    def display_score(val):
        text_surface=font.render(f'Score: {val}',False,(0,54,32))
        score_rect=text_surface.get_rect(center=(65,25))
        screen.blit(text_surface,score_rect)
        return val

    player_x = 30
    run=0
    jump=0
    fjump_count=0
    bjump_count=0
    player_y=60
    delay=0
    st=1
    gun_y=360
    gun_x=240
    burst2_i=0
    burst3_i=0
    s2burst_i=0
    enemys1_x=1000
    sky_i=0
    score=[0]
    gun_list=[]
    s2_list=[]
    last_shot_time=0
    font=py.font.Font("Banty Bold.ttf",30)
    deads1_count=[30]
    deads2_count=[5]
    enemys2_x=920
    enemys2_y=280
    enemys1_y=160
    camel_x=-100
    camel_y=170
    enemys1_live=True
    enemys2_live=True
    burst1_i=0
    health=150
    pblast=False
    blast_check=False
    blast_i=0

    while True:
        clock.tick(60)
        current_time=py.time.get_ticks()
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()

        keys = py.key.get_pressed()
        if not blast_check:
            if keys[py.K_UP] or keys[py.K_SPACE] or keys[py.K_w]:
                if player_y==60 and delay==0:
                    jump_x=player_x
                    py.mixer.music.load("sound\\jump.mp3")
                    py.mixer.music.play()
                    delay+=1
                    k=-6
                    jump=1
                    fjump_count=bjump_count=0
            elif jump==0:
                if keys[py.K_RIGHT] or keys[py.K_d]:
                    st=1
                    if enemys1_x-player_x>120: player_x+=0.06
                    run=3
                elif keys[py.K_LEFT] or keys[py.K_a]:
                    st=0
                    player_x-=0.8
                    run=4
                else:
                    run=0
            if (keys[py.K_k] or keys[py.K_g]) and st!=0 and st!=4 and jump==0:
                if current_time - last_shot_time >=200:
                    py.mixer.music.load("sound\\gun.mp3")
                    py.mixer.music.play()
                    y=gun_y-30 if run in [3,4] else gun_y
                    gun_list.append(bullet.get_rect(midbottom=(player_x+230,y)))
                    last_shot_time = current_time     
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 380))
        screen.blit(camel[(current_time//60)%32],(camel_x,camel_y))
        if camel_x>920: camel_x=-100
        camel_x+=1
        score[0]=display_score(score[0])
        if pblast:
            screen.blit(blast[burst3_i%47],(player_x-60,player_y))
            burst3_i+=1
        if burst3_i>=52:
            game_over()
        if jump==1:
            if fjump_count>=30:
                jump=0
                delay=0
            if fjump_count==8:
                k=7
            if fjump_count==1: jump_x-=50
            if bjump_count>=50:
                jump=0
                delay=0
            if bjump_count==10:
                k=7
            if bjump_count==3:  jump_x+=43
        #____________________________________enemy_________________________________
        if enemys2_live:
            screen.blit(s2[(current_time//30)%12],(enemys2_x,enemys2_y))
            if deads2_count[0]<3: enemys2_x-=6
            else: enemys2_x-=4
        elif not pblast:
            if s2burst_i<38:
                screen.blit(eblast[s2burst_i],(enemys2_x,enemys2_y-60))
                s2burst_i+=1
            else:
                s2burst_i=0
                enemys2_x=920
                enemys2_live=True
        if enemys2_x<=-95: enemys2_x=920
        if deads2_count[0]<=0:
            deads2_count[0]=5
            score[0]+=5
            enemys2_live=False
        if deads1_count[0]<=0:
            deads1_count[0]=30
            score[0]+=10
            enemys1_live=False
        if burst1_i>=16:
            enemys1_live=True
            enemys1_x=1000
            burst1_i=0
        if enemys1_live:
            if enemys1_x-player_x<250:
                enemy=s1a
                health-=1
                x=30
            else:
                enemy=s1r
                x=40
            if enemys1_x<-100: enemys1_x=1000
            screen.blit(enemy[int(current_time/x)%15],(enemys1_x,enemys1_y))
            if enemys1_x-player_x>120:
                if deads1_count[0]<13: enemys1_x-=5.6
                else: enemys1_x-=1.6
        else:
            screen.blit(burst1[int(burst1_i)],(enemys1_x,enemys1_y))
            burst1_i+=0.7
        gun_list=gun_fire(gun_list,deads1_count)
        if player_x+80>=enemys2_x:
            pblast=True
            enemys2_live=False
        if health>0:
            if not blast_check and not pblast:
                if jump==1:
                    if st==0:
                        py.time.delay(10)
                        screen.blit(ftb[int(bjump_count)], (jump_x,player_y))
                        bjump_count+=0.5
                        player_y+=k
                    else:
                        py.time.delay(15)
                        screen.blit(btf[int(fjump_count)], (jump_x,player_y))
                        fjump_count+=0.5
                        player_y+=k
                    if player_y>60: player_y=60
                elif run==3: screen.blit(frun[int(current_time/27)%18], (player_x, 200))
                elif run==4: screen.blit(brun[int(current_time/27)%18], (player_x, 200))
                else:
                    if st==1: screen.blit(stand[int(current_time/100)%40], (player_x, 200))
                    else: screen.blit(bstand[int(current_time/100)%40], (player_x, 200))
        elif burst2_i<20:
            screen.blit(burst2[(current_time//7)%39],(player_x,player_y+100))
            burst2_i+=1
        else: game_over()
        if blast_check:
            screen.blit(blast[int(blast_i)],(player_x-50,player_y+70))
            blast_i+=0.7
        if blast_i>=47: game_over()
        py.display.update()
        py.time.delay(10)
        py.display.flip()

game_start()
