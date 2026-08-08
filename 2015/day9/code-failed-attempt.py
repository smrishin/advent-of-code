from typing import List, Tuple, DefaultDict, Dict
from collections import defaultdict
from copy import deepcopy
import heapq

REDUCED_MATRIX = []
REDUCED_COST = 0

def print_matrix(matrix):
    n = len(matrix)
    for r in range(n):
        row = ""
        for c in range(n):
            row += str(matrix[r][c]) + "\t"

        print(row)

def build_adj_matrix(graph, location_ids, n):
    matrix = [[float('inf')] * n for _ in range(n)] 

    for source, neighbours in graph.items():
        for dest, dist in neighbours:
            matrix[location_ids[source]][location_ids[dest]] = dist

    return matrix

def reduce_matrix(matrix, n):
    r_sum = 0
    c_sum = 0
    for r in range(n):
        min_dist = min(matrix[r])
        if min_dist == float('inf'):
            continue
        r_sum += min_dist
        for c in range(n):
            matrix[r][c] -= min_dist
    # print(matrix)

    for c in range(n):
        min_dist = min([matrix[x][c] for x in range(n)])
        if min_dist == float('inf'):
            continue
        c_sum += min_dist
        for r in range(n):
            matrix[r][c] -= min_dist
    return matrix, r_sum + c_sum
    

def shortest_distance(curr_matrix, source, dest, n):
    # curr_matrix = deepcopy(matrix)
    for c in range(n):
        curr_matrix[source][c] = float('inf')

    for r in range(n):
        curr_matrix[r][dest] = float('inf')
    curr_matrix[dest][source] = float('inf')

    curr_matrix, reduced_sum = reduce_matrix(curr_matrix, n)

    # if dest == 1:
    #     print(f"for dest {dest} new reduced sum is {reduced_sum}")
    #     print_matrix(curr_matrix)

    return curr_matrix, reduced_sum


def main():

    graph: DefaultDict[str,List[Tuple[str, int]]] = defaultdict(list)

    with open('input.txt', 'r') as file:
        for line in file:
            l = line.strip()
            A, rest = l.split(" to ")
            B, dist = rest.split(" = ")
            graph[A].append((B, int(dist)))
            graph[B].append((A, int(dist)))
    # print(graph)
    locations_ids: Dict[str, int] = {}
    i = 0

    for k in graph.keys():
        locations_ids[k] = i
        i += 1
    n = len(locations_ids)
    # n = 5

    # for l, id in locations_ids.items():
    #     print(f"{l} : {id}")

    matrix = build_adj_matrix(graph, locations_ids, n)
    # matrix= [[float('inf'),20,30,10,11],
    #          [15,float('inf'),16,4,2],
    #          [3,5,float('inf'),2,4],
    #          [19,6,18,float('inf'),3],
    #          [16,4,7,16,float('inf')]
    #          ]


    # for r in matrix:
    #     print(r)
    REDUCED_MATRIX, REDUCED_COST = reduce_matrix(deepcopy(matrix), n)

    # print(REDUCED_COST)
    # print_matrix(REDUCED_MATRIX)
    
    # lets consider we start from 0, lets we can add a for loop here
    for source in range(n):
        # visited = set()
        upper = float('inf') 
        candidates = [(REDUCED_COST, 0, source, REDUCED_MATRIX, set())]
        node_id = 0
        final_dest = 0

        while True:
            next_cost, next_node, next_source, next_matrix, curr_visited = heapq.heappop(candidates)
            curr_visited.add(next_source)
            if len(curr_visited) == n:
                upper = next_cost
                final_dest = next_source
                if candidates[0][0] < upper:
                    continue
                break
            for dest in range(n):
                if dest in curr_visited:
                    continue
                node_id += 1
                reduced_candidate_matrix, reduced_candidate_sum = shortest_distance(deepcopy(next_matrix), next_source, dest, n)
                cost = REDUCED_MATRIX[next_source][dest] + next_cost + reduced_candidate_sum
                heapq.heappush(candidates, (cost, node_id, dest, reduced_candidate_matrix, deepcopy(curr_visited)))
            # print(len(candidates))
            # print(f"for {next_source + 1} =========")
            # for p_cost, p_node_id, p_dest, p_matrix, p_visited in candidates:
            #     print(p_cost, p_node_id+1, p_dest+1)
        # print(candidates)
        print(f"start: {source} to end:{final_dest} min travel dist is")
        print(upper - matrix[source][final_dest])
    # for dest in range(n):
    #     if dest in visited:
    #         continue
    #     node_id += 1
    #     reduced_candidate_matrix, reduced_candidate_sum = shortest_distance(deepcopy(next_matrix), next_source, dest, n)
    #     cost = REDUCED_MATRIX[next_source][dest] + next_cost + reduced_candidate_sum
    #     heapq.heappush(candidates, (cost, node_id, dest, reduced_candidate_matrix))
    # # print("latest")
    # for a, b, c, d in candidates:
    #     print(a,b, c)




if __name__ == "__main__":
    main()