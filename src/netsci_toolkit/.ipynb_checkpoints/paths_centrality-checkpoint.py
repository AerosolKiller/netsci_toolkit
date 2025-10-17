import networkx as nx
from collections import deque

def all_shortest_from(G, s):
    """
    Unweighted BFS from source s.
    Returns:
      dist[v]  : shortest-path distance from s to v (=-1 if unreachable)
      g[v]     : number of shortest paths from s to v
      P[v]     : list of predecessors of v on shortest s->v paths
    """
    dist  = {v: -1 for v in G.nodes()}
    g = {v:  0 for v in G.nodes()}
    P = {v: [] for v in G.nodes()}

    dist[s] = 0
    g[s] = 1

    Q = deque([s])
    while Q:
        v = Q.popleft()
        for w in G.neighbors(v):
            if dist[w] < 0:
                dist[w] = dist[v] + 1
                Q.append(w)
            if dist[w] == dist[v] + 1:
                g[w] += g[v]
                P[w].append(v)
    return dist, g, P



def indicator_betweenness_unscaled(G, endpoints=False):
    """
    Indicator betweenness (UNWEIGHTED, UNSCALED):
      For each ordered pair (s, t), s!=t, every node i on at least one
      shortest s->t path gets + 1 / g_st (once per pair).

    endpoints=False: do NOT credit s or t.
    endpoints=True : DO credit s and t as well.
    """
    bc = {v: 0.0 for v in G.nodes()}
    nodes = list(G.nodes())

    for s in nodes:
        dist, g, P = all_shortest_from(G, s)

        # Consider only reachable targets t != s with g[t] > 0
        targets = [t for t in nodes if t != s and g[t] > 0]

        for t in targets:
            contrib = 1.0 / g[t]

            # Reverse-walk the predecessor DAG from t to mark
            # all nodes on at least one shortest s->t path.
            stack = [t]
            visited = {t}
            while stack:
                w = stack.pop()

                # Credit rule: indicator version (once per (s,t) if w lies on any shortest path)
                if endpoints:
                    bc[w] += contrib
                else:
                    if w != s and w != t:
                        bc[w] += contrib

                for v in P[w]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)

    return bc





def nx_bc(G, endpoints=False):
    # Use normalized=False to match "unscaled" convention
    return nx.betweenness_centrality(G, normalized=False, endpoints=endpoints)

