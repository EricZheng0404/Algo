class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # The first edge to be taken, since the constraint is at least one sign
        edges = 1
        for sign in preorder.split(","):
            # A Null node takes one edge
            if sign == "#":
                edges -= 1
                if edges  < 0:
                    return False
            else:
                # A TreeNode takes one edge
                edges -= 1
                # We check this condition right away. 
                # If there's no edge to be taken, we immediately return False
                if edges < 0:
                    return False
                # It also gives 2 more edges
                edges += 2
        # To be sure that all edges are taken
        return edges == 0
