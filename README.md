This repository contains projects from the Data Structures course at Tel Aviv University. It includes:
AVL Tree implemented in Python
Binomial Heap implemented in Java

Overview of AVL Tree
The AVL Tree is a self-balancing binary search tree where the height difference between the left and right subtrees of any node is no more than one. This balance property ensures that operations such as search, insertion, and deletion can be performed in O(log n) time, where n is the number of nodes in the tree.

Key Functionalities:
Search (search(k))
Description: Searches for a node with the given key k. Returns a pointer to the node if found; otherwise, returns None.

Insert (insert(k, s))
Description: Inserts a node with key k and value s into the tree. Assumes that k does not already exist in the tree. Returns the total number of balancing operations required to complete the insertion.

Delete (delete(x))
Description: Deletes the node pointed to by x from the tree. Returns the total number of balancing operations required to complete the deletion.

Convert to Array (avl_to_array())
Description: Converts the AVL tree into a sorted array of key-value pairs, where each pair is represented as (key, value).

Size (size())
Description: Returns the number of nodes in the AVL tree.

Split (split(x))
Description: Splits the tree into two separate AVL trees based on the node x. One tree contains all nodes with keys smaller than x, and the other contains all nodes with keys greater than x. The original tree 
is not usable after this operation.

Join (join(t, k, s))
Description: Joins the current AVL tree with another AVL tree t and a new node with key k and value s. All keys in t are either smaller or larger than k. Returns the cost of the join operation, which is the height difference between the trees plus one.

Rank (rank(x))
Description: Returns the rank of the node x in the tree, where the rank is the position of the node in an in-order traversal of the tree.

Select (select(i))
Description: Finds and returns the node with the i-th smallest key in the AVL tree. Assumes that i is a valid rank.

Get Root (get_root())
Description: Returns a pointer to the root node of the AVL tree. Returns None if the tree is empty.

AVLNode Class
The AVLNode class includes:
get_key(): Returns the key of the node or None if the node is virtual.
get_value(): Returns the value of the node or None if the node is virtual.
get_left(): Returns the left child of the node or None if no left child exists.
get_right(): Returns the right child of the node or None if no right child exists.
get_parent(): Returns the parent of the node or None if no parent exists.
is_real_node(): Returns TRUE if the node is a real node (not virtual).
get_height(): Returns the height of the node, -1 if the node is virtual.
get_size(): Returns the size of the subtree rooted at the node, 0 if the node is virtual.

Additional Notes:
The tree includes virtual nodes (leaf nodes with no key) to simplify rotations and balancing operations.
Balancing operations such as rotations are performed during insertions and deletions to maintain the AVL tree property.

Binomial Heap Overview
This implementation of a Binomial Heap supports various heap operations on non-negative integers. A Binomial Heap is a data structure that supports efficient merge operations and is often used for priority queues. The main features and operations of this implementation include:

Insertion: Add a new element to the heap with a specified key and associated information.
Delete Minimum: Remove the element with the smallest key from the heap, efficiently reorganizing the heap structure.
Find Minimum: Retrieve the item with the smallest key without removing it.
Decrease Key: Reduce the key value of an existing item and adjust the heap structure to maintain heap properties.
Delete: Remove a specific item from the heap, using a combination of decrease key and delete minimum operations.
Meld: Merge two Binomial Heaps into a single heap, combining their elements while maintaining heap properties.
Size and Emptiness: Query the number of elements in the heap and check if the heap is empty.
Number of Trees: Get the count of binomial trees in the heap, providing insight into the heap's internal structure.

Key Classes
HeapNode: Represents a node in the Binomial Heap, containing a key, associated information, and links to child, next, parent nodes.
HeapItem: Represents the data item stored in the heap, including a key and associated information.
