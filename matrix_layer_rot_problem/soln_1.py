#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrix(a,m,n,r):
  for e in range(r):
    row=0
    col=0
    mrow=m-1
    ncol=n-1
    while(row<mrow and col<ncol):
      store=a[row][col]
      for i in range(col+1,ncol+1):
        t=a[row][i]
        a[row][i]=a[row][i-1]
        a[row][i-1]=t
      for i in range(row+1,mrow+1):
        t=a[i][ncol]
        a[i][ncol]=a[i-1][ncol]
        a[i-1][ncol]=t
      for i in range(ncol,col-1,-1):
        t=a[mrow][i-1]
        a[mrow][i]=a[mrow][i-1]
        a[mrow][i-1]=t
      for i in range(mrow,row,-1):
        t=a[i-1][col]
        a[i][col]=a[i-1][col]
        a[i-1][col]=t
      a[row+1][col]=store
      col=col+1
      row=row+1
      mrow=mrow-1
      ncol=ncol-1

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    a = []

    for _ in range(m):
        a.append(list(map(int, input().rstrip().split())))

    matrix(a,m,n,r)
    for i in range(len(a)):
        print(*a[i])

