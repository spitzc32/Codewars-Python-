"""
1st solution Naive Solution Based on brute force algorithm
Created by: Neet

import numpy as np
def closest_pair(p):
    s,ls = None,[]
    for i in range(len(p)):
        for j in range(len(p)):
            if i != j and s == None:
                ls.append([p[i],p[j]])
                s = np.sum(np.abs(np.diff(np.array([p[i],p[j]]),axis=0)))
            elif i != j and s > np.sum(np.abs(np.diff(np.array([p[i],p[j]]),axis=0))):
                ls.pop()
                ls.append((p[i],p[j]))
                s = np.sum(np.abs(np.diff(np.array([p[i],p[j]]),axis=0)))
    return ls[0]        

"""

"""
Second solution optimization of exceution time
import numpy as np
def dis(head,tail):
    return np.sum(np.abs(np.diff(np.array([head,tail]),axis=0)))
    
def filterLeast(p):
    pts,head= list(p),p[0]
    pts.remove(head) 
    if len(p) <= 2:
      return p
    else:
        return [(head,y) for y in p[1:] if dis(head,y) < 4]
        
        
def closest_pair(p):
    p,pts,fil =list(p),[],filterLeast(p)
    for i in p:
        pts.append(fil)
        p.remove(p[0])
        print(p)
    return      
"""
"""
    Problem no 1:(When modified execution )Execution Time
    Problem no 2: Buffer size


import numpy as np
from math import sqrt
def dis(a,b):
    return sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2))
    
def closest_pair(p):
    q,li = list(p),{}
    for i in p:
        if len(p) <=2:
            return p
        else:
            q.remove(i)
            f={dis(i,y):(i,y) for y in q[1:] if dis(i,y) < 2.4 }
            q.append(i)
            li.update(f)
    print(li)
    return li[min(li.keys())]
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import BallTree as tree

def closest_pair(p):
    res = tree(np.array(p))
    dist, ids = res.query(p, 2)
    mindist = dist[:, 1]  # second nearest neighbour
    minid = np.argmin(mindist)
    args = ids[minid]
    return (p[args[0]],p[args[1]])


points = (
            (2, 2), # A
            (2, 8), # B
            (5, 5), # C
            (6, 3), # D
            (6, 7), # E
            (7, 4), # F
            (7, 9)  # G
        )

print(closest_pair(points))
