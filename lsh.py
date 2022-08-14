import numpy as np
import time 
l=[]
#data collection

for i in range(10**7):
  l.append(np.random.normal(0,100,100))

#data processing for lsh
hyper_planes=[]
for j in range(40):
   k=[]
   for i in range(20):
      k.append(np.random.normal(0,100,100))
   hyper_planes.append(k)

#list of dictionaries or hash tables
lis=[]
for i in hyper_planes:
    dict={}
    for j in l:
        m=[]
        for k in i:
            s=0
            for d in range(100):
                s+=j[d]*k[d]
            if(s>=0):
                 m.append(1)
            else:
                m.append(-1)
        if str(m) not in dict.keys():
            dict[str(m)]=[]
        dict[str(m)].append(j)
    lis.append(dict)
    
    
#program starts now
starttime=time.time()
query_point=np.random.normal(0,100,100)
li=[]
t=0
for h in hyper_planes:
    point=[]
    for j in h:
       s=0
       for x in range(100):
          s+=query_point[x]*j[x]
       if(s>=0):
          point.append(1)
       else:
           point.append(-1)
        
    if str(point) in lis[t].keys():
       li.append(lis[t][str(point)])
    t=t+1

ans=[]
for i in range(40):
    if str(point) not in lis[i].keys():
        continue
    lis1=lis[i][str(point)]
    lis2=query_point
    s=0
    m=len(lis1)
    for g in range(m):
        for j in range(100):
            s+=(lis1[g][j]-lis2[j])**2
        s=s**(1/2)
        ans.append(s)
ans.sort()
for i in range(10):
    print(ans[i])
endtime=time.time()
print(endtime-starttime)


#brute force (for checking correctness)
starttime=time.time()
k=[]
for  i in l:
    s=0
    for x in range(100):
        s+=(i[x]-query_point[x])**2
    s=s**(1/2)
    k.append(s)

(k.sort())
print(k)
endtime=time.time()
print(endtime-starttime)
