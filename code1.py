from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

#Defining the function Rossler which returns the new values of x,y,z after time dt
def rossler(x,y,z):
    #updating the lists containing the values of x,y,z
    x_t.append(x) 
    y_t.append(y)
    z_t.append(z)

    #Finding the new values of x,y,z after time dt
    x_i = x + (-y - z) * dt
    y_i = y + (x + a*y) * dt
    z_i = z + (b + z*(x-c)) * dt

    return(x_i,y_i,z_i)

x_t = []
y_t = []
z_t = []
t_t = []

t_initial = 0.0
dt = 0.02
t_final = 60
T = np.arange(t_initial, t_final, dt)
a, b, c = 0.2, 0.2, 5.7

x0,y0,z0 = (0.0,-5.0,0.0)
