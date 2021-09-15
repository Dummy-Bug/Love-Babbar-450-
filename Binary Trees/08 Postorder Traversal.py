def postOrder(root):
        
    visited = set()
    stack   = [root]
    result  = []
        
    while stack:
            
        root = stack.pop()
            
        if not root:
            continue
            
        if root not in visited:
                
            stack.append(root)
            stack.append(root.right)
            stack.append(root.left)
                
            visited.add(root)
                
        else:
            result.append(root.data)
        
    return result