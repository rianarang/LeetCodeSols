class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            #key is value you are searching for
            #value is index of that number
            key = target - nums[i]
            if (key in m):
                return [i, m[key]]
            else:
                m[nums[i]] = i 