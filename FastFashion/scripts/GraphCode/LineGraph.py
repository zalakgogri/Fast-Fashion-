import pandas as pd
import matplotlib.pyplot as plt 

def drawLineGraph(data , xAxisLabel , yAxisLabel , xLabel , yLabel , title): 
    plt.plot(data[xAxisLabel], data[yAxisLabel] , '--bo') 
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    
    plt.savefig(title);
    
    plt.show() 

