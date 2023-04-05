ax = pl.figure(figsize = (15,12)).add_subplot(111, projection='3d')
ax.set_xlim([-10, 15])
ax.set_ylim([-30, 10])
ax.set_zlim([0, 30])
ax.set_yticks(np.arange(-30, 10, 10))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

for t in T:
    new_x,new_y,new_z = rossler(x0,y0,z0)
    t_t.append(t)

    ax.plot([x0, new_x], [y0, new_y], [z0, new_z], 'b-', linewidth=0.5)
        
    x0, y0, z0 = new_x, new_y, new_z


ax.scatter(0,0,0,color='red')

pl.show()


pl.plot(t_t,x_t,'.')
pl.ylabel("x")
pl.xlabel("t")
pl.grid(True)
pl.show()


pl.plot(t_t,y_t,'.')
pl.ylabel("y")
pl.xlabel("t")
pl.grid(True)
pl.show()

pl.plot(t_t,z_t,'.')
pl.ylabel("z")
pl.xlabel("t")
pl.grid(True)
pl.show()

