class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        self.sb = [] # string builder
        self.btTOstr(root,"")
        
        return "".join(self.sb)
    
    def btTOstr(self,root,path):
        
        if not root:
            return ""
        
        if not root.left and not root.right: # if leaf Node then just add the value and return 
            
            self.sb.append(str(root.val))
            return self.sb
           
        self.sb.append(str(root.val))
        
        self.sb.append("(") # even if left stree is Null we have to include the bracket
        
        self.btTOstr(root.left, path) 
        
        self.sb.append(")") # close the bracket for left subtree.
        
        
        if root.right: # only add () if right child is True
            
            self.sb.append( "(" ) # open bracket for right subtree.
            
            self.btTOstr(root.right, path)
        
            self.sb.append(")") # close the bracket for right subtree
        
        return self.sb