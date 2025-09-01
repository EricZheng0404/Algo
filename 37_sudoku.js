/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    let found = false

    function backtrack(board, index) {
        // Use the index to get the row number
        let i = Math.floor(index / 9)
        // Use the index to get the col number
        let j = index % 9
        // It need to be up to 81th that we can get the final result 
        // because the result index is 0 to 81
        if (index == 81) {
            found = true
            return
        }
        // If the index on the board is a preset number (not .), we can go to 
        // the next level
        if (board[i][j] != ".") {
            backtrack(board, index + 1) // I forgot to go into the next level
            return
        }
        // Every single cell has 9 possibilities from 1 to 9
        for(let c = 1; c <= 9; c++) {
            ch = `${c}`
            // We now try if we put the character into the board, it will fit or not
            if (!isValid(board, i, j, ch)) {
                continue
            }
            board[i][j] = ch
            backtrack(board, index + 1)
            // backtrack can set found variable. So, if the variable is updated in the function, it will be reflected in here
            if (found) {
                return
            }
            board[i][j] = "."
        }

    }
    function isValid(board, row, col, ch) {
        for (let i = 0; i < 9; i++) {
            // All numbers are different in the same row
            if (board[row][i] == ch) return false
            // All numbers are different in the same column
            if (board[i][col] == ch) return false
            // All numbers are diffferent in the same 3 * 3 box
            if (board[Math.floor(row / 3) * 3 + Math.floor(i / 3)][Math.floor(col / 3) * 3 + i % 3] == ch) return false
        }
        return true
    }

    // To call the function 
    backtrack(board, 0)
};