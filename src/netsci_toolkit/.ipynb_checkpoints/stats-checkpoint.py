import numpy as np

def log_binned_pdf(x, nbins=50, xmin=None, xmax=None):
    """
    Compute a log-binned probability density for positive data x.
    Returns (x_centers, y_density) suitable for log-log plotting.
    """
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x) & (x > 0)]
    if x.size == 0:
        return np.array([]), np.array([])
    if xmin is None: xmin = x.min()
    if xmax is None: xmax = x.max()
    if xmin == xmax:
        return np.array([xmin]), np.array([1.0])
    edges = np.geomspace(xmin, xmax, nbins + 1)
    counts, edges = np.histogram(x, bins=edges)
    widths  = np.diff(edges)
    centers = np.sqrt(edges[:-1] * edges[1:])  # geometric mean
    pdf = counts / (counts.sum() * widths)
    m = pdf > 0
    return centers[m], pdf[m]

