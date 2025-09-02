/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    let res = 0
    let rank = 0
    function traverse(root, k) {
        if (root === null) {
            return
        }
        if (res != 0) {
            return
        }
        traverse(root.left, k)
        rank += 1
        if (rank == k) {
            res = root.val
        }
        traverse(root.right, k)
    }
    traverse(root, k)
    return res
};