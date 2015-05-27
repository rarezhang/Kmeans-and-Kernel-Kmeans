def loadPoints(filename):
    input = open(filename, "r")
    
    info = input.readline().split()
    
# number of data points and dimension
    # already know: (1)# of data points (2)dimension --> first line of the data file
    nData = int(info[0]) 
    nDim = int(info[1])
    
# create data matrix
    data = [[0]*nDim for i in range(nData)]

    for i in range(nData):
        info = input.readline().split()
        for j in range(nDim):
            data[i][j] = float(info[j]) 

    return data 

def loadClusters(filename): 
    input = open(filename, "r") 
    
    info = input.readline() 
    
    nData = int(info)
    
    clusters = [0] * nData 
    
    for i in range(nData):
        info = input.readline()
        clusters[i] = int(info)
    
    return clusters

