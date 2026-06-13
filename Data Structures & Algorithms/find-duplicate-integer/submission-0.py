class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setStorage = set()

        for element in nums:
            if element in setStorage:
                return element
            setStorage.add(element)
        return 0