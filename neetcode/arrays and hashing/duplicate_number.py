# Time Complexity -> O(N)
# Space Complexity -> O(N)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = set()

        for val in nums:
            if val in hashmap:
                return True
            else:
                hashmap.add(val)