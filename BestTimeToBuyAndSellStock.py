class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #keep track of the lowest val and the max profit
        #if prices[i] < lowest_val -> lowest_val = prices[i]
        #check if prices[i] - lowest_val > max_profit and then replace
        low = 2147483647;
        maxp = 0;
        
        for x in prices:
            if (x < low):
                low = x
            elif ((x - low) > maxp):
                maxp = x - low
                
        return maxp