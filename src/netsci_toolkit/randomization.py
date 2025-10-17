import networkx as nx
import numpy as np
import random

def degree_preserving_randomization(G, n_iter = 500, fail_max = 200):
    """
    Perform degree-preserving randomization on a graph. 

    This function is modified based on Algorithm 11.1 in Bagrow & Ahn textbook. This version of randomization prevent an infinite loop
    by abandoning the exvhange process after reaching a given number of attempts without a successful exchange. 
    
    Parameters
    ----------
    G : networkx.Graph
        the input graph to be randomized. The graph can be directed or undirected. Must be simple. 

    n_iter : int, optional (default = 1000)
        the number of edge exchange to perform. A higher number of iteration leads to more randomization. 
        In this case, we preserve the degree of nodes. This number should be proportional to the number of edges in the graph
        for sufficient randomization. 

    fail_max : int 
        fail_max is a counter cap that makes sure the exchange process will stop if the infinite loop happens. 

    Returns
    -------
    G_random : networkx.Graph
        A randomized graph with same degree distirbution as the input graph G but with a shuffled edge structure. 

    Notes
    -----
    - This function works by randomly select two independent edges in the network (u, v) and (x, y).
      The attempted exchanges are {(u, x), (v, y)} and {(u, y), (x, v)}.
    - swapped is a flag that checks on whether the edge exchange is successful or not. 
      If swapped is true, then add 1 to the success counter and reset the n_fail counter. 
    - When number of failure reaches the max failure, raise the runtime error and stop the function. 

    Example
    -------
    >>> import networkx as nx
    >>> G = nx.erdos_renyi_graph(10, 0.5)
    >>> G_random = degree_preserving_randomization(G, n_iter=100)

    Citations
    ---------
    Klein, Brennan. PHYS 7332 Fall 2025 Class04 notes
    """
    G_random = G.copy()
    edges = list(G_random.edges())
    num_edge = len(edges)
    n_fail = 0
    success = 0 

    swapped = False

    while n_fail < fail_max and success < n_iter:
        edge1_id = np.random.choice(list(range(num_edge)))
        u, v = edges[edge1_id]
        edge2_id = np.random.choice(list(range(num_edge)))
        x, y = edges[edge2_id]
        
        if len({u, v, x, y}) == 4 and n_fail < fail_max:
            if np.random.rand() > 0.5:
                if not (G_random.has_edge(u, x) or G_random.has_edge(v, y)):
                    G_random.remove_edge(u,v)
                    G_random.remove_edge(x,y)
                    G_random.add_edge(u,x)
                    G_random.add_edge(v,y)
                    swapped = True
                        
            else:
                if not (G_random.has_edge(u, y) or G_random.has_edge(v, x)):
                    G_random.remove_edge(u,v)
                    G_random.remove_edge(x,y)
                    G_random.add_edge(u,y)
                    G_random.add_edge(v,x)
                    swapped = True
        if swapped:
            success += 1
            n_fail = 0
            edges = list(G_random.edges())
        else:
            n_fail += 1

    if n_fail >= fail_max:
        raise RuntimeError(f"Stopped: reached {fail_max} consecutive failed attempts. "
                       "No further swaps possible.")
            
    return G_random

