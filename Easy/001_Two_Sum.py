class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]

        # using hashmap
        hashmap = {} # value : index

        for i, n in enumerate(nums): # i = index, n = number in array
            diff = target - n

            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n] = i # update the value and index into hashmap
        return

        
