
# import ipdb
import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import MyPlotFunctions
import MyUtils

# ipdb.set_trace()

dataFilename = "data/All_three_exp_conditions_3.csv"
filename = "newFigures/figure4"
data = pd.read_csv(dataFilename, index_col=0)

print(data.columns.values)
# 'Expt #', 'Cell #', 'Speed', 'Bin(i)', 'Bin(i+1)', 'Bin(i+2)', 'Bin(i+3)', 
# 'Bin(i+4)', 'Bin(i+5)', 'Trial Condition', 'Region', 'Layer', 'Cell Type'

trialConditions = data.loc[:, "Trial Condition"].unique()
print(trialConditions)
# ['Vestibular' 'VisVes' 'Visual']

regions = data.loc[:, "Region"].unique()
print(regions)
# ['SUB' nan 'V1' 'SC' 'RSPg' 'RSPd' 'Hip']

# We will make a figure with len(trialConditions)==3 panels
f, axes = plt.subplots(1, len(trialConditions), sharey=True)

MyPlotFunctions.plotPanel(data, axes[0],'Vestibular')
MyPlotFunctions.plotPanel(data, axes[1], 'VisVes')
MyPlotFunctions.plotPanel(data, axes[2],'Visual')

MyUtils.mySaveFig(filename)
f.show()

# ipdb.set_trace()

