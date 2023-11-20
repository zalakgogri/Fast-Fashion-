import pandas as pd
import sys
sys.path.append( 'C:/Users/sonum/OneDrive/Desktop/FastFashion/scripts/GraphCode')
from GraphCode import BarGraph , LineGraph


def main(data):
    findCarbonProducedAgeWise(data);

def findCarbonProducedAgeWise(data):
    generationName = ["Gen Z" , "Milleniums" , "Gen X" , "Boomers"]
    generation = [18.5 , 34.5 , 50.5 , 66.5]
    
    generationZClothBought = 0;
    generationXClothBought = 0;
    generationMClothBought = 0;
    generationBClothBought = 0;

    generationZ = 0;
    generationX = 0;
    generationM = 0;
    generationB = 0;

    generationZCrabonProduced = 0;
    generationXCrabonProduced = 0;
    generationMCrabonProduced = 0;
    generationBCrabonProduced = 0;

    for index in data.index:
        if data["AverageAge"][index] == 18.5:
            generationZ = generationZ + 1;
            generationZClothBought = generationZClothBought + data["TotalClothBought"][index];
            generationZCrabonProduced = generationZCrabonProduced + data["carbonProduced"][index]
        if data["AverageAge"][index] == 34.5:
            generationM = generationM + 1;
            generationMClothBought = generationMClothBought +  data["TotalClothBought"][index];
            generationMCrabonProduced = generationMCrabonProduced + data["carbonProduced"][index]
        if data["AverageAge"][index] == 50.5:
            generationX = generationX + 1;
            generationXClothBought = generationXClothBought +  data["TotalClothBought"][index];
            generationXCrabonProduced = generationXCrabonProduced + data["carbonProduced"][index]
        if data["AverageAge"][index] == 66.5:
            generationB = generationB + 1;
            generationBClothBought = generationBClothBought +  data["TotalClothBought"][index];
            generationBCrabonProduced = generationBCrabonProduced + data["carbonProduced"][index]

    generationCrabonProduced = [(generationZCrabonProduced / generationZ) , (generationMCrabonProduced / generationM) , (generationXCrabonProduced / generationX) , (generationBCrabonProduced / generationB)]
    generationClothBought = [(generationZClothBought / generationZ) , (generationMClothBought / generationM) , (generationXClothBought / generationX) , (generationBClothBought / generationB)]
    totalCount = [generationZ , generationM , generationX , generationB];
    
    dataCarbonProducedGeneration = pd.DataFrame({"generationName" : generationName , 'generation' : generation , 'carbonAverageProduced' : generationCrabonProduced , "generationClothBought" : generationClothBought , "totalCount" : totalCount});
    dataCarbonProducedGeneration.to_csv('data\carbonProducedByGeneration.csv');

    # LineGraph.drawLineGraph(dataCarbonProducedGeneration , 'generation' , 'carbonAverageProduced');