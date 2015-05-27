def squaredDistance(vec1, vec2):
    sum = 0 
    dim = len(vec1) 
    
    for i in range(dim):
        sum += (vec1[i] - vec2[i]) * (vec1[i] - vec2[i]) 
    
    return sum
