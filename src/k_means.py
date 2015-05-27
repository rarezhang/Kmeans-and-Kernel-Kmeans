from utils import * 


def computeSSE(data, centers, clusterID):
    """
    objective function: calculate Sum of Squared Errors
    :param data:
    :param centers:
    :param clusterID:
    :return:
    """
    sse = 0 
    nData = len(data) 
    for i in range(nData):
        c = clusterID[i]
        sse += squaredDistance(data[i], centers[c]) 
        
    return sse 

def updateClusterID(data, centers):
    """
    assign the closet center to each data point
    :param data: data points: list of list [[a,b],[c,d]....]
    :param centers: data points: list of list [[a,b],[c,d]], K=2 (according to main)
    :return:
    """
    nData = len(data) # how many data points
    nCenters = len(centers) # how many centers

    
    clusterID = [0] * nData
    dis_Centers = [0] * nCenters# the distance between one data point to each center, since K=2, list [len1,len2]
    
    # TODO 
    # assign the closet center to each data point
    for i in range(nData):
        for c in range(nCenters):
            # calculate the distance between one data point to one center
            dis_Centers[c] = squaredDistance(data[i], centers[c])
        # assign the closet center to the data point, clusterID: the index of the dis_Centers list
        clusterID[i] = dis_Centers.index(min(dis_Centers))
    return clusterID

# K: number of clusters 
def updateCenters(data, clusterID, K):
    nDim = len(data[0]) # the dimension of one data point
    centers = [[0] * nDim for i in range(K)] # list of list [[a,b],[c,d]]

    # TODO recompute the centers based on current clustering assignment
    # If a cluster doesn't have any data points, in this homework, leave it to ALL 0s
    ids = sorted(set(clusterID)) # sorted unique clusterID
    for id in ids:
        # get the index from clusterID where data points belong to the same cluster
        indices = [i for i, j in enumerate(clusterID) if j == id]
        # all data point in the same cluster, list of lists [[a,b],[c,d]...]
        cluster = [data[i] for i in indices]
        if len(cluster) == 0:
            #If a cluster doesn't have any data points, leave it to ALL 0s
            centers[id] = [0] * nDim
        else:
            # compute the centroids (i.e., mean point) of each cluster
            centers[id] = [float(sum(col))/len(col) for col in zip(*cluster)]
    return centers 

def kmeans(data, centers, maxIter = 100, tol = 1e-6):
    """

    :param data: data points: list of list [[a,b],[c,d]....]
    :param centers: data points: list of list [[a,b],[c,d]], K=2 (according to main)
    :param maxIter:
    :param tol:
    :return: clusterID: list
    """
    nData = len(data) 
    
    if nData == 0:
        return []

    K = len(centers) 
    
    clusterID = [0] * nData
    
    if K >= nData:
        for i in range(nData):
            clusterID[i] = i
        return clusterID

    nDim = len(data[0]) 
    
    lastDistance = 1e100
    
    for iter in range(maxIter):
        clusterID = updateClusterID(data, centers) 
        centers = updateCenters(data, clusterID, K)
        
        curDistance = computeSSE(data, centers, clusterID) # objective function
        if lastDistance - curDistance < tol or (lastDistance - curDistance)/lastDistance < tol:
            print "# of iterations:", iter 
            print "SSE = ", curDistance
            return clusterID
        
        lastDistance = curDistance
        
    print "# of iterations:", iter 
    print "SSE = ", curDistance
    return clusterID

