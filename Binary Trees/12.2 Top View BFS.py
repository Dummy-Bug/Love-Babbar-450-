class Solution:
    
    def topView(self,root):
        
        global dx 
        dx = dict()
        result = []
        
        self.bfs(root,0) 
        
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
                    if HD not in dx:
                        dx[HD] = node.data
                    
                    q.append([node.left,HD-1])
                    q.append([node.right,HD+1])   