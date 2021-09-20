
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.lookup = dict() # lookup table to get the index of element in inorder array.
        
        for index , element in enumerate(inorder):
            
            self.lookup[element] = index
            
        print(self.lookup)
        
        self.preorder = preorder

        return self.tree(0,len(inorder)-1)
    
    def tree(self,low,hi):
        
        if low > hi : # if lower index is greater than higher index return None
            return None
        
        val   = self.preorder.pop(0) # last element in preorder array will be Root.
        
        node  = TreeNode(val) # make a new Node 
        
        index = self.lookup[val] 
        
        node.left  = self.tree(low,index - 1)
        node.right = self.tree(index + 1, hi)
        
        return node