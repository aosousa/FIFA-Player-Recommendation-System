import matplotlib.pyplot as plt
import pandas as pd

from collections import Counter
from datetime import datetime

def log_message(message):
    """Print message to the console with the current datetime

    Args:
        message: Message to print to the console
    """

    now = datetime.now()
    dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
    print('[{dt}] {msg}'.format(dt=dt_string, msg=message))

def plot_stat_distribution(stat: str, df: pd.DataFrame):
    """Plot distribution of a selected statistic (e.g., Overall, Potential)

    Args:
        df: Players DataFrame
    """
    
    ovr_counter = Counter(df[stat].values)
    
    range_length = list(range(max(df[stat].values)))
    data_series = {}

    for i in range(min(df[stat].values), len(range_length)+1):
        data_series[i] = 0

    for key, value in ovr_counter.items():
        data_series[key] = value

    data_series = pd.Series(data_series)
    x_values = data_series.index

    fig, ax = plt.subplots()
    rect = ax.bar(x_values, data_series.values)
    ax.set_ylabel('Count')
    ax.set_title('{stat} Distribution'.format(stat=stat))
    ax.bar_label(rect, padding=5)

    plt.xticks(x_values)
    plt.show()