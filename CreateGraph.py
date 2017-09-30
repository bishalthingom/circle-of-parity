import pandas as pd
import pprint
import tsp
import datetime
import time
import dataScraper

dataScraper.createGraph()

df = pd.read_csv('epl2015_2016.csv', quotechar="\"")


adj_matrix = [[0 for j in range(20)]for i in range(20)]
degree_matrix = [0 for i in range(20)]

teams = ["Arsenal","Aston Villa","Bournemouth","Chelsea","Crystal Palace","Everton","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United","Norwich City","Southampton","Stoke City","Sunderland","Swansea City","Tottenham Hotspur","Watford","West Bromwich Albion","West Ham United"]

for i in range(len(df)):
    if df['home_team_goal'][i] > df['away_team_goal'][i]:
        home_index = teams.index(df['home_team_long_name'][i])
        away_index = teams.index(df['away_team_long_name'][i])
        if adj_matrix[home_index][away_index] == 0:
            adj_matrix[home_index][away_index] = df['home_team_goal'][i] - df['away_team_goal'][i]
        elif adj_matrix[home_index][away_index] > df['home_team_goal'][i] - df['away_team_goal'][i]:
            adj_matrix[home_index][away_index] = df['home_team_goal'][i] - df['away_team_goal'][i]
        # edges.append((df['home_team_long_name'][i],df['away_team_long_name'][i]))
    elif df['home_team_goal'][i] < df['away_team_goal'][i]:
        # edges.append((df['away_team_long_name'][i], df['home_team_long_name'][i]))
        home_index = teams.index(df['home_team_long_name'][i])
        away_index = teams.index(df['away_team_long_name'][i])
        if adj_matrix[away_index][home_index] == 0:
            adj_matrix[away_index][home_index] = df['away_team_goal'][i] - df['home_team_goal'][i]
        elif adj_matrix[away_index][home_index] > df['away_team_goal'][i] - df['home_team_goal'][i]:
            adj_matrix[away_index][home_index] = df['away_team_goal'][i] - df['home_team_goal'][i]

print adj_matrix
exit(0)

for i in range(20):
    degree_matrix[i] = sum(1 for j in adj_matrix[i] if j < 10000 and j > 0)
print adj_matrix
print degree_matrix
print degree_matrix.index(min(degree_matrix))
if min(degree_matrix) == 0:
    print "Impossible to find."
    exit(0)

start = time.time()
print tsp.tsp_dp_solve(adj_matrix)
end = time.time()

print "Ran for " + str(end-start)

degree_teams = [[teams[i],degree_matrix[i]]for i in range(20)]

degree_teams.sort(key=lambda x: x[1])

print degree_teams

teams = [degree_teams[i][0] for i in range(20)]

print teams

adj_matrix = [[100 if j != i else 0 for j in range(20)]for i in range(20)]
degree_matrix = [0 for i in range(20)]

for i in range(len(df)):
    if df['home_team_goal'][i] > df['away_team_goal'][i]:
        home_index = teams.index(df['home_team_long_name'][i])
        away_index = teams.index(df['away_team_long_name'][i])
        adj_matrix[home_index][away_index] = df['home_team_goal'][i] - df['away_team_goal'][i]
        # edges.append((df['home_team_long_name'][i],df['away_team_long_name'][i]))
    elif df['home_team_goal'][i] < df['away_team_goal'][i]:
        # edges.append((df['away_team_long_name'][i], df['home_team_long_name'][i]))
        home_index = teams.index(df['home_team_long_name'][i])
        away_index = teams.index(df['away_team_long_name'][i])
        adj_matrix[away_index][home_index] = df['away_team_goal'][i] - df['home_team_goal'][i]

for i in range(20):
    degree_matrix[i] = sum(1 for j in adj_matrix[i] if j < 100 and j > 0)
print adj_matrix
print degree_matrix

start = time.time()
# print tsp.tsp_dp_solve(adj_matrix)
end = time.time()

print "Ran for " + str(end-start)
