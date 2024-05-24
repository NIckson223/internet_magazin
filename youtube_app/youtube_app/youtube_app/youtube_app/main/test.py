import numpy as np
import pandas as pd
import matplotlib.pyplot as plt;
plt.style.use('ggplot')
import seaborn as sns
import matplotlib.lines as mlines
pd.set_option('display.max_columns', None)
yt = pd.read_csv('./statistic/GlobalYouTubeStatistics.csv', encoding='latin1', delimiter=";")
yt.head(3)
yt.describe()
yt = yt.dropna()  # drop null values
    ### Діаграма розсіювання передплатників порівняно з переглядами відео ###
sns.scatterplot(data=yt, x='subscribers', y='video views', color='pink').set(title='Підписки VS переглядів відео',
                                                                                 xlabel='Підписки (понад мільйона)',
                                                                                 ylabel='Перегляди відео (Мільярди)')
plt.show()