from django.shortcuts import render
import io
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import urllib, base64
import os
# Create your views here.

def load_table():
    plt.close()
    plt.style.use('ggplot')
    import matplotlib.lines as mlines
    pd.set_option('display.max_columns', None)
    yt = pd.read_csv('./main/statistic/GlobalYouTubeStatistics.csv', encoding='latin1', delimiter=";")
    yt.head(3)
    yt.describe()
    yt = yt.dropna()
    return yt

def lollipop_chart(filtered_yt, title):
    # Create base figure and axis
    fig, ax = plt.subplots(figsize=(9, 9))

        # Lollipop lines
    ax.vlines(x=filtered_yt['channel_type'], ymin=0, ymax=filtered_yt['video views'], color='gray', alpha=0.6)

        # Lollipop heads
    ax.scatter(filtered_yt['channel_type'], filtered_yt['video views'], color='blue', s=75, alpha=0.6)

        # Title & grid
    ax.set_title(title, fontdict={'size': 18})
    ax.grid(linestyle='--', alpha=0.6)
    ax.set_xlabel('Тип каналу')
    ax.set_ylabel('Перегляди відео')
    plt.xticks(rotation=45)
    return plt

def index(request):
    return render(request, 'index.html')


def subs(request):
    yt=load_table()
     # drop null values
    ### Діаграма розсіювання передплатників порівняно з переглядами відео ###
    sns.scatterplot(data=yt, x='subscribers', y='video views', color='blue').set(title='Підписки VS переглядів відео',
                                                                                 xlabel='Підписки (понад мільйона)',
                                                                                 ylabel='Перегляди відео (Мільярди)')
    plt.plot(range=10)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request,'subscribers.html', {'img': uri})


def most_popular(request):
    yt=load_table()
     # drop null values
    ### Діаграма розсіювання передплатників порівняно з переглядами відео ###
    sns.scatterplot(data=yt, x='subscribers', y='video views', color='blue').set(title='Підписки VS переглядів відео',
                                                                                 xlabel='Підписки (понад мільйона)',
                                                                                 ylabel='Перегляди відео (Мільярди)')
    filtered_yt = yt[yt['video views'] > 0]
    top_25_channel_types = filtered_yt.sort_values('video views', ascending=False).head(25)  # Топ 25 переглядів каналу

    lollipop_chart(top_25_channel_types, '25 найпопулярніших каналів за їх типом')
    plt.plot(range=15)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request,'most_popular.html', {'img': uri})



def last_25(request):
    yt=load_table()
    sns.scatterplot(data=yt, x='subscribers', y='video views', color='blue').set(title='Підписки VS переглядів відео',
                                                                                 xlabel='Підписки (понад мільйона)',
                                                                                 ylabel='Перегляди відео (Мільярди)')
    filtered_yt = yt[yt['video views'] > 0]
    bot_25_channel_types = filtered_yt.sort_values('video views', ascending = False).tail(25) #Останні 25 переглядів канал
    lollipop_chart(bot_25_channel_types, 'Останні 25 каналів, переглянутих за типом каналу')

    plt.plot(range=10)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)


    return render(request,'last_25.html', {'img': uri})


def type(request):
    yt=load_table()
    chan_type_pie = yt['channel_type'].value_counts() #Counting channel types
    plt.figure(figsize=(7, 7))
    chan_type_pie.plot(kind='pie', autopct='%1.2f%%') #Shows 2 decimal digits of %

    plt.plot(range=10)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'type.html', {'img': uri})


def most_popular_25(request):
    yt=load_table()

    plt.figure(figsize=(10, 10))
    yt_bp = sns.barplot(y='Youtuber',x='video views',data=yt,
                   order=yt.sort_values('video views',ascending=False).Youtuber.iloc[:25],palette='Spectral') #Top 25 channels
    plt.title('25 найпопулярніших каналів') #Title for graph
    yt_bp.set_xticklabels(['0b', '50b', '100b', '150b', '200b']) #Sets x labels


    plt.plot(range=20)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'most_popular_25.html', {'img': uri})


def popular(request):
    yt=load_table()

    chan_country_pie = yt['Country'].value_counts() #Counting Countries
    plt.figure(figsize=(9, 9))
    chan_country_pie.plot(kind='pie', autopct='%1.2f%%') #Shows 2 decimal digits of %


    plt.plot(range=10)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'popular.html', {'img': uri})

