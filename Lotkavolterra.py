#Code implemented from https://scientific-python.readthedocs.io/en/latest/notebooks_rst/3_Ordinary_Differential_Equations/02_Examples/Lotka_Volterra_model.html with minor alterations

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

alpha = .03 #birth rate of prey
beta = .02 #prey mortality rate
delta = .00014 #predator growth rate
gamma = .23 #predator death rate
x0 = 600 #prey (elk)
y0 = 7 #predator (wolf)
kappa = 0 #immigration rate in from Banff
b0 = 0. #banff

def derivative(X, t, alpha, beta, delta, gamma, kappa, b0):
    x, y = X
    dotx = (x * alpha - beta * y * x) + (kappa * b0)
    doty = (delta * x * y - gamma * y)
    return np.array([dotx, doty])

Nt = 2000
tmax = 600 #time
t = np.linspace(0.,tmax, Nt)
X0 = [x0, y0]
res = integrate.odeint(derivative, X0, t, args = (alpha, beta, delta, gamma, kappa, b0))
x, y = res.T


#plotting - two diff plots due to disparity in population b/w elk & wolf
# need to figure out how to make this actually look good

fig, (axs1, axs2) = plt.subplots(2)
axs1.plot(t, x, 'xb', label = 'Elk')
axs2.plot(t, y, '+r', label = 'Wolf')
axs1.set_ylabel("Prey Population Size")
axs2.set_ylabel("Population Population Size")
axs2.set_xlabel("Years after 1985")

plt.show()

#for displays when the gap in predator/prey is small enough to be shown on a single graph
##plt.figure()
####plt.plot(t, x, 'xb', label = 'Prey') plt.plot(t, y, '+r', label = "Predator") plt.xlabel('Time (years)') plt.ylabel('Population')
##plt.legend()

##plt.show()

#phase plane - for single DiffEQ where we get rid of T
##plt.figure()
##IC = np.linspace(40, 70, 4) # initial conditions for deer population (prey)
##for pred in IC:
    #X0 = [1000, pred]
    #Xs = integrate.odeint(derivative, X0, t, args = (alpha, beta, delta, gamma))
    #plt.plot(Xs[:,0], Xs[:,1], "-", label = "predator population ="+str(X0[1]))
#plt.xlabel("Prey")
#plt.ylabel("Predator")
#plt.legend()
#plt.title("Prey vs. Predator")
#plt.grid
#plt.show()

