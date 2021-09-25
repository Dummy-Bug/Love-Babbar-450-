class Solution:
    
	def minSwaps(self, nums):
	    
		temp = nums.copy()
		temp.sort()
		dx = {}
		
		for i in range(len(temp)):
		    dx[temp[i]] = i
		
		count, i = 0, 0
		
		while i < len(nums):
		    
		    if nums[i] != temp[i]:
		        
		        count = count + 1
		        
		        self.swap(nums,i,dx[nums[i]])# pythonic swaping does not work always.
		    else:
                i = i + 1
               
        return count
        
        
    def swap(self,arr,i,j):
        
        arr[i], arr[j] = arr[j], arr[i]