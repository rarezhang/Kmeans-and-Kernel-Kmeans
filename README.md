# Programming Assignment - Python version
####Prerequisites:####

* python: If you are working on your own machine, you will probably need to install Python. The code in this assignment works for python 2.7.  
* linux (recommended) or windows (you may not be able to apply the make commands, but you can use your own IDE, such as Visual Studio and Code Blocks.)

####Goals####

* Implement the following clustering algorithms: K-means and Kernel K-means.
* Implement the following supervised clustering evaluation metrics: purity and NMI.

####Step 1. K-means####

* Complete the following two key functions of K-means in k_means.py
```
def updateClusterID(data, centers):
    nData = len(data) 
    
    clusterID = [0] * nData
    
    # TODO 
    # assign the closet center to each data point
    
    return clusterID

# K: number of clusters 
def updateCenters(data, clusterID, K):
    nDim = len(data[0])
    centers = [[0] * nDim for i in range(K)]

    # TODO recompute the centers based on current clustering assignment
    # If a cluster doesn't have any data points, in this homework, leave it to ALL 0s

    return centers 
```

* Write the purity and NMI metrics in evaluation.py 
```
def  purity(groundtruthAssignment, algorithmAssignment):
    # TODO  
    # Compute the purity 
    
    return purity 


def NMI(groundtruthAssignment, algorithmAssignment):
    # TODO
    # Compute the NMI

    return NMI
```

* Use the following command line to run the python script  
```
python main_k_means.py  ../data/self_test.data ../data/self_test.ground
```

* If your implementation is correct, you should have information printed on your screen that is very similar to the information given below.
```
# of iterations: 11
SSE =  24189.053923
Purity = 0.666666666667
NMI =  0.0848243120365
```

####Step 2. Kernel K-means####

* Once you have done K-means, you only need to implement a wrapper to transform the data points into the kernel space for kernel K-means. In this homework, we are going to implement the RBF kernel. Please complete the following coordinates transformation function, in file kernel_k_means.py
```
def kernel(data, sigma):
    nData = len(data)
    Gram = [[0] * nData for i in range(nData)] 
    # TODO
    # Calculate the Gram matrix 

    return Gram 
```

* Use the following command line to run the python script  
```
python main_kernel_k_means.py  ../data/self_test.data ../data/self_test.ground
```

* If your implementation is correct, you should have information printed on your screen that is very similar to the information given below.
```
# of iterations: 3
SSE =  2991.54279799
Purity = 0.996666666667
NMI =  0.968782533951
```

