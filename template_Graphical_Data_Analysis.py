"""
Replace with your own header comment
"""

# importing modules

def read_data( fileName ):
    # read in the contents of the data file and return a Pandas DataFrame

def generate_histogram_plot( dataFrame, outFileName ):
    # accept the dataframe and generate a histogram of earthquake magnitude 

    
def generate_kde_plot( dataFrame, outFileName ):
    # accept the dataframe and generate a KDE plot of earthquake magnitude 

def generate_lat_long_plot( dataFrame, outFileName ):
    # accept the dataframe and plot the location of eqrthquakes by longitude and latitude 

def generate_cdf_plot( dataFrame, outFileName ):
    # accept the dataframe and generate a normalized cdf of the earthquake depths
    
def generate_scatter_plot( dataFrame, outFileName ):
    # accept the dataframe and generate a scatter plot of earthquake magnitude vs depth

def generate_quantile_plot( dataFrame, outFileName ):
    # accept the dataframe and generate a quantile plot of earthquake magnitude

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

    # set input and output file names
    inFileName = 'all_month.csv'
    
    # open and read data file
    dataFrame = read_data( inFileName )
    
    # generate histogram figure
    #outHistName = "histogram.tif"
    #generate_histogram_plot( dataFrame, outHistName )

    # generate kde figure
    #outHistName = "kde.tif"
    #generate_kde_plot( dataFrame, outHistName )
    
    # generate lat-long figure
    #outHistName = "lat-long.tif"
    #generate_lat_long_plot( dataFrame, outHistName )

    # generate cdf figure
    #outHistName = "cdf.tif"
    #generate_cdf_plot( dataFrame, outHistName )
    
        
    # generate scatter plot figure
    #outHistName = "scatter.tif"
    #generate_scatter_plot( dataFrame, outHistName )
        
    # generate quantile figure
    #outHistName = "quantile.tif"
    #generate_quantile_plot( dataFrame, outHistName )
    