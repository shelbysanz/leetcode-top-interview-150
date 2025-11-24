class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)

        if len(ratings) <= 1:
            return sum(candies)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candies[i] = max(candies[i], candies[i - 1] + 1)

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


if __name__ == "__main__":
    assert Solution().candy([1, 0, 2]) == 5
    assert Solution().candy([1, 2, 2]) == 4
