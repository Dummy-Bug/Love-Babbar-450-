def kthAncestor(root,k, target_node):
    
    anc = {}
    
    if not root:
        return -1
        
    from collections import deque
    
    q = deque()
    
    q.append(root)
    anc[root.data] = -1
    anc[-1] = -1
       
    while q:
        
        for _ in range(len(q)):
            
            node = q.popleft()
            
            if node.left:
                
                anc[node.left.data] = node.data
                q.append(node.left)
                
            if node.right:
                
                anc[node.right.data] = node.data
                q.append(node.right)
            
    while k != 0 :
        
        target_node = anc[target_node]
        
        k = k - 1
        
    return target_node