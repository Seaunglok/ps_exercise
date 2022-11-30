class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_left(nums, target):
            start = 0
            end = len(nums)-1
            pos = None

            while start <= end:
                mid = (start+end) // 2
                if nums[mid] == target:
                    pos = mid
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return pos

        def binary_right(nums, target):
            start = 0
            end = len(nums) - 1
            pos = None

            while start <= end:
                mid = (start+end) // 2
                if nums[mid] == target:
                    pos = mid
                    start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return pos

        l = []
        if binary_left(nums, target) == None:
            return [-1, -1] 
        l.append(binary_left(nums, target))
        l.append(binary_right(nums, target))

        return l