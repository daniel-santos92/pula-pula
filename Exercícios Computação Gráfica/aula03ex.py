import glfw
from OpenGL.GL import *
import numpy as np
import time

def eixos():
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1.0, 1, 1)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    glColor3f(1, 1.0, 1)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()

def triangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    glVertex3f(-0.5,-0.5,0)
    glColor3f(0, 1, 0)
    glVertex3f(0.5,-0.5,0)
    glColor3f(1, 0, 0)
    glVertex3f(0,0.5,0)
    glEnd()

desenha_em_linhas = False
def key_callback(window, key, scancode, action, mods):
    global desenha_em_linhas
    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        desenha_em_linhas = not desenha_em_linhas
def main():
    if not glfw.init():
        return

    janela = glfw.create_window(500, 500, "Minha janela", None, None)
    if not janela:
        glfw.terminate()
        return

    glfw.make_context_current(janela)
    glfw.set_key_callback(janela, key_callback)

    global desenha_em_linhas
    while not glfw.window_should_close(janela):
        glfw.poll_events()
        glClearColor(0, 0, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if desenha_em_linhas:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        triangulo()
        eixos()

        glfw.swap_buffers(janela)

    glfw.destroy_window(janela)
    glfw.terminate()

if __name__ == "__main__":
    main()