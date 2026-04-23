
"""
Time complexity: O(1)
Worst case will run 1440 times
"""

class Solution:
    def nextClosestTime(self, time: str) -> str:
        available = set([i for i in time if i != ':'])
        time = time.split(':')
        curr = int(time[0]) * 60 + int(time[1])

        def isValid(time_str):
            for i in time_str:
                if i not in available:
                    return False
            return True

        while True:
            curr += 1
            # next day
            if curr == 1440:
                curr = 0

            time_str = str(curr // 60).rjust(2,'0') + str(curr % 60).rjust(2, '0')
            valid = isValid(time_str)
            if not valid:
                continue

            return time_str[:2] + ':' + time_str[2:]
