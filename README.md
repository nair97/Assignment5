# Environmental Informatics

## Assignment 05 - Graphical Analysis with Pandas

### Lab Objectives

On completion of this lab, students will be able to:

1. Use pandas DataFrames to conduct a graphical analysis of a dataset.
2. Generate a variety of figures as part of a graphical analysis of a new dataset.
3. Embed those figures into a test document, and write descriptive captions.

### Reading Assignment

Data Analysis with Open Source Tools:

- Chapter 1: Introduction
- Chapter 2: A single variable: Shape and distribution
- Chapter 3: Two Variables: Establishing Relationships

### Practical Practice

The following tutorials will be helpful for completing this lab.

- This tutorial introduces features of pandas and its dataframe data type work through the tutorial material as [10 minutes to pandas](see http://pandas.pydata.org/pandas-docs/stable/10min.html).
  - Pandas is a powerful tool for working with mixed type data, and likely to become your best friend when working with environmental data.
  - There are plenty of other training materials, but this will get you started.  We will work more with Pandas in later labs.
- For an introduction to the **seaborn module** and its application to graphical data analysis, one or both of these can be very useful:
  - [How to perform exploratory data analysis with seaborn](https://towardsdatascience.com/how-to-perform-exploratory-data-analysis-with-seaborn-97e3413e841d)
  - [The Ultimate Python Seaborn Tutorial: Gotta Catch ‘Em All](https://elitedatascience.com/python-seaborn-tutorial)
  - There are many others, but these cover enough to get you started, and highlight some of the techniques we have discussed in lecture - along with methods we have not discussed.

### The Lab Assignment

Start by cloning this repository and copying the file **template_Graphical_Data_Analysis.py** to the submission file name **Graphical_Data_Analysis.py**. 

Then download the data for this assignment as follows:

- Go to the [USGS earthquake hazards web site](http://earthquake.usgs.gov/earthquakes/feed/), scroll down to **Real-time Feeds** and click on  "Spreadsheet Format" to get the latest earthquake data in a CSV file. 

- On the next screen, scroll down until the heading "Past 30 Days" appears on the far right side.  Click on the link for "All Earthquakes". 

- This should download a file called **all_month.csv** to your default download directory.  Move the file into the assignment repository, so that it is in the same folder as the program **Graphical_Data_Analysis.py**. 

- You will need to document this process (including date and time of download) for your metadata file.

Next, modify the Python program to complete the following tasks:

1. Open and read the contents of the file into Python.

   - You will quickly find that the numpy function genfromtxt() will not work with this data file.  Why not?

   - The best option for reading this file will be to make use of the [read_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) method within the pandas module.  WARNING: there is also a method called read_table(), which does essentially the same thing as read_csv but sounds more general, and has been on the list of functions marked for depreciation for a long time - so just learn to use read_csv() instead.

   - Much of what you learned for working with numpy arrays last week will apply to dataframes as well, but there is a difference in how you index and slice them (an improvement over numpy structured arrays).

   - Don't worry about understanding date and time in pandas (or Python for that matter), we will not make use of that information in this assignment.  We will, however, focus on date and time concepts in an upcoming assignment.

   - The pandas dataframe is built to handle heterogeneous data (data that is not all the same), as opposed to numpy, which is designed for homogeneous data (data that is all the same).  It brings back more of the flexibility of Python lists, but is built relying on the more powerful numpy array data type.  Conceptually, it is similar to the dataframes used within the R statistics package (for example, see the [R Tutorial page on Data Frames](http://www.r-tutor.com/r-introduction/data-frame)).

2. Write Python functions to conduct the following graphical analysis of the data:

   - Generate a histogram of earthquake magnitude, using a bin width of 1 and a range of bins from 0 to 10. (hint: how does the selection of bin size and range affect what the histogram displays?  what does the histogram suggest about the distribution of the data?)
   
   - Generate a KDE plot for the same data. (hint: indicate selections for the kernel type and kernel width, and comment on similarities and differences between the histogram and the KDE plot)
   
   - Plot latitude versus longitude for all earthquakes.  (hint: comment on the distribution of those points.  be sure that you put longitude on the x-axis and latitude on the y-axis, why?)
   
   - Generate a normalized cumulative distribution plot of earthquake depths. (hint: comment on what this plot indicates about the distribution of earthquake depths)
   
   - Generate a scatter plot of earthquake magnitude (x-axis) with depth (y-axis). (hint: comment on how depth and magnitude are related)
   
   - Generate a quantile or Q-Q plot of the earthquake magnitudes.  (hint: what statistical distribution does your Q-Q plot assume? does your data comply with that distribution?)

3. All figure axis should be properly labeled, including correct units.  

4. Each function should export the figure generated as a TIFF file (e.g., <figure_name>.tif).

5. Be sure that the script has a complete header comment block, appropriate in-line comments, and runs without intervention.

#### What to turn in...

The following should be included in your GitHub repository:

1. The data file, **all_month.csv**,  downloaded from the [USGS earthquake hazards web site](http://earthquake.usgs.gov/earthquakes/feed/).

2. A working program called **Graphical_Data_Analysis.py**.

3. TIFF image files for each figure.

5. A metadata file called **Metadata.pdf**:

   - Use Word or a similar word processing program.
   - Describe the source and format of the input data (not more than half a page),
   - Describe the types of analysis conducted by your script (not more than half a page),
   - Import the graphical analysis figures (TIFF files) from your program, and write a caption that describes the figure and addresses the hints provided for each figure.
   - Captions should be consecutively numbered, and figure captions should be under the figure.
   - Convert the Metadata file into a PDF file prior to submission.

7. Put your input file, processing script and metadata file in the assignment repository and push to GitHub to submit.

#### Grading Rubric (50 pts Total)

| Question | Description | Score |
| -------- | ----------- | ----- |
| 1. | Provide a copy of the original earthquake data file | 4 pts |
| 2. | Working Program | (28 pts) |
| 2.1. | Use pandas to read file | 2 pts |
| 2.2. | Plot histogram of earthquake magnitude | 4 pts |
| 2.3. | Plot KDE plot of earthquake magnitude | 6 pts |
| 2.4. | Plot latitude versus longitude for all earthquakes | 4 pts |
| 2.5. | Plot normalized CDF of earthquake depths | 4 pts |
| 2.6. | Scatter plot of earthquake magnitude (X-axis) with depth (y-axis) | 4 pts |
| 2.7. | Q-Q plot of earthquake magnitudes | 4 pts |
| 3. | Program has clear and concise header and in-line comments | 4 pts |
| 4. | Metadata | (14 pts) |
| 4.1. | Includes provenance of earthquake data | 2 pts |
| 4.2. | Discuss why genfromtxt() will not work with this data file | 2 pts |
| 4.3. | Includes all figures generated by the program | 2 pts |
| 4.4. | Each figure includes a numbered caption that describes the figure and addresses the hints provided for each figure | 6 pts |
| 4.5. | Metadata is provided as a PDF | 2 pts |
