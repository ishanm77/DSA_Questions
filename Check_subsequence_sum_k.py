from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    if k==0:
        return True
    if n==0:
        return False
    if a[n-1]>k:
        return isSubsetPresent(n-1,k,a)
    return isSubsetPresent(n-1,k,a) or isSubsetPresent(n-1,k-a[n-1],a)