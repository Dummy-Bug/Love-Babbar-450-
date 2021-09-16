class Solution:
    def bottomView(self, root):
        
        import sys
        sys.setrecursionlimit(10**6)
        
        global dx 
        dx = dict()
        result = []
        
        self.bfs(root,0) # calling with horizontal distance = 0
        
        for val in sorted(dx.keys()):
            result.append(dx[val])
            
        return result
        
    def bfs(self,root,HD):
        
        from collections import deque
        q = deque()
        q.append([root,HD])
        
        while q:
            ln = len(q)
            
            for _ in range(ln):
                
                node, HD = q.popleft()
                
                if node :
                    dx[HD] = node.data
                    
                    q.append([node.left,HD-1])
                    q.append([node.right,HD+1])