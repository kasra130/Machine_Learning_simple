# -*- coding: utf-8 -*-
"""Exercise1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OOW6axqN1KfwlukkwP_LzpoNEYvXwW0k
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




originalDataset = pd.read_csv('Energy_Usage_2010.csv') # load the CSV into python
originalDataset
originalDataset = originalDataset.dropna()  # inplace = true is similar to 
                                                # the numpy copy thing.
originalDataset.head() # head() displays a dataframe in the cell output
austinDataset = originalDataset[originalDataset['COMMUNITY AREA NAME'] == 'Austin']
austinDataset

"""Task 1 output :
1895
"""

#Task1
lines = len(austinDataset)  #Define length

print(lines)    #output length

"""Task 2 output :

No consol output, just a saved CSV file "Austin_Energy_Usage_2010.csv"
"""

#Task2 Austin_Energy_Usage_2010.csv
AUS = pd.DataFrame(austinDataset)     #defining dataset in pandas frame
AUS.to_csv('Austin_Energy_Usage_2010.csv')      #saving the file

"""Task 3 output :

******************Method1*************
***** Average electricity consumption in October 2010 :  7024.78839050132 KWH *****
Maximum KWH of December 501413.0 

******************Method2*****************

***** Average electricity consumption in October 2010 using ndarray :  7024.78839050132 KWH *****
Maximum KWH of December using ndarray 501413.0


"""

#Task3 Calculate the average electricity consumption of all buildings 
#in October 2010, Find the (1.5p)
#Method 1
#october 

import sys
np.set_printoptions(threshold=sys.maxsize)
print("******************Method1*************")
Ave = AUS["KWH OCTOBER 2010"].mean()     #Defining variabel Ave as avrage KWH consumed in October 2010
print("*****","Average electricity consumption in October 2010 : ",Ave , "KWH", "*****")

#Largest electricity consumption in December 2010 
#print(AUS["KWH DECEMBER 2010"]) #Locating specific december column 
Dec = (AUS["KWH DECEMBER 2010"])  # Defining the column as Dec
Max = Dec.max()     #Finidng the maximum value within the defined column 
print("Maximum KWH of December", Max, "\n")

#Method 2  
print("******************Method2*****************\n")  
oct_kwh_Array = AUS["KWH OCTOBER 2010"].values
oct_kwh_ave = np.mean(oct_kwh_Array)
print("*****","Average electricity consumption in October 2010 using ndarray : ",oct_kwh_ave , "KWH", "*****")
Dec_Array = AUS["KWH DECEMBER 2010"]
Maxnp = np.amax(Dec_Array)
print("Maximum KWH of December using ndarray", Maxnp)

"""Task 4 output: 
**********Method1***********

***** Average thermal consumption in October 2010 :  471.84591029023744 *****
Maximum THERM of December 28958.0
******************Method2*****************

