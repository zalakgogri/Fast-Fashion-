import pandas as pd
import matplotlib.pyplot as plt 
import BarGraph
from BarGraph import DrawBarGraph , DrawBarGraphForTwo
from PieChart import drawPieChart
from LineGraph import drawLineGraph

carbonProducedByGender = pd.read_csv('data\carbonProducedByGender.csv');
carbonProducedByGeneration = pd.read_csv('data\carbonProducedByGeneration.csv');

def main(data):
    BarGraph.bargraph(data);
    
    # generation - wise carbon footprint
    DrawBarGraphForTwo(data["generation"] , data["carbonProduced"] , data["TotalClothBought"] ,"generation" , "carbon produced per generation this year total (KgCO2e)" , "cloth bought per generation total (Number of items)" , " ");
    # gender - wise carbon footprint
    DrawBarGraphForTwo(carbonProducedByGender['gender'] , carbonProducedByGender['genderCrabonProduced'] , carbonProducedByGender['clothBought'] , "gender" , "carbon produced per gender this year total (KgCO2e)", "average number of cloths bought in this year" , "average total cloth bought and the carbon produced gender - wise this year");
    # number of gender 
    DrawBarGraph(carbonProducedByGender['gender'] , carbonProducedByGender['totalCount'] , "gender" , "number of participants of those genders" , "gender" , "count of people" , "number of participants of each gender");
    # number of generation
    DrawBarGraph(carbonProducedByGeneration['generationName'] , carbonProducedByGeneration['totalCount'] , "generation" , "number of participants of those generation" , "" , "generation count" , "number of participants of each generation");
    
    
    # PIE-CHART
        # gender wise carbon footprint (average)
    drawPieChart(carbonProducedByGender , 'gender' , 'genderCrabonProduced' , 'average footprint of each gender');
    drawPieChart(carbonProducedByGeneration , 'generationName' , 'carbonAverageProduced' , 'average footprint of each generation');
        
    # LINE-CHART
        # temporal change in carbon footprint
    drawLineGraph(carbonProducedByGeneration , "generation" , "carbonAverageProduced" , "Geneational Age" , "Average Carbon Footprint in clothing in kg CO2e" , "Generational trend in Carbon Footprint in terms of clothing")
        # change in cloth buying trend
    drawLineGraph(carbonProducedByGeneration , "generation" , "generationClothBought" , "Geneational Age" , "Average cloths bought" , "Generational trend in buying cloths total");
    
    # analysis based on gender 