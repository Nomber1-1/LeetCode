class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        """ TODO:
        1. Fill column with letters until reach bottom or no more letters
        2. Fill diagonal until reach top row or no more letters
        3. Repeat until no more letters
        4. Read rows skipping empty spaces
        """
        arr = []
        for i in range(numRows):
            arr.append([])
        
        cur_col = 0
        cur_row = 0
        
        i = 0
        while i < len(s): # while still letters
            if cur_row == 0: # fill_column(arr, s, numRows, cur_col)
                while(cur_row != numRows and i < len(s)):
                    print(f"fill_col: cur row is {cur_row}, cur col is {cur_col}, the letter here is {s[i]}")
                    arr[cur_row].append(s[i])
                    i = i + 1
                    cur_row = cur_row + 1
                    
            else: #fill_diagonal(arr, s, numRows, cur_col)
                # check if at first row
                cur_row = cur_row - 1
                while (cur_row < numRows and cur_row > 1 and i < len(s)):
                    cur_col = cur_col + 1
                    cur_row = cur_row - 1
                    arr[cur_row].append(s[i])
                    print(f"fill_diag: cur row is {cur_row}, cur col is {cur_col}, the letter here is {s[i]}")
                    i = i + 1
        
        print("############################################")
        m = ""
        for row in arr:
            print(f"the row contains {row}")
            for col in row:
                m = m + col
                print(f"letter is {col}, the letter here is {m}")
                
        return m
    
    """ - Alternative Solution - 
    class Solution(object):
    def convert(self,s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        index, step = 0, 1


        for char in s:
            result[index] += char

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step
        return ''.join(result)
    """
    
if __name__ == "__main__":
    a = Solution()
    print(a.convert("PAYPALISHIRING", 4)) # PSHAIIYLRPAIN