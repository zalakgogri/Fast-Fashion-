import matplotlib.pyplot as plt 
import pandas as pd

carbonProduced = pd.read_csv('data\CarbonProduced.csv');

def bargraph(data):
    bargraphCotton(data);
    bargraphLinen(data);
    bargraphNylon(data);
    bargraphPolyster(data);
    bargraphWool(data);
    bargraphCarbonProduced();

def DrawBarGraph(xData , yData , xLabel , yLabel , xLegend , yLegend , title):
    plt.bar(xData , yData , color = "g" ,  width = 0.5 , label = yLabel);
    
    plt.xlabel(xLabel)    
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend([xLegend , yLegend])
    plt.savefig(title)
    plt.show()

def DrawBarGraphForTwo(xData , yData1 , yData2 , xLabel , yLabel1 , yLabel2 , title):
    plt.bar(xData , yData1 , color = "r" ,  width = 0.5 , label = yLabel1);
    plt.bar(xData , yData2 , color = "g" ,  width = 0.4 , label = yLabel2);
    
    plt.xlabel(xLabel)    
    plt.title(title)
    plt.legend()
    plt.savefig(title);
    plt.show()
    
def bargraphCotton(data):
    plt.bar(data["generation"], data["cotton"] * 8.3 , color = "r" ,  width = 0.5 , label = "carbon produced total (In Kg)");
    plt.bar(data["generation"], data["cotton"] , color = 'g' , width = 0.4 ,  label = "cotton bought (In number of Items)");

    plt.xlabel("Generation")    
    plt.title("Cotton Cloth Bought and the carbon produced")
    plt.legend()
    
    plt.savefig("Cotton Cloth Bought and the carbon produced");
    plt.show()

def bargraphWool(data):
    plt.bar(data["generation"], data["wool"] * 13.89 , color = "r" ,  width = 0.5 , label = "carbon produced total (In Kg)");
    plt.bar(data["generation"], data["wool"] , color = 'g' , width = 0.4 ,  label = "cotton bought (In number of Items)");

    plt.xlabel("Generation")
    plt.title("wool Cloth Bought and the carbon produced")
    plt.legend();
    plt.savefig("wool Cloth Bought and the carbon produced")
    plt.show()    

def bargraphPolyster(data):
    plt.bar(data["generation"], data["polyester"] * 6.4 , color = "r" ,  width = 0.5 , label = "carbon produced total (In Kg)");
    plt.bar(data["generation"], data["polyester"] , color = 'g' , width = 0.4 ,  label = "polyester bought (In number of Items)");

    plt.xlabel("Generation")
    plt.title("polyester Cloth Bought and the carbon produced")
    plt.legend();
    plt.savefig("polyester Cloth Bought and the carbon produced");
    plt.show()  

def bargraphNylon(data):
    plt.bar(data["generation"], data["nylon"] * 7.31 , color = "r" ,  width = 0.5 , label = "carbon produced total (In Kg)");
    plt.bar(data["generation"], data["nylon"] , color = 'g' , width = 0.4 ,  label = "nylon bought (In number of Items)");

    plt.xlabel("Generation")
    plt.title("nylon Cloth Bought and the carbon produced")
    plt.legend();
    plt.savefig("nylon Cloth Bought and the carbon produced")
    plt.show() 

def bargraphLinen(data):
    plt.bar(data["generation"], data["linen"] * 4.5 , color = "r" ,  width = 0.5 , label = "carbon produced total (In Kg)");
    plt.bar(data["generation"], data["linen"] , color = 'g' , width = 0.4 ,  label = "linen bought (In number of Items)");

    plt.xlabel("Generation")
    plt.title("linen Cloth Bought and the carbon produced")
    plt.legend();
    plt.savefig("linen Cloth Bought and the carbon produced");
    plt.show()  

def bargraphCarbonProduced():
    plt.bar(carbonProduced.columns , carbonProduced.iloc[0], color = "g" ,  width = 0.5 , label = "carbon produced total (In Kg)");
   
    plt.xlabel("Type of clothing produced")
    plt.ylabel("Carbon produced (assuming the cloth size is medium (40 inches)) in Kg")
    plt.title("Cloth type and the carbon produced")
    plt.legend();
    plt.savefig("Cloth type and the carbon produced");
    plt.show()  