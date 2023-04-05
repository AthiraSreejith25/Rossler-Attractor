N    = 200000 #  of numerical iterations
burn =   8000  #  wait until hitting attractor


x,y,z = np.random.rand(), np.random.rand(), np.random.rand()

x_t = []
y_t = []
z_t = []
t_t = []

dt= 0.001     # time stepsize

#  Roessler parameters that are held fixed
a = 0.1
b = 0.1



cSteps = 60   #  Number of c values to iterate through
cs     = np.linspace(5, 10, cSteps) #list of c values
xVCs   = []  #  list of list of xValues at crossing

for c in cs:  # iterating through different values of c
    print(c)
    xValAtCross = []
    for n in range(1, N):
        x,y,z = rossler(x,y,z)

    if (n > burn) and ((y[n] > 0) and (y[n-1] < 0)):
  
            r = (0 - y[n-1]) / (y[n] - y[n-1])
            xValAtCross.append(x[n-1] + r*(x[n] - x[n-1]))



    xVCs.append(np.array(xValAtCross))
    pl.plot(x, y)   #plot of the attractor

ic  = 0


fig = pl.figure(figsize=(6, 2*4))




for c in cs:  # c from 5, 10 in 50 steps
    cValAtCross = np.ones(len(xVCs[ic])) * c   
    pl.scatter(cValAtCross, xVCs[ic], s=1)
    ic += 1

pl.xlabel("c")
pl.ylabel("x")
fig.add_subplot(2, 1, 2)

#  plot attractor at final value of c
pl.plot(x[burn:], y[burn:],'b')
pl.xlabel("x")
pl.ylabel("y")
pl.savefig("roessler_bifurcation2")
pl.close()
