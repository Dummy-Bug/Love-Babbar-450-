class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        self.result = []
        self.lookup = dict()
        
        self.helper(root) 
        
        return self.result
    
    def helper(self,root):
        
        if not root:
            return ""
            
        sub_tree = "(" 
        
        sub_tree = sub_tree + self.helper(root.left)
        
        sub_tree = sub_tree + str(root.val) 
        
        sub_tree = sub_tree + self.helper(root.right)
        
        sub_tree = sub_tree + ")"
        
        
        if sub_tree in self.lookup and self.lookup[sub_tree] == 1:
            self.result.append(root)
        
        if sub_tree in self.lookup:
            self.lookup[sub_tree] += 1
        else:
            self.lookup[sub_tree] = 1
            
        return sub_tree