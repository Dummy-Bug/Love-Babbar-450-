class Solution:
    
    def sumOfLongRootToLeafPath(self,root):
        
        temp = self.func(root)
        
        return temp[1]
        
    def func(self,root):
        
        if not root:
            return None
            
        lh = self.func(root.left)
        rh = self.func(root.right)
        
        if lh and rh: 
            
            if rh[0] == lh[0]: # if height left subtree == right sutree height
                
                if rh[1] >= lh[1]: # if sum of right subtree > left subtree sum 
                
                    return (1 + rh[0], root.data + rh[1]) 
            
                else:
                
                    return (1 + lh[0], root.data + lh[1])
            
            elif rh[0] > lh[0]: # if right sub-tree height is >> left subtre.
                
                return (1 + rh[0], root.data + rh[1])
                
            else:
                 return (1 + lh[0],root.data + lh[1])
                
        elif lh : # if root has only left child.
            
            return (1 + lh[0], root.data + lh[1])
            
        elif rh: # if root has only right child.
            return (1 + rh[0], root.data + rh[1])
            
        else: # if it is a leaf Node
            return (1 , root.data)