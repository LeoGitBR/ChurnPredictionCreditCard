'''
This is a standard method I use for plot some charts

'''

# Warnings.
from warnings import filterwarnings
filterwarnings('ignore')

# Data manipulation and visualization.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


import sys


palette=sns.color_palette(['#023047', '#e85d04', '#0077b6', '#ff8200', '#0096c7', '#ff9c33'])


def plot_analysis (data, features, hist=True, colorPalette=palette, figsize=(24, 12)):
    '''
    Generate plots for data analysis
    -----------------------------------------------------------------------------------------------------------------------------------------
    Args:
        data: the dataframe
        features: the features to be plotted
        hist: when True, a histogram will be plotted
        colorPalette: Seaboarn.color_pallette. Default value already set as ['#023047', '#e85d04', '#0077b6', '#ff8200', '#0096c7', '#ff9c33']
        figSize: the plotty size. Default is (20,20)
    -----------------------------------------------------------------------------------------------------------------------------------------
    Returns:
        None
    '''
    
    # calculating number of rows
    num_columns = 3
    num_features = len(features)
    num_rows = num_features // num_columns + (num_features % num_columns > 0)
    
    
    fig, ax = plt.subplots(nrows=num_rows, ncols=num_columns, figsize=figsize)

    for i, feature in enumerate(features):
        row = i // num_columns
        col = i % num_columns
        
        ax = ax[row, col] if num_rows > 1 else ax[col] 
        
        sns.histplot(data=data, x=feature, ax=ax, stat='proportion')
        
        
    return None