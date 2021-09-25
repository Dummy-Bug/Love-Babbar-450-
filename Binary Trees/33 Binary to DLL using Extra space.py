class Solution:
    
    def bToDLL(self,root):
        
        self.temp = []
        
        self.binaryToDLL(root)
        
        new_root = self.temp[0]
        
        n = len(self.temp)
        
        if n == 1:
            return root
        
        new_root.left  = None
        new_root.right = self.temp[1]
        
        for i in range(1,n-1):
            
            self.temp[i].left  = self.temp[i-1]
            self.temp[i].right = self.temp[i+1]
        
        else:
            self.temp[n-1].left  = self.temp[n-2]
            self.temp[n-1].right = None
            
        return new_root
        
    def binaryToDLL(self,root):
        
        if not root:
            return None 
        
        self.binaryToDLL(root.left)
        self.temp.append(root)
        self.binaryToDLL(root.right)