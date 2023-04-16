import sys
readl = sys.stdin.readline

N = int(readl())
A = list(map(int, readl().split()))

sol = 0
def merge_sort(start, end):
    global sol
    
    if start < end:        
    
        mid = (start+end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        
        idx1, idx2 = start, mid+1
        Arr = []    
        
        while idx1 <= mid and idx2 <= end:
            if A[idx1] > A[idx2]:
                Arr.append(A[idx2])
                idx2 += 1
                sol += (mid - idx1 + 1)
            else:
                Arr.append(A[idx1])
                idx1 += 1
        
        if idx1 <= mid:
            Arr = Arr + A[idx1:mid+1]
        if idx2 <= end:
            Arr = Arr + A[idx2:end+1]
            
        for i in range(len(Arr)):
            A[start + i] = Arr[i]

merge_sort(0, N-1)
print(sol)

    