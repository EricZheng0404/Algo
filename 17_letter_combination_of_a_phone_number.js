/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length === 0) {
        return []
    }
    let res = []
    let path = []
    let mapping = [
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    ];

    function backtrack(start) {
        if (start == digits.length) {
            res.push(path.join(''))
            return
        }
        let chars = mapping[parseInt(digits[start])]
        for (let char of chars) {
            path.push(char)
            backtrack(start + 1)
            path.pop()
        }
    }
    backtrack(0)
    return res
};

console.log(letterCombinations("23"))