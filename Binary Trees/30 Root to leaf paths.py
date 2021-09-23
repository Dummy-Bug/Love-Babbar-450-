class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.result = []
        
        self.all_paths(root,"")
        
        return self.result
        
    def all_paths(self,root,path):
        
        if root.left:
            self.all_paths(root.left,path  + str(root.val) + "->")
        
        if root.right:
            self.all_paths(root.right,path + str(root.val)+ "->")
            
        if not root.left and not root.right: # if it's a leaf Node we have found a path.
            self.result.append(path + str(root.val))