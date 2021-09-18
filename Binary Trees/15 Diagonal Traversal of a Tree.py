def diagonal(root):
    
    from collections import deque
    q = deque()

    return bfs(root,q)
    
     
def bfs(root,q):
    
    lst = []
    q.append(root)
    result = []
    
    while q:
        
        node   = q.popleft()
        
        while node: # explore all the right childs and push all the left childs.
            
                
            result.append(node.data)
                
            if node.left:
                q.append(node.left)
            
            node = node.right
                
    return result