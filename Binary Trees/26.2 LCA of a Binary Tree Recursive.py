class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = None
        
        self.find_lca(root,p,q)
        
        return self.ans
    
    def find_lca(self,root,p,q): # mainain three flag variables ,mid for root and left,right for children.
        
        if not root:       
            return False
        
        if root == p or root == q: # if root node is one of the given nodes then mark mid = True
            
            mid = True
        else:
            mid = False
        left  = self.find_lca(root.left,p,q) # recurse left subtree for the node
        
        right = self.find_lca(root.right,p,q)
        
        if mid + right + left >= 2: # if any node have any two variables true means we that would be LCA node.
            self.ans = root
        
        return (mid or left or right) # if any is true then it means we have found atleast one of the given nodes.