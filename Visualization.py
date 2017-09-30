import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plotNum():
    df = pd.read_csv('numc.csv')
    # print np.average((df['Circles'].loc[df['League'] == 'premier-league']).values)
    # print np.average((df['Circles'].loc[df['League'] == 'la-liga']).values)
    # print np.average((df['Circles'].loc[df['League'] == 'serie-a']).values)
    # print np.average((df['Circles'].loc[df['League'] == 'bundesliga']).values)
    plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])

    plt.plot((df['Year'].loc[df['League'] == 'premier-league']).values, (df['Circles'].loc[df['League'] == 'premier-league']).values)
    plt.plot((df['Year'].loc[df['League'] == 'la-liga']).values, (df['Circles'].loc[df['League'] == 'la-liga']).values)
    plt.plot((df['Year'].loc[df['League'] == 'serie-a']).values, (df['Circles'].loc[df['League'] == 'serie-a']).values)
    plt.plot((df['Year'].loc[df['League'] == 'bundesliga']).values, (df['Circles'].loc[df['League'] == 'bundesliga']).values)

    plt.legend(['EPL', 'La Liga', 'Serie A', 'Bundesliga'], loc='upper left')

    plt.show()

def plotDays():
    df = pd.read_csv('firstCircle.csv')
    sns.set_style(style='whitegrid')
    ax = sns.barplot(x="Year", y="Days", hue="League", data=df)
    plt.show()


