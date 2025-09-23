class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
         #[[1,2,3,4],[1,2,3,4]]
        #[[3,3],[5,-1],[-2,4]]

        # list inside a list in python

        outer = len(points)
        for i in range(outer):
            inner = points[i]

            for sublist in points:
                for i in sublist:
                    print(sublist[i]-1)

            # for j, n in enumerate(inner):
            #     num = n
            #     # * n[j] + n[j+1]*n[j+1] 

            # print (num)
            # if inner
            # for j in range(len(inner)):
            #     res = points[j]

        # print(inner)
        # print(res)
            # for j in range(len(points))