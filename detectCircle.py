import generateGraph
import tsp

leagues = ['premier-league','la-liga','serie-a','bundesliga','ligue-1']

output = open('circlesofparity.csv','a+')

for league in leagues:
    for year in range(2005,2017,1):
        teams, adj, cost_matrix, score_matrix = generateGraph.getGraph(league, year)
        cost, best_tour = tsp.held_karp(cost_matrix)

        outputstr = league + ',' + str(year) + ',"' + str(teams) + '","' + str(best_tour) + '",' + str(cost)
        print outputstr

        output.write(outputstr + '\n')


