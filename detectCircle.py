import generateGraph
import tsp
import networkx
import hcycle

leagues = ['premier-league','la-liga','serie-a','bundesliga','ligue-1']

teams, adj, cost_matrix, score_matrix = generateGraph.getGraph(leagues[1],2015)
print teams
print score_matrix
cost, best_tour = tsp.held_karp(cost_matrix)
print best_tour

#
# print "Starting search"
#
# output = open('circlesofparity.csv','a+')
#
# for year in range(2013,2014,1):
#     teams, adj, cost_matrix, score_matrix = generateGraph.getGraph(leagues[3], year)
#     cost, best_tour = tsp.held_karp(cost_matrix)
#
#     outputstr = leagues[4] + ',' + str(year) + ',"' + str(teams) + '","' + str(best_tour) + '",' + str(cost)
#     print outputstr
#
#     output.write(outputstr + '\n')
#
# for league in leagues:
#     for year in range(2005,2017,1):
#         teams, adj, cost_matrix, score_matrix = generateGraph.getGraph(league, year)
#         cost, best_tour = tsp.held_karp(cost_matrix)
#
#         outputstr = league + ',' + str(year) + ',"' + str(teams) + '","' + str(best_tour) + '",' + str(cost)
#         print outputstr
#
#         output.write(outputstr + '\n')


