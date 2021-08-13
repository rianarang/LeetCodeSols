class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        if (l == 1): return 1
        if (l == 2 and not (nums[0] == nums[1])): return 2
        if (l == 2 and nums[0] == nums[1]): return 1
        
        i = 1
        
        while(i < l and nums[i] == nums[i-1]):
              i += 1
        if (i == l): return 1 
        #true means decrease
        #false means increase
        
        up = nums[i-1] > nums[i]
              
        ans = 1
              
        while(i < l):
            if (up and nums[i] < nums[i-1] or ((not up) and nums[i] > nums[i-1])):
                ans += 1
                up = (not up)
                
            i += 1
            
        return ans
