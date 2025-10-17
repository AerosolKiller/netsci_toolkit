import networkx as nx

def directed_1in1out_core(H):
    Gc = H.copy()
    # Iteratively prune nodes with in==0 or out==0 (like a directed 1-in/1-out core)
    changed = True
    while changed:
        changed = False
        to_drop = [n for n in Gc if Gc.in_degree(n) == 0 or Gc.out_degree(n) == 0]
        if to_drop:
            Gc.remove_nodes_from(to_drop)
            changed = True
    return Gc

