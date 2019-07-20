# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        d = dict()
        # Dict is to store the indices of inorder elems
        # In inorder array, if any elem's index > than root/other element,
        # then that element is considered greater. 
        # Using dict we can identify which elem is greater in O(1) time.

        for i in range(len(A)):
            d[A[i]] = i

        # since it is postorder, last elem is root
        # Reverse array B, or traverse from right to left
        real_root = TreeNode(B[-1])
        B.reverse()
        
        # Call insert_tree() for all the susequent elements in postorder
        for item in B[1:]:
            self.insert_tree(real_root, item, d)
        return real_root
    
    def insert_tree(self, root, elem, d):
        node = root
        prev = node
        while node:
            place_value = d[elem] - d[node.val]
            prev = node

            # Element is larger than current node
            if place_value > 0:
                node = node.right
            
            # Element is smaller than current node
            elif place_value < 0:
                node = node.left
        # Create a new TreeNode with elem as its value.
        new_node = TreeNode(elem)
        
        # Prev holds the object at which node will be inserted
        node = prev  # since node becomes None
        
        # Isert the element at correct position
        if d[node.val] > d[elem]:
            node.left = new_node
        elif d[node.val] < d[elem]:
            node.right = new_node
