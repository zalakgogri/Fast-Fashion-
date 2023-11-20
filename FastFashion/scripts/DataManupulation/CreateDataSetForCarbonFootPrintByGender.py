import pandas as pd
import sys
sys.path.append( 'C:/Users/sonum/OneDrive/Desktop/FastFashion/scripts/GraphCode')
from GraphCode import BarGraph , LineGraph , PieChart

def main(data):
    findCarbonProducedGenderWise(data);

def findCarbonProducedGenderWise(data):
    gender = ['Male' , 'Female' , 'Others']

    maleCount = 0;
    femaleCount = 0;
    otherCount = 0;

    maleCrabonProduced = 0;
    femaleCrabonProduced = 0;
    othergenerationMCrabonProduced = 0;
    
    maleClothBought = 0;
    femaleClothBought = 0;
    otherClothBought = 0;

    for index in data.index:
        if data["Gender"][index] == 'Male':
            maleCount = maleCount + 1;
            maleCrabonProduced = maleCrabonProduced + data["carbonProduced"][index]
            maleClothBought = maleClothBought + data["TotalClothBought"][index]
        if data["Gender"][index] == 'Female':
            femaleCount = femaleCount + 1;
            femaleCrabonProduced = femaleCrabonProduced + data["carbonProduced"][index]
            femaleClothBought = femaleClothBought + data["TotalClothBought"][index]
        if data["Gender"][index] == 'Others':
            otherCount = otherCount + 1;
            othergenerationMCrabonProduced = othergenerationMCrabonProduced + data["carbonProduced"][index]
            otherClothBought = otherClothBought + data["TotalClothBought"][index]  
    
    if maleCount == 0 :
        maleCount = 1;
    if femaleCount == 0:
        femaleCount = 1;
    if otherCount == 0:
        otherCount = 1;

    genderCrabonProduced = [(maleCrabonProduced / maleCount) , (femaleCrabonProduced / femaleCount) , (othergenerationMCrabonProduced / otherCount)]
    genderClothProduced = [(maleClothBought / maleCount) , (femaleClothBought / femaleCount) , (otherClothBought / otherCount)]
    totalClothBought = [maleClothBought , femaleClothBought , otherClothBought];
    totalCount = [maleCount , femaleCount ,otherCount];
    
    dataCarbonProducedByGender = pd.DataFrame({'gender' : gender , 'genderCrabonProduced' : genderCrabonProduced , 'clothBought' : genderClothProduced , "totalClothBought" : totalClothBought , "totalCount" : totalCount})
    
    dataCarbonProducedByGender.to_csv('data\carbonProducedByGender.csv');
    
    # PieChart.drawPieChart(dataCarbonProducedByGender , 'gender' , 'genderCrabonProduced');

    print(dataCarbonProducedByGender);
