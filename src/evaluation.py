from math import log, sqrt

def count_occurrence(list):
    """
    count the occurrences of a list item
    :param list:
    :return: dictionary {element:occurrence}
    """
    d = {}
    for i in list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def cal_entropy(assignment):
    """
    calculate the entropy of clustering
    :param assignment: the assignment for the data, list: [0,1,0,0, ....]
    :return: entropy
    """
    occ = count_occurrence(assignment) # get # of data points in each cluster, dictionary
    n = float(sum(occ.values())) # number of data points
    h = 0 # entropy of cluster
    for id in occ:
        p = occ[id] / n # the probability of cluster C_id
        if p != 0:
            h += p*log(p)
    return -h

def purity(groundtruthAssignment, algorithmAssignment):
    purity = 0
    # TODO  
    # Compute the purity
    ids = sorted(set(algorithmAssignment)) # sorted unique clusterID
    matching = 0
    for id in ids:
        # get the index from clusterID where data points belong to the same cluster
        indices = [i for i, j in enumerate(algorithmAssignment) if j == id]
        cluster = [groundtruthAssignment[i] for i in indices]
        occ = count_occurrence(cluster)
        matching += max(occ.values())
    purity =  matching / float(len(groundtruthAssignment))
    return purity 


def NMI(groundtruthAssignment, algorithmAssignment):

    NMI = 0
    # TODO
    # Compute the NMI
    ## compute entropy
    h_c = cal_entropy(algorithmAssignment) # Entropy of clustering C
    h_t = cal_entropy(groundtruthAssignment) # Entropy of partitioning T

    ## compute Mutual information
    occ_c = count_occurrence(algorithmAssignment) # get occurrence: for the probability of cluster C_id
    n_c = float(sum(occ_c.values())) # total # of cluster C_id
    occ_t = count_occurrence(groundtruthAssignment) # get occurrence: for the probability of cluster T_id
    n_t = float(sum(occ_t.values())) # total # of cluster T_id
    ids_c = sorted(set(algorithmAssignment))
    ids_t = sorted(set(groundtruthAssignment))

    # cartesian product for all possible id combination
    cp = [(i,j) for i in ids_c for j in ids_t]
    # dictionary for the shared information, e.g.,{(0, 1): 0, (1, 0): 0, (0, 0): 0, (1, 1): 0}
    p = dict(zip(cp,[0]*len(cp)))

    for (i,j) in zip(algorithmAssignment,groundtruthAssignment):
            p[(i,j)] += 1

    mi = 0 # mutual information
    for c in ids_c:
        for t in ids_t:
            if p[(c,t)] != 0:
                mi += (p[(c,t)]/n_c) * log( (p[(c,t)]/n_c) / ((occ_c[c]/n_c)*(occ_t[t]/n_t)) )
    NMI = mi / sqrt(float(h_c*h_t))
    return NMI
