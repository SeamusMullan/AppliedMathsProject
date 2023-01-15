import numpy as np
import matplotlib.pyplot as plt

## Variables
# angle = np.deg2rad(23)      ## launch angle in degrees
g = 9.81                    ## gravity
u = 18.775                  ## initial velocity (x and y components follow)
ux = 17.277
uy = 7.345
sy = 2.75                   ## height of target (2.5 - 3 meters)
hSpread = 22                ## horizontal spread in degrees

dist = 47.5                 ## distance to target (45 - 50 meters)

## Revision 0
## calculate motion of projectile (equation)
xvals = []
yvals = []

def f(x):
    return (-x**2 + 47.5*x)/205

print(f(dist))

maxX = 0
maxY = 0

for x in np.arange(0, 47.5, .01):
    y = f(x)
    xvals.append(x)
    yvals.append(y)
    if y > maxY:
        maxY = y
        maxX = x

## line from player to max height
plt.plot((dist/2), sy, 'bo')
plt.plot(-9.14, 1.8, 'bo')

plt.plot((dist/2, -9.14), (sy, 1.8), 'b--')
## start angle @ 2.4 degrees

## plot 1
plt.plot(xvals, yvals, 'r', label='Projectile Motion')
plt.axhline(y=sy, color='b', linestyle="dotted", label='Max Height')
plt.xlabel('Distance X (m)')
# plt.xticks(np.arange(0, 30, 2))
plt.ylabel('Distance Y (m)')
# plt.yticks(np.arange(0, 3, .25))
plt.title('Clay Target Motion')

plt.legend()
plt.grid()
plt.show()
