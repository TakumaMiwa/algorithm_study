class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        import collections

        def compare_rows(row1, row2):
            counter1 = collections.Counter(row1)[1]
            counter2 = collections.Counter(row2)[1]
            if counter1 > counter2:
                return True
            else:
                return False

        kweaks = []
        for i, row in enumerate(mat):
            kweaks.append(i)
            l = len(kweaks)-1
            while l>=1 and compare_rows(mat[kweaks[l-1]], mat[kweaks[l]]):
                a = kweaks[l-1]
                kweaks[l-1] = kweaks[l]
                kweaks[l] = a
                l -= 1
            if len(kweaks) > k:
                kweaks.pop()
        return kweaks