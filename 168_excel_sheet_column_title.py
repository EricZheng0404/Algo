class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            # This is converted to 0-indexed
            numberIndex = (columnNumber) % 26
            # chr(numberIndex + ord("A")) gives the least significant 
            # digit
            res = chr(numberIndex + ord("A")) + res
            columnNumber = columnNumber // 26
        return res
