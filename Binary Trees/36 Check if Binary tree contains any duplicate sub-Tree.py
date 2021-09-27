class Solution:
    
    def dupSub(self, root):
        
        import sys 
        sys.setrecursionlimit(10**6)
        
        self.result = 0
        self.lookup = dict() 
        
        self.helper(root)
        
        return self.result
        
    def helper(self,root):
        
        if not root:
            return ""
            
        sub_tree = "(" 
        
        sub_tree = sub_tree + self.helper(root.left)
        
        sub_tree = sub_tree + str(root.data)
        
        sub_tree = sub_tree + self.helper(root.right)
        
        sub_tree = sub_tree + ")"
        
        
        if sub_tree in self.lookup:
            
            if self.result == 0:
                if len(sub_tree) > 3:
                    self.result = 1
        else:
            self.lookup[sub_tree] = 1
            
        return sub_tree  