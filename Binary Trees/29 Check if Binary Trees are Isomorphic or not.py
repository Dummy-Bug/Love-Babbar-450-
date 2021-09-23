class Solution:
     
     # call fuunction with replacement and without replacement of chil nodes.
    def isIsomorphic(self, root1, root2): 
        
        if not root1 and not root2: # if both None
            return True
            
        if not root1 or not root2: # if any one is None
            return False
            
        if root1.data != root2.data:
            return False
            
        left_without_swaping  = self.isIsomorphic(root1.left,root2.left) 
        
        right_without_swaping = self.isIsomorphic(root1.right,root2.right)
        
        
        left_with_swaping     = self.isIsomorphic(root1.left,root2.right)
        
        right_with_swaping    = self.isIsomorphic(root1.right,root2.left)
        
        return (left_without_swaping and right_without_swaping)or(left_with_swaping and right_with_swaping)