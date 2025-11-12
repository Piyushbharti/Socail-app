def subsetsWithDup(nums):
    ans = []
    nums.sort()
    def solve(index, curr):
        ans.append(curr[:])
        for i in range(index, len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            curr.append(nums[i])
            solve(i+1, curr)
            curr.pop()
    solve(0, [])
    return ans
nums = [1,2,2]
print(subsetsWithDup(nums))