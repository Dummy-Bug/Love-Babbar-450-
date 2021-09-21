def insert(root, key):
    
    if not root:
        
        root = Node(key)
        
        return root
    
    if root.data == key :
        return
    elif root.data < key :
        
        root.right = insert(root.right,key)
        
    else:
        root.left = insert(root.left,key)
    
    return root