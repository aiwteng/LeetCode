class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Find the shortest string in the array
        shortest = min(strs,key=len)

        for i, char in enumerate(shortest): 
            #enumerate allow iterate over the sequence while also keep tracking index
            for x in strs:
                if x[i] != char:
                    return shortest[:i] 
                    #take all character of 'shortest' from index 0 to index i

        return shortest