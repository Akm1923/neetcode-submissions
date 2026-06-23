
from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        for i in points:
            d=(sqrt((0 - i[0])**2 + (0 - i[1])**2))
            l.append((d,i))
        heapq.heapify(l)
        return [i[1] for i in heapq.nsmallest(k,l)]
        