***** Average Thermal consumption in October 2010 using ndarray :  471.84591029023744 *****
Maximum THERM of December using ndarray 28958.0
"""

#Task4 Same like question 3, but for thermals (1.5p)

print("**********Method1***********\n")
#october
AveT = AUS["THERM OCTOBER 2010"].mean()  #Definingv aribale  AveT as average thermal consumption of October 2010
print("*****","Average thermal consumption in October 2010 : ",AveT ,"*****")

#Largest thermal consumption in December 2010 
DecT = (AUS["THERM DECEMBER 2010"])  # Defining the column as Dec
MaxT = DecT.max()     #Finidng the maximum value within the defined column 
print("Maximum THERM of December", MaxT)


#Method 2  
print("******************Method2*****************\n")  
oct_THERM_Array = AUS["THERM OCTOBER 2010"].values
oct_THERM_ave = np.mean(oct_THERM_Array)
print("*****","Average Thermal consumption in October 2010 using ndarray : ", oct_THERM_ave, "*****")
DecT_Array = AUS["THERM DECEMBER 2010"]
Maxnp = np.amax(DecT_Array)
print("Maximum THERM of December using ndarray", Maxnp)

"""Task 5 output :
8 added column to the csv file 
[1895 rows x 81 columns]
"""

#Task5
#Add new columns to the dataframe: Lets say we have four seasons containing the corresponding months:

#Winter: January, February, December
#Spring: March, April, May
#Summer: June, July, August
#Autumn: September, October, November
#Add new columns to the end of the DataFrame that shows the KWH and Therms in each season by 
#adding up the months in each season. This means you need to add 8 more columms, 4 for KWH and 4 for Thermals. (3p)
#First I need to define the new columns by dragging the defined columns from AUS??
#Then I need to specify to drag both thermal and electrical data of each month 
#add up the data of each month and make a super season
#For each season we need KWH and THERM 

Winter_KWH = AUS["KWH DECEMBER 2010"] + AUS["KWH JANUARY 2010"] + AUS["KWH FEBRUARY 2010"] 
AUS["KWH average for Winter"] = Winter_KWH
Winter_THERM = AUS["THERM DECEMBER 2010"] + AUS["THERM JANUARY 2010"] + AUS["THERM FEBRUARY 2010"] 
AUS["THERMAL average for Winter"] = Winter_THERM

Spring_KWH = AUS["KWH MARCH 2010"] + AUS["KWH APRIL 2010"] + AUS["KWH MAY 2010"] 
AUS["KWH average for Spring"] = Spring_KWH
Spring_THERM = AUS["THERM MARCH 2010"] + AUS["TERM APRIL 2010"] + AUS["THERM MAY 2010"]
AUS["THERMAL average for Spring"] = Spring_THERM


Summer_KWH = AUS["KWH JUNE 2010"] + AUS["KWH JULY 2010"] + AUS["KWH AUGUST 2010"] 
AUS["KWH average for Summer"] = Summer_KWH
Summer_THERM = AUS["THERM JUNE 2010"] + AUS["THERM JULY 2010"] + AUS["THERM AUGUST 2010"]
AUS["THERMAL average for Summer"] = Summer_THERM 

Autumn_KWH = AUS["KWH SEPTEMBER 2010"] + AUS["KWH OCTOBER 2010"] + AUS["KWH NOVEMBER 2010"] 
AUS["KWH average for Autumn"] = Autumn_KWH
Autumn_THERM = AUS["THERM SEPTEMBER 2010"] + AUS["THERM OCTOBER 2010"] + AUS["THERM NOVEMBER 2010"] 
AUS["THERMAL average for Autumn"] = Autumn_THERM

AUS.to_csv('Austin_Energy_Usage_2010_Added_columns.csv')
print(AUS)

#Task6
print("Seasonal averages of KWH use on histogram\n")
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2) #defining the format in which histogram shall be printed at for KWH 4 seasons

ax0.hist(Winter_KWH, bins=100, histtype='bar',)      #Each season's histogram defined by an ax'n' . 
ax0.set_title('KWH winter')                                          #Title for each histogram

ax1.hist(Spring_KWH, bins=100, histtype='bar',)
ax1.set_title('KWH winter')

ax2.hist(Summer_KWH, bins=100, histtype='bar',)
ax2.set_title('KWH winter')

ax3.hist(Autumn_KWH, bins=100, histtype='bar',)
ax3.set_title('KWH winter')


fig.tight_layout()                                 #tight latyout 
plt.show()                        #exactly what it says , shows the figures


print("***********************************************************************************************\n")              
#Method is the same but for THERMAL consumption 
print("Seasonal averages of thermal use on histogram\n")

fig, ((ax4, ax5), (ax6, ax7)) = plt.subplots(nrows=2, ncols=2)

ax4.hist(Winter_THERM, bins=100, histtype='bar',)
ax4.set_title('THERM winter')

ax5.hist(Spring_THERM, bins=100, histtype='bar',)
ax5.set_title('THERM Spring')

ax6.hist(Summer_THERM, bins=100, histtype='bar',)
ax6.set_title('THERM Summer')

ax7.hist(Autumn_THERM, bins=100, histtype='bar',)
ax7.set_title('THERM Autumn')


fig.tight_layout()
plt.show()