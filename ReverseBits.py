class Solution:
    def reverseBits(self, n: int) -> int:
        #use & operator to find last digit ex. 5 & 1 is 1 and 4&1 is 0 bc 5 has a 1 as last digit 1&1 is 1, 1&0 is 0
        
        #then add to answer variable 2^x (x starting at 31 and decrementing)
        
        # will only add when 1 (so successful &) and will decrement everytime
        i = 31
        ans = 0
        #if 1 at that position
        #in range will do from 0 to 31
        for exp in range(32):
            if(n & (2**exp)):
                ans += 2**i
            i -= 1
            
        return ans