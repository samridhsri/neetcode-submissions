class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # If the array is sorted use the two pointer method

        # If the array is not sorted you can use the two pointer method: key = number, value = index
        hashMap = {}
        result = []

        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                if hashMap[diff] < i:
                    result.append(hashMap[diff])
                    result.append(i)
                    return result
                else:
                    result.append(i)
                    result.append(hashMap[diff])
                    return result
            
            hashMap[nums[i]] = hashMap.get(nums[i], i)
        
        return result
