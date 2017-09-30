#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

#Handle characters out of range(128)
_u = lambda t: t.decode('UTF-8', 'replace') if isinstance(t, str) else t
_uu = lambda *tt: tuple(_u(t) for t in tt)

def createGraph(league,year):
    season = str(year) + '–' + str(year + 1)[-2:]
    url = 'https://en.wikipedia.org/wiki/' + season + '_' + league
    print url


    # url = 'https://en.wikipedia.org/wiki/2016–17_Premier_League'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    req = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(req).read()
    # exit(0)

    # html = open('2017–18 Premier League - Wikipedia.html','r').read()
    # html = open('2016–17 Bundesliga - Wikipedia.html', 'r').read()
    # data = html.read()
    soup = BeautifulSoup(html,'lxml')
    tds = soup.find_all("td")
    ths = soup.find_all("th")
    flag = False

    teams = []
    n = 0


    count = 0
    #The if conditions are according to the wiki page structure
    for th in ths:
        team = th.text.strip()
        str1 = _u(team)
        str2 = _u('Home \ Away')
        if flag:
            if len(team) != 3:
                break
            n += 1
        if str1 == str2:
            flag = True

    count = 0
    flag = False
    th_flag = True
    if n == 0:
        th_flag = False
    if not th_flag:
        for td in tds:
            team = td.text.strip()
            str1 = _u(team)
            str2 = _u('Home ╲ Away')
            if flag:
                team_check = team[:-4]
                team = team[:-5]
                if '!' in  team_check:
                    break
                teams.append(team)
                # if len(team) != 3:
                #     break
                n += 1
            if str1 == str2:
                flag = True
    else:
        for th in ths:
            team = th.text.strip()
            str1 = _u(team)
            str2 = _u('Home \ Away')
            if flag:
                count += 1
                if count <= (2 * n) and count > n:
                    teams.append(team)
                if count > 2 * n:
                    break
            if str1 == str2:
                flag = True

    count = 0
    adj = [[1000 for j in range(n)]for i in range(n)]
    score_matrix = [['-' for j in range(n)]for i in range(n)]
    flag = False

    if not th_flag:
        for td in tds:
            result = td.text.strip()
            str1 = _u(result)
            str2 = _u('Home ╲ Away')
            if flag and '!' not in result:
                count += 1
                home_id = (count - 1) / n
                away_id = (count - 1) % n
                if count == (n * n):
                    flag = False
                    break
                if str1 not in ['','a',str2]:
                    result = result.replace(u'\u2013','-')
                    home, away = result.split('-')
                    if int(home) > int(away):
                        if adj[home_id][away_id] == 1000:
                            adj[home_id][away_id] = 1
                        elif adj[home_id][away_id] == 1:
                            adj[home_id][away_id] = 2
                        # if adj[home_id][away_id] == 0:
                        #     adj[home_id][away_id] = int(home) - int(away)
                        #     score_matrix[home_id][away_id] = home + '-' + away
                        # elif adj[home_id][away_id] > int(home) - int(away):
                        #     adj[home_id][away_id] = int(home) - int(away)
                        #     score_matrix[home_id][away_id] = home + '-' + away
                    elif int(away) > int(home):
                        if adj[away_id][home_id] == 1000:
                            adj[away_id][home_id] = 1
                        elif adj[away_id][home_id] == 1:
                            adj[away_id][home_id] = 2
                        # if adj[away_id][home_id] == 0:
                        #     adj[away_id][home_id] = int(away) - int(home)
                        #     score_matrix[away_id][home_id] = away + '-' + home
                        # elif adj[away_id][home_id] > int(away) - int(home):
                        #     adj[away_id][home_id] = int(away) - int(home)
                        #     score_matrix[away_id][home_id] = away + '-' + home
            if str1 == str2:
                flag = True
    else:
        for td in tds:
            result = td.text.strip()
            str1 = _u(result)
            str2 = _u('—')
            if flag:
                count += 1
                home_id = (count - 1) / n
                away_id = (count - 1) % n
                if count == n * n:
                    flag = False
                    break
                if str1 not in ['','a',str2]:
                    result = result.replace(u'\u2013','-')
                    home, away = result.split('-')
                    if int(home) > int(away):
                        if adj[home_id][away_id] == 1000:
                            adj[home_id][away_id] = 1
                        elif adj[home_id][away_id] == 1:
                            adj[home_id][away_id] = 2
                        # if adj[home_id][away_id] == 0:
                        #     adj[home_id][away_id] = int(home) - int(away)
                        #     score_matrix[home_id][away_id] = home + '-' + away
                        # elif adj[home_id][away_id] > int(home) - int(away):
                        #     adj[home_id][away_id] = int(home) - int(away)
                        #     score_matrix[home_id][away_id] = home + '-' + away
                    elif int(away) > int(home):
                        if adj[away_id][home_id] == 1000:
                            adj[away_id][home_id] = 1
                        elif adj[away_id][home_id] == 1:
                            adj[away_id][home_id] = 2
                        # if adj[away_id][home_id] == 0:
                        #     adj[away_id][home_id] = int(away) - int(home)
                        #     score_matrix[away_id][home_id] = away + '-' + home
                        # elif adj[away_id][home_id] > int(away) - int(home):
                        #     adj[away_id][home_id] = int(away) - int(home)
                        #     score_matrix[away_id][home_id] = away + '-' + home
            if str1 == str2:
                flag = True

    return teams, adj

# leagues = ['Premier_League','Serie_A','La_Liga','Ligue_1','Bundesliga','Primeira_Liga']

