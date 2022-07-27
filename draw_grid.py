import numpy as np
import taichi as ti
grid_n = 10
dx = 1 / grid_n
dy = 1 / grid_n
def draw_grid():
    X = []
    Y = []
    for i in range(grid_n):
        X.append([dx*i,0])
        Y.append([dx*i,1])
    for i in range(grid_n):
        X.append([0, dy*i])
        Y.append([1, dy*i])
    X = np.array(X)
    Y = np.array(Y)
    gui.lines(begin=X, end=Y, radius=2, color=0x000000)

gui = ti.GUI("draw_grid", res=800, background_color=0xFFFFFF)

while gui.running:
    draw_grid()
    gui.show()
