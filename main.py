"""This project is a training programm for Invoker~!"""
import pygame
import time
import random
import traceback
import sys

from pygame.locals import *

pygame.init()
pygame.time.delay(1000)
pygame.mixer.init()
bg_size = width, height = 500, 500
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('Invoker')
white = 255, 255, 255

background = pygame.image.load('images/background.jpg').convert()
none_image = pygame.image.load('images/none_image.png').convert_alpha()
Q = pygame.image.load('images/Quas_icon.png').convert_alpha()
W = pygame.image.load('images/Wex_icon.png').convert_alpha()
E = pygame.image.load('images/Exort_icon.png').convert_alpha()
WEE = pygame.image.load('images/Chaos_Meteor.png').convert_alpha()
QQQ = pygame.image.load('images/Cold_Snap.png').convert_alpha()
QWE = pygame.image.load('images/Deafening_Blast.png').convert_alpha()
WWW = pygame.image.load('images/EMP.png').convert_alpha()
QEE = pygame.image.load('images/Forge_Spirit.png').convert_alpha()
QQW = pygame.image.load('images/Ghost_Walk.png').convert_alpha()
QQE = pygame.image.load('images/Ice_Wall.png').convert_alpha()
EEE = pygame.image.load('images/Sun_Strike.png').convert_alpha()
QWW = pygame.image.load('images/Tornado.png').convert_alpha()
EWW = pygame.image.load('images/Alacrity.png').convert_alpha()
life_image = pygame.image.load('images/Life.png').convert_alpha()


pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.set_volume(0.3)
invoke_sound = pygame.mixer.Sound('sounds/invoke.wav')
invoke_sound.set_volume(0.2)
alacity_sound = pygame.mixer.Sound('sounds/Alacrity.mp3')
alacity_sound.set_volume(0.2)
chaos_meteor_sound = pygame.mixer.Sound('sounds/Chaos_meteor_cast.mp3')
chaos_meteor_sound.set_volume(0.2)
cold_snap_sound = pygame.mixer.Sound('sounds/cold_snap.mp3')
cold_snap_sound.set_volume(0.2)
Deafening_Blast_sound = pygame.mixer.Sound('sounds/Deafening_Blast.mp3')
Deafening_Blast_sound.set_volume(0.2)
EMP_sound = pygame.mixer.Sound('sounds/EMP_effect.mp3')
EMP_sound.set_volume(0.2)
forage_sound = pygame.mixer.Sound('sounds/forage.mp3')
forage_sound.set_volume(0.2)
ghost_walk_sound = pygame.mixer.Sound('sounds/Ghost_Walk.mp3')
ghost_walk_sound.set_volume(0.2)
ice_wall_sound = pygame.mixer.Sound('sounds/ice_wall.mp3')
ice_wall_sound.set_volume(0.2)
sun_strike_sound = pygame.mixer.Sound('sounds/Sun_Strike.mp3')
sun_strike_sound.set_volume(0.2)
Tornado_sound = pygame.mixer.Sound('sounds/Tornado_cast.mp3')
Tornado_sound.set_volume(0.2)

current_skill = [None, None, None]
element_list = {'Q': Q, 'E': E, 'W': W, None: none_image}
skill_list = {'EEE': EEE, 'EEW': WEE, 'QQQ': QQQ, 'EQW': QWE, 'WWW': WWW, \
              'EEQ': QEE, 'QQW': QQW, 'EQQ': QQE, 'QWW': QWW, 'EWW': EWW}
sounds_list = {'EEE': sun_strike_sound, 'EEW': chaos_meteor_sound, 'QQQ': cold_snap_sound,
               'EQW': Deafening_Blast_sound, 'WWW': EMP_sound, 'EEQ': forage_sound,
               'QQW': ghost_walk_sound, 'EQQ': ice_wall_sound, 'QWW': Tornado_sound,
               'EWW': alacity_sound}
skill_keys = list(skill_list.keys())
ave_time = []


# -----------some components for combo trainging -------------

# -----------some components for combo trainging -------------
def invoke(curren_list):
    if any(x is None for x in curren_list):
        #  There are less than three elements, cannot invoke!
        return ''
    return ''.join(sorted(curren_list))

def main():
    response_time = 0
    life = 3
    playing = True
    target = random.choice(skill_keys)
    time1 = time.clock()
    time_font = pygame.font.SysFont('arial', 36)
    while playing and life:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    current_skill.pop(0)
                    current_skill.append('Q')
                if event.key == K_w:
                    current_skill.pop(0)
                    current_skill.append('W')
                if event.key == K_e:
                    current_skill.pop(0)
                    current_skill.append('E')
                if event.key == K_r:
                    invoke_sound.play()
                    skill = invoke(current_skill)
                    time2 = time.clock()
                    response_time = time2 - time1
                    if target == skill:
                        sounds_list[skill].play()
                        target = random.choice(skill_keys)
                        time1 = time.clock()
                        ave_time.append(response_time)
                        screen.blit(skill_list[target], (225, 225))
                    else:
                        life -= 1
                        target = random.choice(skill_keys)
                        time1 = time.clock()
                        screen.blit(skill_list[target], (225, 225))
            if life:
                screen.blit(background, (0, 0))
                screen.blit(skill_list[target], (225, 225))
                element1_image = element_list[current_skill[0]]
                element2_image = element_list[current_skill[1]]
                element3_image = element_list[current_skill[2]]
                screen.blit(element1_image, (60, 350))
                screen.blit(element2_image, (186, 350))
                screen.blit(element3_image, (312, 350))
                time_text = time_font.render('Responsing time : ' + str(response_time), True, white)
                screen.blit(time_text, (10, 5))

            pygame.display.flip()


if __name__ == '__main__':
    pygame.mixer.music.play(-1)
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    print('Total successful responses are: ' + str(len(ave_time)))

    print('Your average responsing time is ' + str(sum(ave_time)/len(ave_time)) + 's')  # There is one situation where the sum is very big , and this method will result in a value error. Need to improve it.
