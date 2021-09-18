class Solution:
    
    def printBoundaryView(self,root):
        
        global result
        result  = []
        
        if not root:
            return
        result.append(root.data)
        
        self.leftboundary(root.left) 
        self.leaves(root)
        self.rightboundary(root.right)
        
        return result
        
    def leftboundary(self,root):
        
        if not root:
            return
        
        global result
        
        if root.left: 
            
            result.append(root.data)
            self.leftboundary(root.left)
        
        elif root.right:
            
            result.append(root.data)
            self.leftboundary(root.right)
        
    def leaves(self,root):
        
        if not root:
            return 
        
        global result
        
        if not root.left and not root.right:
            
            result.append(root.data)
            
        self.leaves(root.left)
        self.leaves(root.right)
    
    def rightboundary(self,root):
        
        if not root:
            return
        
        global result
        
        if root.right:
            self.rightboundary(root.right) 
            result.append(root.data)
            
        elif root.left:
            self.rightboundary(root.left)
            result.append(root.data)