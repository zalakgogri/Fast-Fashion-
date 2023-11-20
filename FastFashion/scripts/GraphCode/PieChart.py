import pandas as pd
import matplotlib.pyplot as plt 

def drawPieChart(data , xAxisLabel , yAxisLabel , title):    
    plt.pie(data[yAxisLabel] , labels=(data[xAxisLabel]), autopct='%1.1f%%', startangle=140 )
    plt.title(title);
    plt.legend(data[xAxisLabel]);
    plt.axis('equal')
    plt.savefig(title)
    plt.show()
