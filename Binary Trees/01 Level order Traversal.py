class Solution:
    
    def __init__(self):
        from collections import deque
        
    def levelOrder(self,root ):
        
        if not root: # if root is Null return an empty list
            return []
        return self.bfs(root)
        
    def bfs(self,root):
        
        q = deque()
        q.append(root)
        result = []
        
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                result.append(node.data)  
                
                if node: # can't move to left or right if node is Null
                    
                    if node.left: # don't add if node is Null
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
            
                      
        
        return result
