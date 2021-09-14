class Solution:
    def height(self, root):
        
        return self.dfs(root)
        
    def dfs(self,root):
        
        if not root:
            return 0
            
        left  = self.dfs(root.left) # explore the left and 
        right = self.dfs(root.right)                   #  right sub tree.
        
        return ( 1 +  max(left,right) )
 