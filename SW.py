from pygame import *
from random import randint
font.init()
mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
font_1 = font.SysFont('Arial =', 35)
font_2 = font.SysFont('Arial', 24)
img_back = "background_1.jpg" 
img_Base = "Base.jpg" 
img_hero = "rocket.png"  
img_bullet = "bullet.png" 
img_bullet_1 = "bullet_1.png"
img_bullet_2 = "Plazma.png"
img_bullet_e = "bullet_e.png"
img_enemy = "ufo.png"   
img_enemy_1 = "ufo_1.png"  

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed = 0, Hp = 0):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.Hp = Hp
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        # mixer.music.load('moving.ogg')
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet( img_bullet, ship.rect.centerx, ship.rect.top, 20, 80, speed = 15)
        bullets.add(bullet)
    def fire_1(self):
        bullet_1 = Bullet( img_bullet_1, ship.rect.centerx, ship.rect.top, 40, 50, speed = 10)
        bullets_1.add(bullet_1)
    def fire_2(self):
        bullet_2 = plazma( img_bullet_2, ship.rect.centerx - 20, 20, 40, 400)
        bullets_2.add(bullet_2)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
class Bullet(GameSprite):
   def update(self):
    self.rect.y -= self.speed
    if self.rect.y < 0:
        self.kill()
class plazma(GameSprite):
    def update(self):
        self.rect.x = ship.rect.centerx - 20
class boss(GameSprite):
    def update(self):
        if self.rect.y < 50:
            self.rect.y += self.speed       
class Frame(GameSprite):
        pass
class Bonus(GameSprite):
    def update(self):
        if self.rect.y < 480:
            self.rect.y += self.speed
