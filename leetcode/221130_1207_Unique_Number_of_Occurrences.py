class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        aa = list(set(arr))
        ans = []
        for i in range(len(aa)):
            ans.append(arr.count(aa[i]))

        chk = set(ans)

        if len(chk) == len(aa):
            return True
        return False