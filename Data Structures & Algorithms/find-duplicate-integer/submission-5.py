class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Its guaranteed that there will be a duplicate

        fp = 0
        sp = 0

        # after we find a cycle, start a pointer from starting again

        while True:
            fp = nums[fp]
            fp = nums[fp]
            sp = nums[sp]

            if fp == sp:
                sp = 0

                while fp!=sp:
                    fp = nums[fp]
                    sp = nums[sp]
                return fp