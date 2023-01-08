#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        
        
        # we are given it is dag... we can do topo sort and do relaxation
        
        # intuition >> (not yet clear)
        
        # topo sort with dfs
        
        adj_list = {}
        
        for i in range(n) :
            adj_list[i] = []
            
        for st,end,wt in edges :
            
            adj_list[st].append((end, wt))
        
        
        topo_stack = []
        
        def dfs(node) :
            visit[node] = 1
            
            children = adj_list[node]
            
            for child, _ in children :
                if visit[child] == 0 :
                    dfs(child)
            
            
            # visit of node is done...
            # add into topo sort
            topo_stack.append(node)
            
        
        
        visit = [0] * n
        
        for i in range(n) :
            if visit[i] == 0 :
                dfs(i)
                
        
        # topo_stack contains topological order from top...
        
        src = 0
        dist = [float('inf')] * n
        
        dist[src] = 0
        
        # src should be top of stack... if there is some nodes.. we cant reach them directly
        while topo_stack and topo_stack[-1] != src:
            topo_stack.pop()
            
        
        while topo_stack :
            
            node = topo_stack.pop()
            
            children = adj_list[node]
            
            for child, wt in children :
                
                if dist[node] + wt < dist[child] :
                    dist[child] = dist[node] + wt
                    
        
        
        for i in range(n) :
            if dist[i] == float('inf') :
                dist[i] = -1
        
        return dist
        
            
            
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends