class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        if not s or not words:
            return 0
        s += "*"
        parts = []
        c_val = s[0]
        c_index = 0
        c_count = 1
        for i in range(1, len(s)):
            if c_val != s[i]:
                if c_count >= 3:
                    parts.append(f'*{c_val}')
                else:
                    parts.append(s[c_index:i])
                c_count = 1
                c_val = s[i]
                c_index = i
            else:
                c_count += 1
        
        prefix = set()
        for i in parts:
            if "*" in i:
                if not prefix:
                    prefix.add(f"{i[1]}")
                    prefix.add(f"{i[1]}{i[1]}")
                else:
                    new_prefix = set()
                    for j in prefix:
                        new_prefix.add(f"{j}{i[1]}")
                        new_prefix.add(f"{j}{i[1]}{i[1]}")
                    prefix = new_prefix
            else:
                if not prefix:
                    prefix.add(i)
                else:
                    new_prefix = set()
                    for j in prefix:
                        new_prefix.add(f"{j}{i}")
                    prefix = new_prefix
        return len(prefix & set(words))
                
            
