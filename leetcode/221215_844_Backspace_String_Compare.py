class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_copy, t_copy = [], []
        
        for i in range(len(s)):            
            if s[i] == "#":
                if s_copy:
                    s_copy.pop()
            else:
                s_copy.append(s[i])
                
        for i in range(len(t)):
            if t[i] == "#":
                if t_copy:
                    t_copy.pop()
            else:
                t_copy.append(t[i])
                
        
        return s_copy == t_copy
        