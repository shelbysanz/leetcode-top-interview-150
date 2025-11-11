class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_array = s.split(' ')
        if len(word_array) != len(pattern):
            return False

        word_to_pattern: dict[str,str] = {}
        pattern_to_word: dict[str,str] = {}
        for word, pattern_char in zip(word_array, pattern):
            if word in word_to_pattern:
                if word_to_pattern[word] != pattern_char:
                    return False
            else:
                word_to_pattern[word] = pattern_char
            if pattern_char in pattern_to_word:
                if pattern_to_word[pattern_char] != word:
                    return False
            else:
                pattern_to_word[pattern_char] = word
        return True


if __name__ == "__main__":
    assert Solution().wordPattern("abba", "dog cat cat dog") == True
    assert Solution().wordPattern("abba", "dog dog dog dog") == False
    assert Solution().wordPattern("abba", "dog dog dog dog") == False
