def serialize(root, A):
    
    if not root: # storing Tree in preorder instead of level order.
        
        A.append(-1)
        return None
    
    A.append(root.data) 
    
    serialize(root.left,A)
    serialize(root.right,A)


def deSerialize(A):
   
   helper.index = 0
   
   return helper(A)
   
def helper(A): 
    
    if helper.index >= len(A) or A[helper.index] == -1:
        
        helper.index += 1
        return None
        
    node = Node(A[helper.index]) # create a new node
    helper.index += 1
    
    node.left  = helper(A)
    node.right = helper(A)
    
    return node