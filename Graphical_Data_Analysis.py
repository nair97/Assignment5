#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:29:38 2020

@author: meerarakesh09
"""

# importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

 # read in the contents of the data file and return a Pandas DataFrame
def read_data( fileName ):
    
    dataFrame = pd.read_csv('all_month.csv', index_col=0, sep = ',', na_filter = True)
    
    return dataFrame

# accept the dataframe and generate a histogram of earthquake magnitude 
def generate_histogram_plot( dataFrame, outFileName ):
    
    #plot the histogram 
    plt.hist(dataFrame['mag'].dropna(),bins = 10,range=[0,10])
    
    #label the axis and title of the graph
    plt.xlabel('Magnitude',fontsize=10)
    plt.ylabel('Measured Frequency Reading',fontsize=10)
    plt.title('Earthquake Magnitude Histogram',fontsize=15)
    
    #save the file in .tif 
    plt.savefig('histogram.tif')
    # Display Histogram
    plt.show()
    #close the file
    plt.close()
    
 # accept the dataframe and generate a KDE plot of earthquake magnitude 
def generate_kde_plot( dataFrame, outFileName ):
	
    #plot KDE graph
    sns.kdeplot(dataFrame['mag'].dropna(),color='b', shade=True)
    
    #label the axis and title of graph
    plt.xlabel('Magnitude',fontsize=10)  
    plt.ylabel('Reading Strength', fontsize=10)  
    plt.title('KDE of Earthquake Magnitude',fontsize=15)
   
    #save the file in .tif and close the file
    plt.savefig('kde.tif')
    # Display KDE
    plt.show()
    #close the file
    plt.close()
    
# accept the dataframe and plot the location of eqrthquakes by longitude and latitude 
def generate_lat_long_plot( dataFrame, outFileName ):

    plt.scatter(dataFrame['longitude'].dropna(), dataFrame['latitude'].dropna(), marker='+',color = 'r')
   
    #label the axis and title 
    plt.xlabel('Longitude', fontsize=10)  
    plt.ylabel('Latitude', fontsize=10) 
    plt.title('Longitude v/s Latitude of all Earthquakes',fontsize=15)
    
     #save the file in .tif 
    plt.savefig('lat-long.tif')
    # Display Lat-Long graph
    plt.show()
    #close the file
    plt.close()

# accept the dataframe and generate a normalized cdf of the earthquake depths
def generate_cdf_plot( dataFrame, outFileName ):
    
    plt.hist(dataFrame['mag'].dropna(), cumulative=True, density=1, color='tab:orange')
    
    #label the axis and title 
    plt.xlabel('Magnitude values', fontsize=10)  
    plt.ylabel('CDF', fontsize=10) 
    plt.title('Normalized CDF of Earthquake depths',fontsize=15)
    
     #save the file in .tif 
    plt.savefig('cdf.tif')
    # Display CDF
    plt.show()
    #close the file
    plt.close()
    
# accept the dataframe and generate a scatter plot of earthquake magnitude vs depth
def generate_scatter_plot( dataFrame, outFileName ):
    
    plt.scatter(dataFrame['mag'],dataFrame['depth'], color = 'g', marker = '.')

# Label Axes
    plt.xlabel('Magnitude')
    plt.ylabel('Depth')
    plt.title('Earthquake Magnitude vs. Depth')
    
     #save the file in .tif 
    plt.savefig('scatter.tif')
    # Display Scatter
    plt.show()
    #close the file
    plt.close()

 # accept the dataframe and generate a quantile plot of earthquake magnitude
def generate_quantile_plot( dataFrame, outFileName ):
   
    stats.probplot(dataFrame['mag'].dropna(), dist="norm", plot=plt)
    
    # Label Axes
    plt.xlabel('Theoretical Quantile', fontsize=10)
    plt.ylabel('Data Quantile', fontsize=10)
    plt.title("The  QQ-plot of Earthquake magnitude", fontsize=15)
    
     #save the file in .tif 
    plt.savefig('quantile.tif')
    # Display Quantile
    plt.show()
    #close the file
    plt.close()

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

 # set input and output file names
     inFileName = 'all_month.csv'
    
# open and read data file
     dataFrame = read_data( inFileName )
    
# generate histogram figure
     print('The histogram of Earthquake magnitude \n')
     outHistName = 'histogram.tif'
     generate_histogram_plot( dataFrame, outHistName )
 
# generate kde figure
     print('The KDE of Earthquake magnitude \n')
     outHistName = 'kde.tif'
     generate_kde_plot( dataFrame, outHistName )
     
# generate lat-long figure
     print('The Longitude and Latitudes of Earthquake magnitude \n')
     outHistName = 'lat-long.tif'
     generate_lat_long_plot( dataFrame, outHistName )

# generate cdf figure
     print('The normalized CDF of Earthquake depths \n')
     outHistName = "cdf.tif"
     generate_cdf_plot( dataFrame, outHistName )
     
# generate scatter plot figure
     print('The Scatter plot of Earthquake magnitude and depths \n')
     outHistName = "scatter.tif"
     generate_scatter_plot( dataFrame, outHistName )
     
# generate quantile figure
     print('The Quantile plot of Earthquake magnitude \n')
     outHistName = "quantile.tif"
     generate_quantile_plot( dataFrame, outHistName )
  