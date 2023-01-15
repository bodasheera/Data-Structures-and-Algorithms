class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} #value : index

        for i,num in enumerate(nums):
            diff = target-num
            if  prevMap.get(diff,-1) != -1:
                return [i, prevMap[diff]]
            else:
                prevMap[num] = i