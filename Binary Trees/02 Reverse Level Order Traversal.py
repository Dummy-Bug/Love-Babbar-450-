def reverseLevelOrder(root):
    
    if not root :
        return []
        
    return bfs(root)
    
def bfs(root):
    
    from collections import deque
    
    q = deque()
    q.append(root)
    result = []
    
    while q:
        
        for _ in range(len(q)): # to get the level order traversal 
            
            node = q.popleft()
            result.append(node.data)
            
            if node: # can't check left and right child of a Null Node
                
                if node.right :
                    q.append(node.right)
                
                if node.left:
                    q.append(node.left)
                    
    return result[::-1] # reverse result before returning to get reverse level order.
    