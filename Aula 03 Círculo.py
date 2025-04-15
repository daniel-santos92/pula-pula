import glfw
from OpenGL.GL import *
import numpy as np
import time

def eixos():
    glBegin(GL_LINES)
    glColor3f(1.0, 1, 1)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    glColor3f(1, 1.0, 1)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()

def circulo(raio, segmentos):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,1,0)
    for i in range(segmentos):
        angulo = 2.0 * np.pi * i / segmentos
        x = raio * np.cos(angulo)
        y = raio * np.sin(angulo)
        glVertex3f(x, y, 0)
    glEnd()

def triangulo(altura):
    glColor3f(0,0,0)
    glBegin(GL_TRIANGLES)
    glVertex3f(0,0, 0)
    glVertex3f(0.5,altura, 0)
    glVertex3f(0.5, -altura,0)
    glEnd()

def main():
    if not glfw.init():
        exit()

    janela = glfw.create_window(500, 500, "Minha janela", None, None)
    glfw.make_context_current(janela)

    glfw.swap_interval(1)

    while not glfw.window_should_close(janela):
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #eixos()
        circulo(0.5, 32)

        altura = 0.2 * np.sin(time.time()*7)
        triangulo(altura)

        glfw.swap_buffers(janela)
        glfw.poll_events()

    glfw.destroy_window(janela)
    glfw.terminate()

if __name__ == "__main__":
    main()