class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strNum = str(n)
        flag = len(strNum)

        # from right to left
        for i in range(len(strNum)-1, 0, -1):
            #if the second last > the last
            # record the i the last as flag
            # change the second last -1
            if strNum[i - 1] > strNum[i]:
                flag = i 
                strNum = strNum[:i - 1] + str(int(strNum[i - 1]) - 1) + strNum[i:]

        # change the element behind the flag as 9 
        for i in range(flag, len(strNum)):
            strNum = strNum[:i] + '9' + strNum[i + 1:]

        return int(strNum)