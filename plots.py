'''Helper functions for plotting'''

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

def bin_list(i, n, c=0):
    '''Generate a list of integers to define bins for plotting

    Keyword arguments:
    i -- size of bin
    n -- number of bins
    c -- center of bin range (default 0)
    Note that the number of bins must always be even.
    If n is odd, the number of bins will be n-1.
    for example bin_list(2,5,1) = [-3, -1, 1, 3, 5]
    '''
    b = int(n/2*-1)
    e = int((-1*b) + 1)
    return [ (x*i)+c for x in range(b,e)]
    
def bean_data(df, plot_group, plot_var, sort_on = None, sort_func = np.min, rev = False, bins = None):
    '''prepare labels and data for bean plot'''
    if bins is not None:
        plot_group = pd.cut(df[plot_group], bins)
    v_data = [[group,data] for group, data in df.groupby(plot_group)]
    if sort_on:
        v_data = sorted(v_data, key = lambda x: sort_func(x[1][sort_on]), reverse = rev)
    labels = []
    plot_data = []
    for row in v_data:
        data_series = row[1][plot_var].dropna()
        if len(data_series) > 2:
            labels.append(row[0])
            plot_data.append(data_series)
    return labels, plot_data
    
def draw_bplot(df, plot_group, plot_var, sort_by = None, sort_func = np.min, reverse = False, bins = None):
    '''draw bean plot from DataFrame given labels to groupby and plot'''
    labels, b_data = bean_data(df, plot_group, plot_var, sort_on = sort_by, sort_func = sort_func, rev = reverse, bins = bins)
    fig = plt.figure(figsize = (20,10))
    ax = fig.add_subplot(111)
    #labels = zip(labels, map(len, v_data))
    sm.graphics.beanplot(b_data, ax=ax, labels=labels,
                           plot_opts={'cutoff_val':2, 'cutoff_type':'abs',
                                       'label_fontsize':'small',
                                        'label_rotation':30})
    ax.set_xlabel(plot_group)
    ax.set_ylabel(plot_var)
    plt.show()