class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        A = List

        for i in range(n):
            tmp = nums[i]
            for j in range(i+1, n):
                if tmp + nums[j] == target:
                    A = [i, j]
                    return A
            