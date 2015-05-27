from utils import * 
from math import exp 

def kernel(data, sigma):
    """
    RBF kernel-k-means
    :param data: data points: list of list [[a,b],[c,d]....]
    :param sigma: Gaussian radial basis function
    :return:
    """
    nData = len(data)
    Gram = [[0] * nData for i in range(nData)] # nData x nData matrix
    # TODO
    # Calculate the Gram matrix

    # symmetric matrix
    for i in range(nData):
        for j in range(i,nData):
            if i != j: # diagonal element of matrix = 0
                # RBF kernel: K(xi,xj) = e ( (-|xi-xj|**2) / (2sigma**2)
                square_dist = squaredDistance(data[i],data[j])
                base = 2.0 * sigma**2
                Gram[i][j] = exp(-square_dist/base)
                Gram[j][i] = Gram[i][j]
    return Gram 
