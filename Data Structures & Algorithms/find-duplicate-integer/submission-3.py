class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fp = 0
        sp = 0

        while True:
            fp = nums[fp]
            fp = nums[fp]
            sp = nums[sp]

            if sp == fp:
                fp = 0
                
                while sp != fp:
                    fp = nums[fp]
                    sp = nums[sp]

                    if fp == sp:
                        return fp
        return -1