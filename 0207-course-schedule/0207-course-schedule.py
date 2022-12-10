from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # (a, b)  -> b must take first.. in topological order b comes first -- (b -> a) indeg of a ++
        
        # cycle detection with topolical sort with bfs
        
        #s1: calc indegrees
        
        if not numCourses or not prerequisites :
            return True
        
        
        indegrees = {}
        adj_list = {}
        
        for i in range(numCourses) : # constraint 
            indegrees[i] = 0
            adj_list[i] = []
            
        for ( a, b) in prerequisites :
            
            # edge -> (b -> a)
            
            if a in indegrees :
                indegrees[a] += 1

                
            if b in adj_list :
                adj_list[b].append(a)
                
        
        # make visit as 0
        
        visited = [0] * numCourses
        
        # if no indeg with 0 -> cycle 
        
        # # push all indeg to queue as probable cands
        queue = deque()
        for k,v in indegrees.items() :
            if v == 0 :
                queue.appendleft(k)
                visited[k] = 1
                
        ans = []
        if len(queue) == 0 :
            return False
        
        while queue :
            
            node = queue.popleft()
            ans.append(node)
            
            # decrease indegrees
            
            children = adj_list[node]
            
            for child in children :
                indegrees[child] -= 1
                
            # add probable cands to queue
            
            for k,v in indegrees.items() :
                
                if v == 0  and visited[k] == 0 :
                    queue.appendleft(k)
                    visited[k] = 1
                    
        
        return len(ans) == numCourses
            
        
                    
                