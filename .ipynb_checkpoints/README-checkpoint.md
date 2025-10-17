# netsci_toolkit
A tiny network-science toolkit distilled from coursework utilities.

## Functions
- degree_preserving_randomization(G, n_iter, ...): Degree-preserving edge-swap null model.
- all_shortest_from(G, s): Unweighted BFS building block (dist, sigma, predecessors).
- indicator_betweenness_unscaled(G, endpoints=False): Unscaled betweenness.
- nx_bc(G, endpoints=False): Wrapper around NetworkX betweenness (normalized=False).
- directed_1in1out_core(G): Iteratively prunes to in>=1 & out>=1 core (directed).
- log_binned_pdf(x, bins_per_decade, ...): Log-binned empirical PDF for heavy tails.

See docstrings for details and examples.
