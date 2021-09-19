class Solution:
    def isSumTree(self,root):
        
        self.result = True
        self.helper(root)
        
        return self.result
    
    def helper(self,root):
        
        if not root:
            return 0
            
        left  = self.helper(root.left)
        right = self.helper(root.right)
        
        if left == 0 and right == 0:
            return root.data
        
        
        if root.data != left + right:
            self.result = False
            return -1
                
        return ( root.data + left + right )
