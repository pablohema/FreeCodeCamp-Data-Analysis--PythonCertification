import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)


# Clean data
df = df.loc[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot

    # First solution:
    #fig = plt.figure(figsize=(20,9), dpi=120)
    #plt.plot(df, color='red')
    #plt.ylabel('Page Views')
    #plt.xlabel('Date')
    #plt.title('Daily freecodecamp forum page views 5/2016-12/2019')

    # Second solution:
    fig, ax = plt.subplots(figsize=(20,9), dpi=120)
    ax.plot(df.index, df['value'], 'r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    ## Draw bar plot

    fig = df_bar.plot.bar(xlabel='Years', ylabel='Average Page Views', legend=True, figsize=(15,9)).figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month_num'] = df_box['date'].dt.month

    df_box = df_box.sort_values('month_num')
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
    ax[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax = ax[0])
    ax[1] = sns.boxplot(x=df_box['month'], y=df_box['value'], ax = ax[1])

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return 