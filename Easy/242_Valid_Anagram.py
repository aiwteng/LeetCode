class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Hashmap
        countS , countT = {}, {}

        # Check size first, if size is not same, return False
        if (len(s)!=len(t)):
            return False
        
        # Counter for each letter in s and T
        for i in range(len(s)):
            # the get function is when the letter is not yet exists, default value will be 0
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        if(countS != countT):
            return False
        return True
        
