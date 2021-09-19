class Solution:
    
    def flatten(self,root):
        
        self.helper(root)
        
    def helper(self,root):
        
        if not root:
            return None
        
        left  = self.helper(root.left)
        right = self.helper(root.right)
        
        if not left and not right:
            return root
        
        if left:
            self.fit(root)
            
        return root
    
    def fit(self,parent):
        
        l_child = parent.left
        r_child = parent.right
        
        node    = l_child
        
        while node.right:
            node = node.right
        
        node.right   = r_child
        parent.right = l_child
        
        parent.left  = None  # to diconnect node from it's old left children.