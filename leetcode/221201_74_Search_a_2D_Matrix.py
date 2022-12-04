class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        arr = []

        for rr in range(r):
            for cc in range(c):
                arr.append(matrix[rr][cc])
        
        start = 0
        end = len(arr) - 1        

        while start <= end:
            mid = (start + end) // 2
            # print(arr[mid])
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False