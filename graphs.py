from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import math
from scipy.stats import gaussian_kde

class Graphs():
    
    def __init__(self):
        pass
    
    def graph_bar(self, title, title_x, title_y, data_x, label_y):
        data_y = np.arange(len(data_x))
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

    def graph_pie(self, title, data, labels):
        total = np.sum(data)
        if total > 1: #Check if data is in percent range
            for i in range(len(data)):
                data[i] = data[i] / total * 100
        fig1, ax1 = plt.subplots()

        text_args = dict(fontsize=10, weight='bold', color='black')  # Must use a dict to add text args
        # For usefull information about labelling https://stackoverflow.com/questions/53239733/matplotlib-move-labels-into-middle-of-pie-chart
        # https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py

        ax1.pie(data, labels=labels, shadow=True, autopct='%1.1f%%', textprops=text_args)
        ax1.set_title(title, bbox={'facecolor':'0.8', 'pad':5})

        plt.show()
        
    def graph_scatter(self, data_x, data_y, title="", best_fit=False):
        fig2, ax2 = plt.subplots()
        ax2 = sns.regplot(x=data_x, y=data_y, line_kws={"color":"r","alpha":0.7,"lw":3}, fit_reg=False)
        ax2.set_title(title)
        plt.show()
        
    def graph_box(self, data_x, title=""):
        fig3, ax3 = plt.subplots()
        ax3 = sns.boxplot(x=data_x)
        # ax3.boxplot(data_x)
        ax3.set_title(title)
        plt.show()
        
    def graph_density(self, data, title="", fill=False):
        plt.subplots()
        # Build a "density" function based on the dataset
        # When you give a value from the X axis to this function, it returns the according value on the Y axis
        density = gaussian_kde(data)
        density.covariance_factor = lambda : .25
        density._compute_covariance()
        
        # Create a vector of 200 values going from 0 to 8:
        length = max(data)-min(data)
        xs = np.linspace(0, math.ceil(length), math.ceil(length*20))
        # Make the chart
        # We're actually building a line chart where x values are set all along the axis and y value are
        # the corresponding values from the density function
        if fill:
            plt.fill_between(xs, density(xs), color="#69b3a2", alpha=0.4)
        else:
            plt.plot(xs,density(xs))
        plt.title(title)
        plt.show()
        
        #https://www.python-graph-gallery.com/density-chart-matplotlib
        
    def graph_violin(self):
        pass
        #https://www.python-graph-gallery.com/50-basic-violinplot-and-input-formats
        
    def graph_loli(self, data, title=""):
        x = range(1,len(data)+1)
        fig6, ax6 = plt.subplots()
        ax6.stem(x, data)
        plt.show()
        #https://www.python-graph-gallery.com/180-basic-lollipop-plot