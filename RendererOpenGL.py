from OpenGL.raw.GL.VERSION.GL_1_0 import GL_COLOR, GL_COLOR_BUFFER_BIT, glClear, glClearColor
import pygame
from pygame import mixer
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders
import glm

width = 960
height = 540

# Movimiento del objeto. 
deltaTime = 0.0



pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT )
clock = pygame.time.Clock()

# Posible fondo 
pygame.image.load('white.png')
pygame_icon =pygame.image.load('ash.png')
pygame.display.set_caption('MODEL VIEWER')
pygame.display.set_icon(pygame_icon)
by = pygame.Color("darkslategray3")


rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

face = Model('model.obj', 'earth.bmp')
face.position.z = -5
mixer.music.load('./Music/lifi.wav')
mixer.music.set_volume(0.7)
mixer.music.play(-1)

rend.scene.append( face )
rend.pointLight

isRunning = True
while isRunning:
    glClearColor(0.7, 1, 0, 1)
    
    keys = pygame.key.get_pressed()

    # Traslacion de camara en eje X
    if keys[K_d]:
        target = rend.scene[0].position
        rend.rotateRight(target, 2)
        #rend.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        target = rend.scene[0].position
        rend.rotateLeft(target, 2)
        #rend.camPosition.x -= 1 * deltaTime

    # Traslacion de camara en eje Y
    if keys[K_s]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_w]:
        rend.camPosition.y += 1 * deltaTime

    # Zoom In 
    if keys[K_UP]:
        rend.camPosition.z -= 1 * deltaTime
    # Zoom Out
    if keys[K_DOWN]:
        rend.camPosition.z += 1 * deltaTime


    # Hacer que explote el modelo 
    if keys[K_o]:
        if rend.valor > 0:
            rend.valor -= 0.1 * deltaTime

    if keys[K_p]:
        if rend.valor < 0.2:
            rend.valor += 0.1 * deltaTime

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_1:
                rend.filledMode()
            if ev.key == K_2:
                rend.wireframeMode()
            #Empiezan los shaders
            if ev.key == K_3:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader_v2)
            if ev.key == K_4:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader_v3)
            if ev.key == K_5:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader_v4)
            if ev.key == K_6:
                rend.setShaders(shaders.vertex_toon_shader, shaders.fragment_shader_v5)
            if ev.key == K_7:
                rend.scene.remove( face )
                face = Model('ufo.obj', 'a.jpg')
                face.position.z = -5 
                mixer.music.load('./Music/ufo.wav')
                mixer.music.set_volume(0.6)
                mixer.music.play(1)
                rend.scene.append( face )
            if ev.key == K_8:
                rend.scene.remove( face )
                face = Model('Pusheen.obj', 'Pusheen.png')
                face.position.z = -5 
                mixer.music.load('./Music/cat.wav')
                mixer.music.set_volume(0.6)
                mixer.music.play(1)
                rend.scene.append( face )
            if ev.key == K_9:
                rend.scene.remove( face )
                face = Model('spi.obj', 'a.png')
                face.position.z = -4
                mixer.music.load('./Music/spider.wav')
                mixer.music.set_volume(0.6)
                mixer.music.play(1)
                rend.scene.append( face )
            if ev.key == K_0:
                rend.scene.remove( face )
                face = Model('model.obj', 'earth.bmp')
                face.position.z = -3
                mixer.music.load('./Music/lifi.wav')
                mixer.music.set_volume(0.6)
                mixer.music.play(1) 
                rend.scene.append( face )
                

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()
    screen.fill(by)

    pygame.display.flip()


pygame.quit()
