class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        mid = len(s) // 2

        s1 = s[:mid]
        s2 = s[mid:]

        s1_cnt = 0
        for ss in s1:
            if ss in vowel:
                s1_cnt += 1

        s2_cnt = 0
        for ss in s2:
            if ss in vowel:
                s2_cnt += 1

        if s1_cnt == s2_cnt:
            return True
        return False
