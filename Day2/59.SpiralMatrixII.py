from ast import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startx, starty = 0, 0
        middle, loop = n // 2, n // 2
        count = 1 #be careful 
        result = [[0]*n for _ in range(n)]

        for offset in range(1, loop+1):
            #from left ot right 
            for i in range(starty, n - offset):
                result[startx][i] = count
                count += 1
            #from top to bottom 
            for i in range(startx, n - offset):
                result[i][n - offset] = count
                count += 1
            #from right to left
            for i in range(n - offset, starty, -1):
                result[n - offset][i] = count
                count += 1
            #from bottom to top
            for i in range(n - offset, startx, -1):
                result[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        if n % 2 != 0 : 
            result[middle][middle] = count
        return result

#Thinking: 
#1. since the question start from 1 not 0, so the count should be 1
#2. offset is 1 because only one number also is a loop 
#3. 