import numpy as np
import matplotlib.pyplot as plt

def min_max_plot(A, B, cityName):
    plt.subplot(1,1,1)
    X = np.linspace(1, 365, 365, endpoint=True)
    plt.plot(X, A, color="blue", label = "Min Temp")
    plt.plot(X, B, color="red", label = "Max Temp")
    plt.legend(loc='upper left')
    ax = plt.gca() 
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(8)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

    ax.set_xlabel('Days', color='black', fontsize=14)
    ax.set_ylabel('Temperature', color='black', fontsize=14)
    plt.title('Min/Max Daily Temperatures in 2015 for '+cityName, color="black", fontsize=14)    
    return plt
