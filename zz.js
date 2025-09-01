function generateBinary(n) {
    let res = []
    let path = ""

    function backtrack(result) {
        if (path.length === n) {
            res.push(path)
            return
        }

        for (let i of [0, 1]) {
            path = path + i
            backtrack(result)
            path = path.substring(0, path.length - 1)
        }
    }

    backtrack(3)
    return res
}

console.log(generateBinary(3))