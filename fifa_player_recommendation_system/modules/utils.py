import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from collections import Counter
from datetime import datetime
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def log_message(message):
    """Print message to the console with the current datetime

    Args:
        message: Message to print to the console
    """

    now = datetime.now()
    dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
    print('[{dt}] {msg}'.format(dt=dt_string, msg=message))

def plot_stat_distribution(df: pd.DataFrame, x: str):
    """Plot distribution of a selected statistic (e.g., Overall, Potential)

    Args:
        df: Players DataFrame
        x: What value to show in the X-axis
    """
    
    counter = Counter(df[x].values)
    data_series = {}

    for key, value in counter.items():
        data_series[key] = value

    data_series = pd.Series(data_series)
    x_values = data_series.index

    fig, ax = plt.subplots()
    rect = ax.bar(x_values, data_series.values)
    ax.set_ylabel('Count')
    ax.set_title('{x} Distribution'.format(x=x))
    ax.bar_label(rect, padding=5)

    plt.xticks(x_values)
    plt.show()

def generate_box_plot(df: pd.DataFrame, x: str, y: str):
    """Generate a box plot

    Args:
        df: Players DataFrame
        x: What value to show in the X-axis
        y: What value to show in the Y-axis
    """

    sns.boxplot(data=df, x=x, y=y)
    plt.show()

def generate_scatter_plot(df: pd.DataFrame, x: str, y: str):
    """Generate a scatter plot
    
    Args:
        df: Players DataFrame
        x: What value to show in the X-axis
        y: What value to show in the Y-axis
    """
    
    sns.scatterplot(data=df, x=x, y=y)
    plt.show()

def generate_distribution_plot(df: pd.DataFrame, x: str, hue: str):
    """Generate a distribution plot
    
    Args:
        df: Players DataFrame
        x: What value to show in the X-axis
        hue: What value to use in the plot's hue property
    """
    
    sns.displot(data=df, x=x, hue=hue)
    plt.xticks(rotation=90)
    plt.show()

def pca(df: pd.DataFrame):
    """Principal Component Analysis of the DataFrame

    Args:
        df: Player stats DataFrame
    """

    # data standardization
    data = StandardScaler().fit_transform(df)

    pca = PCA()
    pca.n_components = 38
    pca_data = pca.fit_transform(data)

    # percentage of variance explained by the components
    percentage_var_explained = pca.explained_variance_ / np.sum(pca.explained_variance_)

    # cumulative variance explained
    cumulative_var_explained = np.cumsum(percentage_var_explained)

    plt.figure(1, figsize=(6, 4))
    plt.plot(cumulative_var_explained, linewidth=2)
    plt.axis('tight')
    plt.grid()
    plt.xlabel('Principal components')
    plt.ylabel('Cumulative variance explained')
    plt.title('PCA: components selection')
    plt.show()