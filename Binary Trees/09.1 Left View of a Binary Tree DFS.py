def LeftView(root):
    
    global visited  # can't declare and intialise in same line
    visited = set()
    
    global result 
    result = []
    
    dfs(root,0) # calling dfs function
    
    return result
    
    
def dfs(root,level):
    
    global result
    global visited
    
    if not root:
        return 
    
    if level not in visited: # Put the level in set and data in result.
        
        visited.add(level)
        result.append(root.data)
    
    dfs(root.left,level+1)
    dfs(root.right,level+1)