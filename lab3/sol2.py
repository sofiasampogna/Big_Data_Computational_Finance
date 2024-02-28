import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# plot the feasible region
d = np.linspace(-2,6,300)
x,y = np.meshgrid(d,d)
plt.imshow( ((y>=0) & (x>=0) & (y>=1-x) & (y>=x) & (y<=6-3*x)).astype(int) , 
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);


# plot the lines defining the constraints
x = np.linspace(0, 6, 2000)
# x2 >= 0
y1 = (x*0)+0 
# x1+x2 >=1 
y2 = 1-x
# x1-x2<=0 
y3 = x
# 3x1+x2 <= 6 
y4 = 6-3 * x


# Make plot
plt.plot(x, 0*np.ones_like(y1))
plt.plot(x, y2, label=r'$x_1+x_2\geq 1$')
plt.plot(x, y3, label=r'$x_1-x_2 \leq 0$')
plt.plot(x, y4, label=r'$3x_1+x_2 \leq 6$')
plt.xlim(0,6)
plt.ylim(0,6)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')