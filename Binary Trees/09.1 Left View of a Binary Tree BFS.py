def LeftView(root):
    
    # Use Level Order Traversal
    from collections import deque
    
    q = deque()
    q.append(root)
    result = []
    
    while q:
        ln   = len(q)
        flag = True
        
        for _ in range(ln):
            
            node = q.popleft()
            
            if node :
                
                if  flag : # if both node and flag are not null
                
                    result.append(node.data)
                    flag = False
                
                # even if the flag is False still we push to queue
                q.append(node.left)
                q.append(node.right)
    
    return result