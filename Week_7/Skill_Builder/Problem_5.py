# You are using Python
import numpy as np
arr1=np.array(list(map(float,input().split())))
arr2=np.array(list(map(float,input().split())))
arr3=np.correlate(arr1,arr2,mode="full")
print("Cross-correlation of the two time series:")
print(arr3)