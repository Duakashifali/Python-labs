# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:59:08 2026

@author: hp
"""
import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print(a)
print('\n')
print("Axis parameter not passed. The input array is flattened before insertion.")
print(np.insert(a,1,[11,12]))
print('\n')
print("Axis parameter passed. The value array is broadcast to match input array.")
print("Broadcast along axis 0:")
print(np.insert(a,1,[11,12],axis=0))
print('\n')
print("Broadcast along axis 1:")
print(np.insert(a,1,[11,12,13],axis=1))