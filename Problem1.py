class Solution:
    def combinationSum(self, candidates, target):
        
        def backtrack(start, end, path, target):
            if target == 0:
                res.append(path[:])
            elif target > 0:
                for i in range(start,end):
                    path.append(candidates[i])
                    backtrack(i, end, path, target - candidates[i])
                    path.pop()
        
        res = []
        candidates.sort()
        backtrack(0, len(candidates), [], target)
        return res
                

sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates,target))
        