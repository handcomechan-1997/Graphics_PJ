# coding=gbk
import warnings
warnings.simplefilter("ignore", DeprecationWarning)
import pyaudio
import wave

import numpy as np
import pygame
from pygame.locals import *


CHUNK = 1024

wf = wave.open("test1.wav", 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)


data = wf.readframes(CHUNK)
pygame.init()

pygame.display.set_caption('音乐可视化')
screen = pygame.display.set_mode((840, 400), 0, 32)
bg = pygame.image.load('zelda2.jpg')
while data != '':

    stream.write(data)
    data = wf.readframes(CHUNK)
    numpydata = np.fromstring(data, dtype=np.int16)
    transforamed=np.real(np.fft.fft(numpydata))

    screen.fill((123, 82, 92))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    count=50
    screen.blit(bg, (0, 0))
    for n in range(0,transforamed.size,count):
        hight=abs(int(transforamed[n]/10000))

        pygame.draw.rect(screen,(127,255,212),Rect((20*n/count,400),(20,-hight*3)))
    pygame.display.update()

stream.stop_stream()
stream.close()
p.terminate()

