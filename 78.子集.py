class Solution:
    def subSet(self,nums:list) -> list:
        if not nums:
            return
        res = []
        def dfs(i, path ):
            res.append(path[:])
            for i in range(i, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        print(res)
        return res
s=Solution()
s.subSet([1,2,3])