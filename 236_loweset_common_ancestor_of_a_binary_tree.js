/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    let res = null
    function traverse(root) {
        // Base case: if it's a null, then we haven't found a match
        if (root === null) {
            return false
        }
        // Early termination
        if (res !== null) {
            return 
        }
        // Subproblems 
        let left = traverse(root.left)
        let right = traverse(root.right)
        let mid = (root === p || root === q)
        // If we've found 2 or more, then the current root is the answer
        if (left + right + mid >= 2) {
            res = root
        }
        return left || right || mid
    }
    traverse(root)
    return res
};