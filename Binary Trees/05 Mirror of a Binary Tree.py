class Solution:
    
    def mirror(self,root):
        
        if not root:
            return 
        
        self.mirror(root.left) # first explore left sub-tree
        
        self.mirror(root.right)# then explore right sub-tree
        
        root.left, root.right = root.right, root.left
        
        return root
        