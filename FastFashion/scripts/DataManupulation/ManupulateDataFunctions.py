import pandas as pd
import sys
sys.path.append( 'C:/Users/sonum/OneDrive/Desktop/FastFashion/scripts/GraphCode')
from GraphCode import BarGraph
from DataManupulation import CreateDataSetForCarbonFootPrintByAge as cds
from DataManupulation import CreateDataSetForCarbonFootPrintByGender as cDsG

def manuplateDataMain(data):
    addAverageAgeAllGenerations(data);
    addCarbonGeneratedAllGeneration(data);
    addTotalClothBought(data);

    cDsG.main(data);
    cds.main(data);

    print(data);

def addCarbonGeneratedAllGeneration(data):
    data['carbonProduced'] = data["wool"] * 13.89  + data["cotton"] * 8.3 + data["linen"] * 4.5 + data["polyester"] * 6.4 + data["nylon"] * 7.31; 
    # BarGraph.DrawBarGraph(data["generation"] , data["carbonProduced"], "Generation" , "carbon produced by different generations due to fast fashion in kg Co2e" , "" , "" , "carbon footprint");

def addTotalClothBought(data):
    data['TotalClothBought'] = data["wool"] + data["cotton"] + data["linen"] + data["polyester"] + data["nylon"];

def addAverageAgeAllGenerations(data):
    data["AverageAge"] = [
        (26 + 11) / 2 if generation == "Gen Z (11 - 26)" else
        (42 + 27) / 2 if generation == "Millenials (27 - 42)" else
        (58 + 43) / 2 if generation == "Gen X (43 - 58)" else
        (50.5 + 16)
        for generation in data["generation"]
    ]