class Solution:
    def checkMirrorTree(self, n, e, A, B):
        
        A1 = [[] for j in range(2*e)]
        B1 = [[] for i in range(2*e)]
        
        for i in range(0,2*e,2):
            x = A[i]
            y = A[i+1]
            
            A1[x].append(y)
        
        for i in range(0,2*e,2):
            
            x = B[i]
            y = B[i+1]
            
            B1[x].append(y)
        
        while A1 and B1:
            
            l1 = A1.pop()
            l2 = B1.pop()
            
            if l1 != l2[::-1]:
                return 0
                
        if A1 or B1:
            return 0
            
        return 1