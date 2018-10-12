import math
import matplotlib.pyplot as plt
import random
import tensorflow as tf

def min():
        for i in random(0,1):
            print(i)
min()
''' if __name__=="__main__":
    x=[float(i)/100.0 for i in range(1,300)]
    y=[math.log(i) for i in x]
    plt.plot(x,y,'r-',linewidth=3,label='Log carve')
    a=[x[20],x[175]]
    b=[y[20],y[175]]
    plt.plot(a,b,'g-',linewidth=2)
    plt.plot(a, b, 'b*', markersize=5,alpha=0.75)
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("log(x)")
    plt.show()
    '''