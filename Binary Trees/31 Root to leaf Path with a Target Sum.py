class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return 
        
        self.Target_Sum = targetSum
        self.result     = []
        
        self.path_sum(root,[],0)
        return self.result
    
    def path_sum(self,root,path,curr_sum):
        
        curr_sum = curr_sum + root.val

        if not root.left and not root.right:
            
            if curr_sum == self.Target_Sum:
        
                self.result.append(path + [root.val])
        
        if root.left:
            self.path_sum(root.left,path + [root.val],curr_sum)
            
        if root.right:
            self.path_sum(root.right,path + [root.val],curr_sum)
        