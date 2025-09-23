class Solution:
    from typing import List
    import heapq
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for x, y in points:
            dist = x*x + y*y
            
            heapq.heappush(heap, (dist, [x,y] ))
            
            
            res = []
            
            for _ in range(k):
                res.append(heapq.heappop(heap)[1])
            
        
        
    