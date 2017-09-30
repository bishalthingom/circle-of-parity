#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
from datetime import datetime
import pandas as pd

def days_between(d1, d2):
    try:
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
    except:
        print d1,d2
    return abs((d2 - d1).days)

#Handle characters out of range(128)
_u = lambda t: t.decode('UTF-8', 'replace') if isinstance(t, str) else t
_uu = lambda *tt: tuple(_u(t) for t in tt)

def generateDf(url, ip_year):

    df = pd.DataFrame(columns=['Date', 'HomeTeam', 'HomeGoals', 'AwayGoals', 'AwayTeam'])
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    req = urllib2.Request(url, None, headers)
    data = urllib2.urlopen(req).readlines()
    #
    # html = open('Bundesliga Results | Sky Sports.html','r')
    # data = html.readlines()

    flag = False
    team_count = 0
    score_count = 0
    team_h = ''
    score_h = ''
    score_a = ''
    date_search = '<h4 class="fixres__header2">'
    team_search = '<span class="swap-text__target">'
    score_search = '<span class="matches__teamscores-side">'
    for index,line in enumerate(data):
        if date_search in line:
            flag = True
            soup = BeautifulSoup(line,'lxml')
            date = soup.find_all('h4')
            date = date[0].text.strip()
            day, date, month = date.split(' ')
            date = date[:-2]
            month = str(months.index(month) + 1)
            if len(month) == 1:
                month = '0' + str(month)
            if len(date) == 1:
                date = '0' + str(date)
            if int(month) < 6:
                year = ip_year + 1
            else:
                year = ip_year
            date = str(year) + '-' + str(month) + '-' + str(date)
        if flag and team_search in line:
            team_count = (team_count + 1) % 2
            soup = BeautifulSoup(line,'lxml')
            team = soup.find_all('span')
            team = team[0].text.strip()
            if team_count == 1:
                team_h = team
            else:
                team_a = team
                df = pd.DataFrame([[date, team_h, score_h, score_a, team_a]], columns=['Date','HomeTeam','HomeGoals','AwayGoals','AwayTeam']).append(df, ignore_index=True)
                # df = pd.concat([temp_df,df])
        if flag and score_search in line:
            score_count = (score_count + 1) % 2
            score_string = line + data[index + 1]
            soup = BeautifulSoup(score_string, 'lxml')
            score = soup.find_all('span')
            score = score[0].text.strip()
            if score_count == 1:
                score_h = score
            else:
                score_a = score

    return df

def getGraph(league, year):
    season = str(year) + '-' + str(year + 1)[-2:]
    url = 'http://www.skysports.com/' + league + '-results/' + season
    df = generateDf(url, year)

    home_teams = df['HomeTeam'].unique()
    away_teams = df['AwayTeam'].unique()

    start_date = df['Date'].min()

    teams = list(home_teams)
    teams.extend(x for x in away_teams if x not in teams)


    teams = sorted(teams)

    num = len(teams)
    adj_matrix = [[1000 for j in range(num)]for i in range(num)]
    cost_matrix = [[100000 for j in range(num)]for i in range(num)]
    score_matrix = [['-' for j in range(num)]for i in range(num)]
    degree_matrix = [0 for i in range(num)]

    for i in range(len(df)):
        # if df['Date'][i] > '2015-11-23':
        #     break
        if df['HomeGoals'][i] > df['AwayGoals'][i]:
            home_index = teams.index(df['HomeTeam'][i])
            away_index = teams.index(df['AwayTeam'][i])
            if adj_matrix[home_index][away_index] == 1000:
                adj_matrix[home_index][away_index] = 1
            elif adj_matrix[home_index][away_index] == 1:
                adj_matrix[home_index][away_index] = 2
            if cost_matrix[home_index][away_index] > days_between(df['Date'][i],start_date):
                cost_matrix[home_index][away_index] = days_between(df['Date'][i],start_date)
                score_matrix[home_index][away_index] = str(df['HomeGoals'][i]) + '-' + str(df['AwayGoals'][i])
            # df['HomeGoals'][i] - df['AwayGoals'][i]
            # edges.append((df['HomeTeam'][i],df['AwayTeam'][i]))
        elif df['HomeGoals'][i] < df['AwayGoals'][i]:
            # edges.append((df['AwayTeam'][i], df['HomeTeam'][i]))
            home_index = teams.index(df['HomeTeam'][i])
            away_index = teams.index(df['AwayTeam'][i])
            if adj_matrix[away_index][home_index] == 1000:
                adj_matrix[away_index][home_index] = 1
            elif adj_matrix[away_index][home_index] == 1:
                adj_matrix[away_index][home_index] = 2
            if cost_matrix[away_index][home_index] > days_between(df['Date'][i], start_date):
                cost_matrix[away_index][home_index] = days_between(df['Date'][i], start_date)
                score_matrix[away_index][home_index] = str(df['AwayGoals'][i]) + '-' + str(df['HomeGoals'][i])
            # df['AwayGoals'][i] - df['HomeGoals'][i]
    return teams, adj_matrix, cost_matrix, score_matrix

# getGraph('premier-league',2016)