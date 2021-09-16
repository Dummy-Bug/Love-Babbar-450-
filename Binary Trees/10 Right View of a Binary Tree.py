class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque
    
        return bfs(root)

def bfs(root):
    
    q = deque()
    q.append(root)
    result = []
    
    while q:
        ln   = len(q)
        flag = True
        
        for _ in range(ln):
            
            node = q.popleft()
            
            if node and  flag : # if both node and flag are not null
                
                result.append(node.val)
                flag = False
                
            if node: # even if the flag is False still we push to queue
                q.append(node.right)
                q.append(node.left)
    
    return result
