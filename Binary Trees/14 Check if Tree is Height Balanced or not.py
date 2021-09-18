class Solution:
    def isBalanced(self, root: Optional[TreeNode]):
         
        global result
        result = True
        
        self.dfs(root)
        return result

    def dfs(self,node):
        
        if not node:
            return 0

        lh = self.dfs(node.left)
        rh = self.dfs(node.right)
        
        if abs(rh - lh) > 1 :
            global result
            result = False
            
        return ( 1 + max(lh,rh) )