import generateGraph
import tsp
import dataScraper
import networkx
import hcycle

leagues = ['bundesliga']
           # 'ligue-1']

output = open('numc.csv','a+')

# adj = [[1000, 2, 1, 1, 1, 2, 1000, 2, 1, 1, 1000, 1000, 2, 2, 1000, 2, 1, 1000], [1000, 1000, 1000, 1, 1000, 1, 1000, 1000, 1, 1000, 1, 1000, 1, 1000, 1000, 1000, 1, 1], [1, 2, 1000, 1, 1000, 1, 2, 1, 1000, 2, 1000, 1, 1, 1, 1, 1, 1000, 1000], [1, 1, 1, 1000, 1000, 1, 1000, 1, 1000, 1000, 1, 1, 1, 1, 1, 1, 1, 1000], [1, 1, 1, 2, 1000, 1, 1, 2, 1, 1000, 1000, 1000, 1000, 2, 1000, 1, 2, 1], [1000, 1, 1000, 1, 1000, 1000, 1, 1000, 1, 1000, 1000, 1, 1, 2, 1000, 1, 1, 1000], [1, 2, 1000, 2, 1000, 1, 1000, 1000, 2, 1, 1, 1000, 1000, 1000, 1, 1, 1, 2], [1000, 2, 1, 1, 1000, 1, 1, 1000, 1000, 1000, 1000, 1000, 1000, 1, 2, 1000, 1000, 1], [1, 1, 2, 1, 1, 1, 1000, 1, 1000, 2, 1000, 1000, 2, 1000, 1, 1, 1, 1000], [1, 2, 1000, 2, 1000, 2, 1000, 1, 1000, 1000, 1000, 1000, 1, 1, 1000, 2, 1000, 1000], [1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1000, 1000, 1000, 1000, 1000, 1, 2, 1], [2, 2, 1000, 1, 1, 1, 1, 1, 1, 1, 2, 1000, 2, 1000, 1000, 1, 1, 2], [1000, 1000, 1, 1, 2, 1000, 2, 1, 1000, 1, 1, 1000, 1000, 1, 1000, 1, 1000, 1], [1000, 2, 1, 1, 1000, 1000, 1000, 1, 2, 1, 2, 2, 1000, 1000, 1000, 1000, 1000, 1000], [2, 1, 1000, 1, 1, 1, 1000, 1000, 1, 1, 1, 2, 1, 2, 1000, 1, 2, 1], [1000, 1000, 1, 1, 1000, 1, 1000, 1000, 1, 1000, 1, 1, 1000, 1, 1, 1000, 1000, 1], [1, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1000, 1000, 1, 2, 1000, 1000, 1000, 1000, 1000], [2, 1000, 1, 1000, 1000, 2, 1000, 1000, 1, 1, 1, 1000, 1000, 1, 1, 1000, 2, 1000]]
# cost, best_tour = tsp.held_karp(adj)
# print cost
# exit(0)

for year in range(2002, 2003, 1):
    # teams, adj, cost_matrix, score_matrix = generateGraph.getGraph(league, year)
    # print teams
    # for i in range(len(adj)):
    #     print adj[i]
    teams, adj = dataScraper.createGraph('La_Liga', year)
    count = 0
    cost, best_tour = tsp.held_karp(adj)
    print cost
    while cost < 1000:
        count += 1
        cost, best_tour = tsp.held_karp(adj)
        n = len(best_tour)
        for i in range(n):
            if adj[best_tour[i]][best_tour[(i + 1) % n]] == 2:
                adj[best_tour[i]][best_tour[(i + 1) % n]] = 1
            elif adj[best_tour[i]][best_tour[(i + 1) % n]] == 1:
                adj[best_tour[i]][best_tour[(i + 1) % n]] = 1000

    outputstr = 'la-liga' + ',' + str(year) + ',' + str(count)

    output.write(outputstr + '\n')
    print outputstr