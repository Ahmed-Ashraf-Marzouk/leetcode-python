class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict()
        c = 0
        for i, n in enumerate(nums):
            try:
                o = d[nums[i]]
                o.append(i)
            except:
                d[nums[i]] = [i]
        print(d)

        c = 0
        for d_e in d:
            l = len(d[d_e])
            if l > 1:
                c += comb(l, 2)
                print(c)
        return c
