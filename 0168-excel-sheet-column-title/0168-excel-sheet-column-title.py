class Solution(object):
    def convertToTitle(self, columnNumber):
        title =""
        while columnNumber > 0:
            reminder = (columnNumber - 1) % 26
            title = chr(reminder + 65) +title
            columnNumber = (columnNumber- 1) // 26

        return title