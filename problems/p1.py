
#################################################

# Problem 1. Compute Shortest Path Between any two coordinates in a city. You can solve this for your own city. 
# Assume that you can use network and load open street maps to convert it into a networkx graph. 
# If you don’t know how to do that, you can look it up. Once you load it up you need to code up dikstra search algorithm. 
# Network x has shortest path algorithm – do not use that.


######################################################


import numpy as np
import networkx as nx
import osmnx as ox
import heapq


def trace_shortest_route(src:int,target:int,prev:dict) -> list:
    """
    Read the shortest path from source to target and return list of node path. 
    """
    S = []
    u = target

    if target == src:
        S.append(u)
        return S
    
    if prev[u]:
        while u != src:
            S.append(u)
            u = prev[u]

    S.append(src)
    S.reverse()
    return S




def dijkstra(G:nx.MultiDiGraph,src:int,target:int) -> float | dict:
    """
    Source: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    Followed the priority queue implementation. 
    """
    
    dist = {}
    prev = {} # track predecessor of node
    dist[src] = 0 # track distances from source node. 

    Q = [(0,src)] #priority queue

    for n in G.nodes(): ## Initialize distances
        if n != src:
            dist[n] = np.Inf
            prev[n] = None
    
    while len(Q)>0:
        dist_u, u = heapq.heappop(Q)  # extract min 
        if u == target:
            return dist[u], prev
        
        for neighbor,edict in G[u].items():
            alt = dist[u] + edict[0]['length']
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u
                heapq.heappush(Q,(alt,neighbor)) # add with priority

   





if __name__ == "__main__":

    ox.settings.use_cache = True
    ox.settings.log_console = False
    G = ox.graph_from_place("Denver, Colorado, USA", network_type="drive") #grab graph

    ######################
    # POINTS OF INTEREST #
    ######################

    Colorado_State_Capitol = (39.7393, -104.9848)
    Denver_International_Airport = (39.856094, -104.673737)
    University_of_Denver = (39.6766,-104.9619)
    Coors_Field = (39.7559,-104.9942) #MLB baseball field 

    src_coords = University_of_Denver
    target_coords = Denver_International_Airport

    src = ox.nearest_nodes(G, src_coords[1],src_coords[0]) # get nearest nodse in graph to lat, long coordinates
    target = ox.nearest_nodes(G, target_coords[1],target_coords[0])

    dist,prev = dijkstra(G,src,target)
    print(f"{dist} meters")
    
    S = trace_shortest_route(src,target,prev) #Read the shortest path from source to target and return list of node path. 
    
    fig, ax = ox.plot_graph_route(G, S, route_linewidth=3, node_size=0, bgcolor='k') #plot shortest path
    fig.show()

    ############################################################################
    # Some Checks to see if my dijkstra implementation is behaving as expected #
    ###########################################################################
    # nx_dist = nx.single_source_dijkstra_path_length(G,src,weight='length')

    # print(f"Distance check: {nx_dist[target] == dist}")

    # nx_path = nx.single_source_dijkstra_path(G,src,weight='length')

    # print(f"Path check: {nx_path[target]==S}")