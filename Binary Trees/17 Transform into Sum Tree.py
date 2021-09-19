class Solution:
    
    def toSumTree(self, root) :
  
        self.helper(root)
        
    def helper(self,root):
        
        if not root:
            return 0
        
        left  = self.helper(root.left)
        right = self.helper(root.right)
        
        value     = left + right + root.data
        root.data = left + right
        
        return value