def reset ():
    global finish, run, able, present, present_1, present_a, present_1_a, collected, starting, start, Difficulty, Dif, B_b, S_Setting, Boss_health, goal, B_s, p_s, r, c, volume, score,  lost
    volume = 100
    score = 0
    lost = 0  
    finish = False
    run = True  
    c = 1
    able = 0
    present = False
    present_1 = False
    present_a = True
    present_1_a = True
    collected = 0
    starting = True 
    S_Setting = False   
    start = False
    Difficulty = "Hard"
    Dif = 3
    B_b = True
    Boss_health = 100
    goal = 300
    B_s = 100
    p_s = 200
    r = True
    monsters.empty()
    monsters_1.empty()
    bullets_1.empty()
    bullets_2.empty()
    bullets_e.empty ()
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
Base = transform.scale(image.load(img_Base), (win_width, win_height))
center = (win_width //2, win_height//2)
center_top = (win_width //2, 0)
Boss = boss( "Boss.png", win_width // 2 -150, -50 , 300, 100, speed = 0.5)
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
bullet_img = Bullet( img_bullet, 20, 100, 10, 40, speed = 15)
bullet_1_img = Bullet( img_bullet_1, 54, 100, 40, 50, speed = 10)
bullet_2_img = Bullet( img_bullet_2, 120, 100, 10, 40)
frame_1 = Frame('Frame_1.png', 0, 100, 50, 50 )
frame_2 = Frame('Frame.png', 50, 100, 50, 50 )
frame_3 = Frame('Frame.png', 100, 100, 50, 50 )
bonus = Bonus('bonus.png', randint(80, win_width-80), 0, 50, 70, 3 ) 
bonus_1 = Bonus('bonus_1.png', randint(80, win_width-80), 0, 50, 50, 3 ) 
Play = GameSprite('Play.png', win_width //2 - 70, win_height //2 - 100, 106, 35)
Options = GameSprite('Options.png', win_width //2 -100 ,win_height //2 -40, 156, 33)
Exit = GameSprite('Exit.png', win_width //2 - 70 ,win_height //2 + 20, 106, 34)
Back = GameSprite('Back.png', 30, 20, 107, 34)
difficulty = GameSprite('Difficulty.png', win_width //2 - 200, win_height // 2 -50, 150, 34)
Volume = GameSprite('Volume.png', win_width //2 -200, win_height //2 +50, 156, 33)
Menu = GameSprite('Menu.png', 10, 30, 32, 32)
Plus = GameSprite('plus.png', win_width //2 +100, win_height // 2 -50, 32, 32)
Plus_1 = GameSprite('plus.png', win_width //2 + 100, win_height // 2 +50, 32, 32)
Minus = GameSprite('minus.png', win_width //2 , win_height // 2 -50, 32, 32)
Minus_1 = GameSprite('minus.png', win_width //2 ,win_height // 2 +50, 32, 32)
bullets = sprite.Group()
bullets_1 = sprite.Group()
bullets_2 = sprite.Group()
bullets_e = sprite.Group()
monsters = sprite.Group()
monsters_1 = sprite.Group()
for i in range(1, 3):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
# mixer.music.play()
volume = 100
score = 0
lost = 0  
max_list = 3 
finish = False
run = True  
clock = time.Clock()
c = 1
able = 0
present = False
present_1 = False
present_a = True
present_1_a = True
collected = 0
starting = True 
S_Setting = False   
start = False
Difficulty = "Hard"
Dif = 3
B_b = True
Boss_health = 100
goal = 300
B_s = 100
p_s = 200
r = True
global BASICFONT
BASICFONT = font.Font(None, 24)
STARTFONT = font.Font(None, 35)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if c == 1:
                    ship.fire() 
                elif c == 2:
                    ship.fire_1()
                # mixer.music.load('shoot_1.ogg')
                elif c == 3:
                    ship.fire_2()
            elif e.key == K_1:
                frame_1 = Frame('Frame_1.png', 0, 100, 50, 50 )
                frame_2 = Frame('Frame.png', 50, 100, 50, 50 )
                frame_3 = Frame('Frame.png', 100, 100, 50, 50 )
                c = 1
            elif e.key == K_2:
                c = 0
                frame_1 = Frame('Frame.png', 0, 100, 50, 50 )
                frame_2 = Frame('Frame_1.png', 50, 100, 50, 50 )
                frame_3 = Frame('Frame.png', 100, 100, 50, 50 )
                if present_a == False:
                    c = 2
            elif e.key == K_3:
                c = 0
                frame_1 = Frame('Frame.png', 0, 100, 50, 50 )
                frame_3 = Frame('Frame_1.png', 100, 100, 50, 50 )
                frame_2 = Frame('Frame.png', 50, 100, 50, 50 )
                if present_1_a == False:
                    c = 3
       
                
        elif e.type == MOUSEBUTTONUP: 
                if Play.rect.collidepoint(e.pos):
                    if starting ==  True:
                            start = True
                            starting = False
                elif Options.rect.collidepoint(e.pos):
                    if starting == True:
                        S_Setting = True

                elif Back.rect.collidepoint(e.pos):
                    if S_Setting == True:
                        starting = True 
                        S_Setting = False

                elif Plus_1.rect.collidepoint(e.pos):
                    if S_Setting == True:
                        if volume < 100:
                            volume += 10
                elif Minus_1.rect.collidepoint(e.pos):
                    if S_Setting == True:
                        if volume > 0:
                            volume -= 10
                elif Plus.rect.collidepoint(e.pos):
                    if S_Setting == True:
                        if Dif <4:
                            Dif += 1
                elif Minus.rect.collidepoint(e.pos):
                    if S_Setting == True:
                        if Dif > 0:
                            Dif -= 1
                elif Exit.rect.collidepoint(e.pos):
                    if starting == True:
                        run = False
                elif Menu.rect.collidepoint(e.pos):
                    if start == True:
                        start = False
                        starting = True
               
    if not finish:
        if starting or S_Setting == True:
            window.blit(Base, (0, 0))
        if starting == True:
           
            Play.reset()
            Options.reset()
            Exit.reset()
        

        if S_Setting == True:
            starting = False
            Back.reset()
            Volume.reset()
            difficulty.reset()
            Minus.reset()
            Plus.reset()
            Minus_1.reset()
            Plus_1.reset()
            if Dif == 1:
                Difficulty = "Light"
            elif Dif == 2:
                Difficulty = "Medium"
            elif Dif ==3:
                Difficulty = "Hard"
            text = font_1.render("Volume: " + str(volume), None, "white" )
            window.blit(text, (500, 30))
            text_1 = font_1.render("Difficulty: " + str(Difficulty), None, "white" )
            window.blit(text_1 , (500, 50))



        if start == True:
            window.blit(background, (0, 0))
            text = font_1.render("Score " + str(score), None, "white" )
            window.blit(text, (500, 30   ))
            text_1 = font_1.render("Losts: " + str(lost), None, "white" )
            window.blit(text_1 , (500, 50))
            ship.update()
            ship.reset()
            Menu.reset()
            
            frame_1.reset()
            frame_2.reset()
            frame_3.reset()

            bullet_img.reset()
            if present_a == False:
                bullet_1_img.reset()       
            if present_1_a == False:
                bullet_2_img.reset()
            bullets.update()
            bullets.draw(window)
            bullets_1.update()
            bullets_1.draw(window)
            if c == 3:
                bullets_2.update()
                bullets_2.draw(window)
            # mixer.music.set_volume(volume // 100)
       
                    
            monsters.update()
            monsters.draw(window)
            monsters_1.update()
            monsters_1.draw(window)
            
            if Difficulty == "Hard":
                if len(monsters) <5:
                    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
                    monsters.add(monster)
                if score > 125:
                    
                    if len(monsters_1) <2:
                        monster_1 = Enemy(img_enemy_1, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
                        monsters_1.add(monster_1)
                
                B_s = 100
                p_s = 200
                goal = 300
            elif Difficulty == "Medium":
                if len(monsters) <3:
                    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
                    monsters.add(monster)
               
                if score > 125:
                    if len(bullets_e) <1:
                        bullet_e = Enemy(img_enemy, randint(win_width // 2 -150,win_width // 2 + 150 ), -80, 80, 50, randint(1, 5))
                        bullets_e.add(bullet_e)
                B_s = 50
                p_s = 100
                goal = 150
            elif Difficulty == "Light":
                if len(monsters) <2:
                    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
                    monsters.add(monster)
                
                B_s = 25
                p_s = 50
                goal = 75
                
            for bullet_e in bullets_e:
                    if sprite.spritecollide(ship, bullets_e, True):
                        
                        finish = True
            
         
            for monster in monsters:
                    if sprite.spritecollide(ship, monsters, True):
                  
                        
                        finish = True
                      
                    if sprite.groupcollide(bullets, monsters, True, True):
                  
                       
                        score += 1
                    if sprite.groupcollide(bullets_1, monsters, True, True):
                  
                      
                        score += 1
                    if sprite.groupcollide(bullets_2, monsters, False, True):
                        score += 1
                        
            for monster_1 in monsters_1:
                
                    if sprite.spritecollide(ship, monsters_1, True):
                 
                       
                        finish = True
                      
                    if sprite.groupcollide(bullets_1, monsters_1, True, True):
                        score += 2
                    if sprite.groupcollide(bullets, monsters_1, True, True):
                        able += 1
                        if able == 2:     
                            score += 2
                            able = 0
                    if sprite.groupcollide(bullets_2, monsters_1, False, True):    
                        score += 2
                        able = 0
            if score > goal:
                
                finish = True
            if score> p_s:
      
                if present_1_a == True:
                    bonus_1.reset()
                    bonus_1.update()
                    if sprite.collide_rect(ship, bonus_1):
                        collected = 2
                                
                        present_1_a = False
            if score > B_s and Boss_health > 0:
                
                    B_b == False  
                    Boss.update() 
                    Boss.reset()
                    if r == True:
                        for i in range(1, 4):
                            bullet_e = Enemy(img_bullet_e, randint(win_width // 2 -150,win_width // 2 + 150 ), -100, 20, 80, randint(1, 3))
                            bullets_e.add(bullet_e)
                        r = False
                    bullets_e.update()
                    bullets_e.draw(window)
                    if sprite.spritecollide(Boss, bullets, True):
                        Boss_health -= 10
                        
                    if sprite.spritecollide(Boss, bullets_1, True):
                        Boss_health -= 20
                       
            if Boss_health <= 0:
                present = True
                if present_a == True:
                    bonus.update()
                    bonus.reset()
                    if sprite.collide_rect(ship, bonus):
                        collected = 1
               
                        present_a = False
            
            if finish == True:
                reset()
                

    clock.tick(60)
    display.update()
