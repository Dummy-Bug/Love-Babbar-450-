class Solution:
    
    def getMaxSum(self,root):
        from collections import defaultdict
        
        self.lookup = defaultdict(lambda : [])
        return self.helper(root)
        
    def helper(self,root):
        
        if not root:
            return 0
        
        if root in self.lookup:
            return self.lookup[root]
            
        if not root.left and not root.right: # if current node is a leaf node. 
            
            include = root.data 
            
            exclude = 0
            
        elif not root.left:
            
            y = root.right
            
            include = root.data + self.helper(y.right) + self.helper(y.left)
            
            exclude = self.helper(y) 
        
        elif not root.right: # if node doesn't have right child.
        
            x = root.left
            
            include = root.data + self.helper(x.left) + self.helper(x.right)
            
            exclude = self.helper(x)
            
        elif root.left and root.right:
            
            x = root.left
            y = root.right
            
            include = root.data + self.helper(x.left) + self.helper(y.right) + self.helper(x.right) + self.helper(y.left)
            
            exclude = self.helper(x) + self.helper(y)
            
        self.lookup[root] = max(include,exclude)
        
        return self.lookup[root]