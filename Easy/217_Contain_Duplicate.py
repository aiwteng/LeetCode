class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Sol3: use hash set (fastest)
        hashset = set() # initialise hashset

        for i in nums: # iterate every value in nums array
            if i in hashset: # if the value is in the hashset, return True
                return True
            else:
                hashset.add(i) # else add the number in the hashset
        return False

        # # Sol2: sort the array first
        # sorted_nums = self.merge_sort(nums)

        # for i in range(len(nums)-1):
        #     if ( nums[i] == nums[i+1]):
        #         return True
        # return False

    # #Merge sort algorithm
    # def merge_sort(self,arr):
    #     if len(arr) > 1:
    #         mid = len(arr) // 2  # Finding the middle of the array
    #         left_half = arr[:mid]  # Dividing the array elements into 2 halves
    #         right_half = arr[mid:]

    #         self.merge_sort(left_half)  # Sorting the first half
    #         self.merge_sort(right_half)  # Sorting the second half

    #         i = j = k = 0

    #         # Copy data to temporary arrays left_half[] and right_half[]
    #         while i < len(left_half) and j < len(right_half):
    #             if left_half[i] < right_half[j]:
    #                 arr[k] = left_half[i]
    #                 i += 1
    #             else:
    #                 arr[k] = right_half[j]
    #                 j += 1
    #             k += 1

    #         # Checking if any element was left
    #         while i < len(left_half):
    #             arr[k] = left_half[i]
    #             i += 1
    #             k += 1

    #         while j < len(right_half):
    #             arr[k] = right_half[j]
    #             j += 1
    #             k += 1

    #     return arr  

    # Time Limit Exceeded 65/75 testcases passed
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (nums[j] == nums[i]):
        #             return True
        # return False                



        