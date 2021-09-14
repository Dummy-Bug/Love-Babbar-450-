class Solution:

# check editorial author has solved the problem using global variable

    def diameter(self,root):
        
        self.diam = 0
        
        self.dfs(root)
        
        return self.diam
        
    def dfs(self,root):
        
        if not root:
            return 0 
        
        left  = self.dfs(root.left)
        right = self.dfs(root.right)
        
        root_diam = left + right + 1
        
        self.diam = max(self.diam,root_diam)
        
        return (1 + max(left , right) )