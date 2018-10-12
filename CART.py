import numpy as np
import matplotlib.pyplot as plt

def entropy(p):
    return -p*np.log(p)-(1-p)*np.log(1-p)
def fun(p):
    return -2*p*p+2
x=np.linspace(0.01,0.99,200)
plt.plot(x,fun(x))
plt.show()

def split(x,y,d,value):
    index_a=(x[:,d]<=value)
    index_b=(x[:,d]>value)
    return x[index_a],x[index_a],y[index_a],y[index_b]
def try_split(x,y):
    best_entropy=float("inf")
