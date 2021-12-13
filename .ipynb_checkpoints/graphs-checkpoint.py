from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

class Graphs():
    
    def __init__(self):
        pass
    
    def graph_bar(self, title, title_x, title_y, data_x, data_y, label_y):
        fig, ax = plt.subplots()
        hbars = ax.barh(data_y, data_x, align='center')

        ax.set_yticks(ticks=data_y) #Note if you coppy tuts on line they have changed this so it needs to be done in two lines
        ax.set_yticklabels(label_y)
        ax.invert_yaxis()
        ax.set_ylabel(title_y)
        ax.set_xlabel(title_x)
        ax.set_title(title)

        for i in range(len(data_y)): #Adding Labels to the Graph
          plt.text(data_x[i]/2, i, data_x[i], ha='center', va = 'center', color='white', fontweight='bold')

        plt.show()