#download all_month.csv from the USGS earthquake hazards web site and save
#read all_month.csv in read_csv to dataFrame
#define and plot functions
        generate_histogram_plot(dataFrame)
        generate_kde_plot(dataFrame)
        generate_lat_long_plot(dataFrame)
        generate_cdf_plot(dataFrame)
        generate_scatter_plot(dataFrame)
        generate_quantile_plot(dataFrame)

#build plots and format
#import and save plot graphs to TIF files
        savefig('histogram.tif')       
        savefig('kde.tif')
        savefig('lat-long.tif')
        savefig('cdf.tif')
        savefig('scatter.tif')
        savefig('quantile.tif')
                

The function np.genfromtxt() is used in Numpy to load data for simple homogenous
datasets and covers functions for missing values because the datasets are all same
and doesnt change, whereas the pandas dataframe is used to handle heterogeneous data,
which the datasets arent same always.
                
