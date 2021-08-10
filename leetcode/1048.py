from collections import defaultdict

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = defaultdict(dict)
        min_key = max_key = len(words[0])
        for word in words:
            dic[len(word)][word] = 1
            min_key = min(min_key, len(word))
            max_key = max(max_key, len(word))

        max_chain = 1
        for i in range(min_key, max_key):
            for istring, chain in dic[i].items():
                for next_string, chain2 in dic[i+1].items():
                    if self.isChain(istring, next_string[0]) and chain+1>chain2:
                        dic[i+1][next_string] = chain + 1
                        max_chain = max(max_chain, chain)

        return max_chain




    def isChain(self, word1, word2):

        if len(word2) - 1 == len(word1):
            return False

        p = 0
        skip = False
        for char in word1:
            if char == word2[p]: p += 1
            else:
                if skip:
                    return False
                elif word2[p+1]==char:
                    skip = True
                    p += 2
                else:
                    return False

        return True

