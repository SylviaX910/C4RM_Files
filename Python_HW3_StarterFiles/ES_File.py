import numpy as np

def ES(losses, alpha=None, VaR=None):
    if VaR is None:
        VaR = np.percentile(losses, 100 * alpha)
        
    es_value = np.mean(losses[losses > VaR])
    return es_value
