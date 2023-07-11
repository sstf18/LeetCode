from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0 
        points.sort(key=lambda x:x[0])
        result = 1
        for i in range(1, len(points)):
            # i's left > i-1's right
            if points[i][0] > points[i - 1][1]:
                result += 1
            else: 
                # i's right = min(i-1's right, i's right)
                points[i][1] = min(points[i - 1][1], points[i][1])
        return result


# main point is that:
# after sort points list, one the left side 
# in a for loop, if the second left > first right, then result += 1 
# min(one the right side) to iterator get the mutiple ballon