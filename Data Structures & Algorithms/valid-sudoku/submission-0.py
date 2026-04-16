class Solution: 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_boxes = [set() for _ in range(9)]

        for row in range(9):
            curr_row = set()
            curr_column = set() 
            for column in range(9):

                x_row = board[row][column]

                # check sub-boxes
                sub_index = 3 * (row // 3) + column // 3
                if x_row == '.':
                    pass
                elif x_row not in sub_boxes[sub_index]:
                    sub_boxes[sub_index].add(x_row)
                else:  
                    return False
                
                # check row 
                if x_row == '.':
                    pass
                elif x_row not in curr_row:
                    curr_row.add(x_row)
                else:
                    return False

                # check column
                x_col  = board[column][row]
                if x_col == '.':
                    pass
                elif x_col not in curr_column and x_col != '.':
                    curr_column.add(x_col)
                else:
                    return False
                    
            print(curr_row)

        return True