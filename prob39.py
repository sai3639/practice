# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:00:24 2021

@author: saira

"""

def CheesyMatMul(A,B):
    import numpy as np
    if A.shape[1] != B.shape[0]: # "Inner dimensions don't agree: A's shape: {} != B's shape {}".format(A.shape, B.shape)
        return np.empty(A.shape)
    else:
        ARows = A.shape[0]
        BCols = B.shape[1]
        InDim = A.shape[1]
        Prod = np.zeros((ARows, BCols))
        for ARow  in range(ARows):
            for BCol in range(BCols):
                for EachInnerDim in range(InDim):
                    Prod[ARow, BCol] += A[ARow, EachInnerDim]  * B[EachInnerDim, BCol]
        return Prod
    
    
# test

from numpy import array, matmul
M1 = array([[1, 5, 4], [3, 7, -1]])
M2 = array([[2], [0], [2]])
print('CheesyMatmul of \n{} \n&\n{} \nis\n{}'.format(M1, M2, CheesyMatMul(M1, M2)))
print('Numpy.Matmul of \n{} \n&\n{} \nis\n{}'.format(M1, M2, matmul(M1, M2)))