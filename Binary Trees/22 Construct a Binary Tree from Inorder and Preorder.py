class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.lookup = dict() # lookup table to get the index of element in inorder array.
        
        for index , element in enumerate(inorder):
            
            self.lookup[element] = index
            
        # print(self.lookup)
        
        self.postorder = postorder

        return self.tree(0,len(inorder)-1)
    
    def tree(self,low,hi):
        
        if low > hi : # if lower index is greater than higher index return None
            return None

        val   = self.postorder.pop() # can optimize this step, check the leetcode official solution
        
        node  = TreeNode(val) # make a new Node 
        
        index = self.lookup[val] 
        
        node.right = self.tree(index + 1, hi)
        node.left  = self.tree(low,index - 1)
        
        
        return node