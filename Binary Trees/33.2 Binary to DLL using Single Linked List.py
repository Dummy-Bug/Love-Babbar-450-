class Solution:
    
    def bToDLL(self,root):
        
        global prev
        prev = None 
        
        self.bToSLL(root) # convert all left pointers such that it forms 
                                                       # a reverse single linked list 
        
        return self.SLLtoDLL(root) # now traverse back linked list and form the DLL
        
        
    def bToSLL(self,root):
        
        if not root:
            return None
        
        global prev    
        
        self.bToSLL(root.left)
        
        root.left = prev
        prev      = root # update the previous pointer to current node
        
        
        self.bToSLL(root.right) # now explore the right sub-tree.
        
        
    def SLLtoDLL(self,root):
        
        if not root:
            return None
            
        while root.right:# since we have changed all the left pointer so
                # rightmost node would be last node of DLL and first node of reversed SLL
            root = root.right
        
        while root.left:
            
            prev = root     
            root = root.left
            
            root.right = prev    # link the node
             
        return root