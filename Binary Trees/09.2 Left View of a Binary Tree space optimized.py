def LeftView(root):
    
    global max_level  # can't declare and intialise in same line
    max_level = -1
    
    global result 
    result = []
    
    dfs(root,0) # calling dfs function
    
    return result
    
    
def dfs(root,level):
    
    global max_level
    global visited
    
    if not root:
        return 
    
    if max_level < level: # Put the level in set and data in result.
        
        max_level = level
        result.append(root.data)
    
    dfs(root.left,level+1)
    dfs(root.right,level+1)