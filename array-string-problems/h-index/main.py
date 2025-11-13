class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)

        h_index = 0
        for index, citation in enumerate(citations):
            if index + 1 <= citation:
                h_index += 1
            else:
                break
        return 


