from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0], x[1]))
        que = []
        for p in people: 
            # p[1] means the second value in people
            # insert the index of peopel in p list. 
            que.insert(p[1], p)
        return que