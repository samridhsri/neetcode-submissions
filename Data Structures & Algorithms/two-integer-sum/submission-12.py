class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap:
                return [i,hashMap[nums[i]]] if i < hashMap[nums[i]] else [hashMap[nums[i]],i]
            
            diff = target - nums[i]

            hashMap[diff] = i
        
        return -1