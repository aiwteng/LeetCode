from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # using hashmap
        # create a defaultdict with a default value of an empty list
        hashmap = defaultdict(list) # key(character count) : List of anagrams

        # calculate number of letter in each word (eg: 1e, 1a, 1t)

        # loop every words in the list of string
        for w in strs: 
            count = [0] * 26 # a to z
            # loop every character in the word
            for c in w:
                count[ord(c) - ord("a")] += 1 
            
            # group all anagrams together
            # for the word that having same key(character count),
            # will be added to particular hashmap
            hashmap[tuple(count)].append(w)

        return hashmap.values()

# Note:
# ord(): a function to return the unicode code of a character
# ord(char) - ord("a") : we need to find the index of each character
# we take the ord(char) - the unicode of "a" will get the index in the count array
# eg: when char = a, ord(a) -> 0 and minus ord("a") will get 0, means index of letter a = 0

# tuple(): to create a sequence of element that cannot be change after created
# because a list(count) cannot be key, so have to add tuple()

# defaultdict(): to provide default value(0) when accessing keys that do not exist