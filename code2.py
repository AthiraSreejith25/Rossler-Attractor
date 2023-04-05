x_t = []
y_t = []
z_t = []
t_t = []

ax = pl.figure(figsize = (15,12)).add_subplot(111, projection='3d')
ax.set_xlim([-10, 15])
ax.set_ylim([-30, 10])
ax.set_zlim([0, 30])
ax.set_yticks(np.arange(-30, 10, 10))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

for y0 in np.arange(-8,-3,1.0): #setting different values of y0 in the initial condition
    x0, z0 = 0.0, 0.0
    
    for t in T:
        
        new_x,new_y,new_z = rossler(x0,y0,z0) #calculating new x,y,z
        t_t.append(t)

        ax.plot([x0, new_x], [y0, new_y], [z0, new_z], 'm-',alpha = 0.6, linewidth=0.3) #plotting the x,y,z values
            
        x0, y0, z0 = new_x, new_y, new_z #Updating the new values of x,y,z


ax.scatter(0,0,0,color='black') #plotting  the origin
pl.show()


pl.plot(x_t,y_t,'b.',alpha = 0.1)
pl.ylabel("y")
pl.xlabel("x")
pl.grid(True)
pl.show()

pl.plot(y_t,z_t,'b.',alpha = 0.3)
pl.ylabel("z")
pl.xlabel("y")
pl.grid(True)
pl.show()

pl.plot(x_t,z_t,'b.',alpha = 0.3)
pl.ylabel("x")
pl.xlabel("z")
pl.grid(True)
pl.show()


