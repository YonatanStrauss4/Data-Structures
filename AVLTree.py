
# username - Strauss1
# id1      - 208582502
# name1    - Yonatan Strauss
# id2      - 322712001
# name2    - Tal Dotan

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: any
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        return self.height

    """returns the size of the subtree

    @rtype: int
    @returns: the size of the subtree of self, 0 if the node is virtual
    """

    def get_size(self):
        return self.size

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h

    """sets the size of node

    @type s: int
    @param s: the size
    """

    def set_size(self, s):
        self.size = s

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.key is not None



"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        self.tree_size = 0

    # add your fields here



    """"searches for a value in the dictionary corresponding to the key

        @type key: int
        @param key: a key to be searched
        @rtype: any
        @returns: the value corresponding to key.
        """

    def search(self, key):     # O(log(n))
        node = self.root
        while node.get_key() is not None:
            if key == node.get_key():
                return node
            elif key < node.get_key():
                node = node.get_left()
            else:
                node = node.get_right()
        return node

    """inserts val at position i in the dictionary

        @type key: int
        @pre: key currently does not appear in the dictionary
        @param key: key of item that is to be inserted to self
        @type val: any
        @param val: the value of the item
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
    def right_rotation(self, node):                           # right rotation method
        if self.root.get_key() == node.get_key():             # special case for rotation at the top of the tree
            self.root = node.get_left()                       # changing the root to the new one (because of rotation)
        a = node.get_left()                                   # no need to explain much on the further lines, it's just implamating the rotation algorithm from slideshow
        node.set_left(a.get_right())
        node.get_left().set_parent(node)
        a.set_right(node)
        a.set_parent(node.parent)
        if a.get_parent() is not None:
            if a.get_parent().get_key() < a.get_key():
                a.get_parent().set_right(a)
            else:
                a.get_parent().set_left(a)
        node.parent = a
        node.set_height(max(node.get_left().get_height(), node.get_right().get_height()) + 1)  # next lines are updating the size and height of the rotated nodes
        a.set_height(max(a.get_left().get_height(), a.get_right().get_height()) + 1)
        node.set_size(node.get_left().get_size() + node.get_right().get_size() + 1)
        a.set_size(a.get_left().get_size() + a.get_right().get_size() + 1)


    def left_rotation(self, node):                        # right rotation method
        if self.root.get_key() == node.get_key():         # special case for rotation at the top of the tree
            self.root = node.get_right()                  # changing the root to the new one (because of rotation)
        a = node.get_right()                              # no need to explain much on the further lines, it's just implamating the rotation algorithm from slideshow
        node.set_right(a.get_left())
        node.get_right().set_parent(node)
        a.set_left(node)
        a.set_parent(node.parent)
        if a.get_parent() is not None:
            if a.get_parent().get_key() < a.get_key():
                a.get_parent().set_right(a)
            else:
                a.get_parent().set_left(a)
        node.parent = a
        node.set_height(max(node.get_left().get_height(), node.get_right().get_height()) + 1)  # next lines are updating the size and height of the rotated nodes
        a.set_height(max(a.get_left().get_height(), a.get_right().get_height()) + 1)
        node.set_size(node.get_left().get_size() + node.get_right().get_size() + 1)
        a.set_size(a.get_left().get_size() + a.get_right().get_size() + 1)


    def insert(self, key, val):              #insert method O(log(n))
        num_of_balance_act = 0
        bf = 0                              # balance factor
        parent = None
        node = self.root
        while node is not None and node.get_key() is not None:     # loop to get to the 'good' position
            parent = node
            if key < node.get_key():
                node = node.get_left()
            else:
                node = node.get_right()
            parent.set_size(parent.get_size() + 1)                 #updating size of subtree of parent (each iteration different parent)

        if parent is None:                              # if tree was empty
            self.root = AVLNode(key, val)               # inserting the root
            self.root.set_size(1)                       # setting size of root
            self.root.set_left(AVLNode(None, None))     # creating virtual left child
            self.root.get_left().set_parent(self.root)
            self.root.set_right(AVLNode(None, None))    # creating virtual right child
            self.root.get_right().set_parent(self.root)
            self.root.set_height(0)                     # setting the height to be zero
            self.tree_size += 1                         # updating size of tree

        elif key < parent.get_key():
            parent.set_left(AVLNode(key, val))                 # setting the new node as left child of parent
            parent.get_left().set_parent(parent)               # connecting the new node to its parent
            parent.get_left().set_left(AVLNode(None, None))    # creating virtual left child
            parent.get_left().get_left().set_parent(parent.get_left())
            parent.get_left().set_right(AVLNode(None, None))   # creating virtual right child
            parent.get_left().get_right().set_parent(parent.get_left())
            parent.get_left().set_height(0)                    # setting the height of the new node to zero
            parent.get_left().set_size(1)                      # setting size of  new node to one
            self.tree_size += 1  # updating tree size after insertion of 1 node



        else:
            parent.set_right(AVLNode(key, val))                 # setting the new node as right child of parent
            parent.get_right().set_parent(parent)               # connecting the new node to its parent
            parent.get_right().set_left(AVLNode(None, None))    # creating virtual right child
            parent.get_right().get_left().set_parent(parent.get_right())
            parent.get_right().set_right(AVLNode(None, None))   # creating virtual left child
            parent.get_right().get_right().set_parent(parent.get_right())
            parent.get_right().set_height(0)                    # setting the height of the new node to zero
            parent.get_right().set_size(1)                      # setting size of  new node to one
            self.tree_size += 1  # updating tree size after insertion of 1 node



        # now we're going to do some rotations
        while parent is not None:                               # in rotations, we work on the parents height
            bf = parent.get_left().get_height() - parent.get_right().get_height()  # calculating balance factor for parent
            tmp_height = parent.get_height()                                       # keeping the current parent high for further computings
            parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)  #setting the new parent high and size
            parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
            if abs(bf) < 2 and tmp_height == parent.get_height():     # checking what we need to know about balance factor and the change in parent high before and after insertion
                return num_of_balance_act                                   # no need to rotate
            elif abs(bf) < 2 and tmp_height != parent.get_height():   # checking again
                num_of_balance_act += 1  # the height update of the parent counts as a balancing act
                parent = parent.get_parent()                          # no need to rotate, go up and check the next parent
                continue
            else:                                                     # need some rotations
                if bf == -2:
                    num_of_balance_act += 1
                    right_bf = parent.get_right().get_left().get_height() - parent.get_right().get_right().get_height()  # checking balance factor for right child
                    if right_bf == -1:
                        self.left_rotation(parent)            # rotate left on the parent!
                    else:
                        num_of_balance_act += 1
                        self.right_rotation(parent.get_right())       # rotate right on the right child and then left on parent
                        self.left_rotation(parent)
                else:
                    num_of_balance_act += 1
                    left_bf = parent.get_left().get_left().get_height() - parent.get_left().get_right().get_height()  # checking balance factor for left child
                    if left_bf == 1:
                        self.right_rotation(parent)     # rotate right on the parent!
                    else:
                        num_of_balance_act += 1
                        self.left_rotation(parent.get_left())   # rotate left on the left child and then right on parent
                        self.right_rotation(parent)
        return num_of_balance_act                                     # return the number of rotations that happened



    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):
        num_of_balance_act = 0
        parent = node.get_parent()
        if node.get_height() == 0:  # if node is a leaf
            self.delete_leaf(node)
        elif node.get_right().get_key() is not None and node.get_left().get_key() is None:
            self.delete_only_right_child(node)
        elif node.get_left().get_key() is not None and node.get_right().get_key() is None:
            self.delete_only_left_child(node)
        else:
            successor = node.get_right()
            while successor.get_left().get_key() is not None:
                successor = successor.get_left()
            parent = successor.get_parent()
            self.delete_with_two_children(node)

        # now we're going to do some rotations
        while parent is not None:  # in rotations, we work on the parents height
            bf = parent.get_left().get_height() - parent.get_right().get_height()  # calculating balance factor for parent
            tmp_height = parent.get_height()  # keeping the current parent high for further computings
            parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)  # setting the new parent high
            if abs(bf) < 2 and tmp_height == parent.get_height():  # checking what we need to know about balance factor and the change in parent high before and after insertion
                parent = parent.get_parent()  # no need to rotate, go up and check the next parent
                continue
            elif abs(bf) < 2 and tmp_height != parent.get_height():  # checking again
                num_of_balance_act += 1  # the height update of the parent counts as a balancing act
                parent = parent.get_parent()  # no need to rotate, go up and check the next parent
                continue
            else:  # need some rotations
                if bf == -2:
                    num_of_balance_act += 1
                    right_bf = parent.get_right().get_left().get_height() - parent.get_right().get_right().get_height()  # checking balance factor for right child
                    if right_bf == -1 or right_bf == 0:
                        self.left_rotation(parent)  # rotate left on the parent!
                    else:
                        num_of_balance_act += 1
                        self.right_rotation(
                            parent.get_right())  # rotate right on the right child and then left on parent
                        self.left_rotation(parent)
                    parent = parent.get_parent()  # no need to rotate, go up and check the next parent
                    continue
                else:
                    num_of_balance_act += 1
                    left_bf = parent.get_left().get_left().get_height() - parent.get_left().get_right().get_height()  # checking balance factor for left child
                    if left_bf == 1 or left_bf == 0:
                        self.right_rotation(parent)  # rotate right on the parent!
                    else:
                        num_of_balance_act += 1
                        self.left_rotation(parent.get_left())  # rotate left on the left child and then right on parent
                        self.right_rotation(parent)
                    continue

        return num_of_balance_act  # return the number of balances

    def delete_leaf(self, node):  # deleting a leaf node in an AVL tree
        if node == self.get_root():  # tree contains only this node
            self.root = None
            self.tree_size = 0
            return self
        if node.get_parent().get_left() is node:  # node is the left child of its parent
            parent = node.get_parent()
            parent.set_left(AVLNode(None, None))
            parent.get_left().set_parent(parent)
            parent.set_height(max(parent.get_right().get_height(), parent.get_left().get_height()) + 1)
            parent.set_size(parent.get_size() - 1)
            while parent.get_parent() is not None:  # updating the size and heights of the parents
                p2 = parent.get_parent()
                p2.set_size(p2.get_size() - 1)
                p2.set_height(max(p2.get_left().get_height(), p2.get_right().get_height()) + 1)
                parent = parent.get_parent()

        else:  # node is the right child of its parent
            parent = node.get_parent()
            parent.set_right(AVLNode(None, None))
            parent.get_right().set_parent(parent)
            parent.set_height(max(parent.get_right().get_height(), parent.get_left().get_height()) + 1)
            parent.set_size(parent.get_size() - 1)
            while parent.get_parent() is not None:  # updating the size and heights of the parents
                p2 = parent.get_parent()
                p2.set_size(p2.get_size() - 1)
                p2.set_height(max(p2.get_left().get_height(), p2.get_right().get_height()) + 1)
                parent = parent.get_parent()
        self.tree_size -= 1
        return self

    def delete_only_left_child(self, node):  # deleting a node that has only a left child
        if node == self.get_root():
            self.root = node.get_left()
            node.get_left().set_parent(None)
            node.set_left(None)
            self.tree_size -= 1
            return self
        if node.get_parent().get_left() == node:  # node is the left child of its parent
            parent = node.get_parent()
            parent.set_left(node.get_left())
            parent.get_left().set_parent(parent)
            node.set_parent(None)
            node.set_left(None)
            parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)
            parent.set_size(parent.get_size() - 1)
            while parent.get_parent() is not None:  # updating the size and heights of the parents
                p2 = parent.get_parent()
                p2.set_size(p2.get_size() - 1)
                p2.set_height(max(p2.get_left().get_height(), p2.get_right().get_height()) + 1)
                parent = parent.get_parent()

        else:  # node is the right child of its parent
            parent = node.get_parent()
            parent.set_right(node.get_left())
            parent.get_right().set_parent(parent)
            node.set_parent(None)
            node.set_left(None)
            parent.set_height(max(parent.get_right().get_height(), parent.get_left().get_height()) + 1)
            parent.set_size(parent.get_size() - 1)
            while parent.get_parent() is not None:  # updating the size and heights of the parents
                p2 = parent.get_parent()
                p2.set_size(p2.get_size() - 1)
                p2.set_height(max(p2.get_left().get_height(), p2.get_right().get_height()) + 1)
                parent = parent.get_parent()
        self.tree_size -= 1
        return self

    def delete_only_right_child(self, node):  # deleting a node that has only a right child
        if node == self.get_root():
            self.root = node.get_right()
            node.get_right().set_parent(None)
            node.set_right(None)
        elif node.get_parent().get_right() == node:  # node is the right child of its parent
            parent = node.get_parent()
            parent.set_right(node.get_right())
            parent.get_right().set_parent(parent)
            node.set_parent(None)
            node.set_right(None)
            parent.set_height(max(parent.get_right().get_height(), parent.get_left().get_height()) + 1)
            parent.set_size(parent.get_size() - 1)
            while parent.get_parent() is not None:  # updating the size and heights of the parents
                p2 = parent.get_parent()
                p2.set_size(p2.get_size() - 1)
                p2.set_height(max(p2.get_left().get_height(), p2.get_right().get_height()) + 1)
                parent = parent.get_parent()
        else:  # node is the left child of its parent
            parent = node.get_parent()
            parent.set_left(node.get_right())
            parent.get_left().set_parent(parent)
            node.set_parent(None)
            node.set_right(None)
            parent.set_height(max(parent.get_right().get_height(), parent.get_left().get_height()) + 1)
            parent.set_size(parent.get_size() - 1)
            while parent.get_parent() is not None:  # updating the size and heights of the parents
                p2 = parent.get_parent()
                p2.set_size(p2.get_size() - 1)
                p2.set_height(max(p2.get_left().get_height(), p2.get_right().get_height()) + 1)
                parent = parent.get_parent()
        self.tree_size -= 1
        return self

    def delete_with_two_children(self, node):  # deleting a node that has two children
        successor = node.get_right()
        while successor.get_left().get_key() is not None:
            successor = successor.get_left()
        node.set_key(successor.get_key())
        node.set_value(successor.get_value())
        if successor.get_size() == 1:  # if successor is a leaf
            self.delete_leaf(successor)
        else:  # if successor has a right child (cannot have a left child)
            self.delete_only_right_child(successor)
        return self

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):                    # O(n)
        if self.root is None:                  # special case tree is empty
            return []
        arr = []
        node = self.root
        return self.in_order(node, arr)        # calling the recursive method

    def in_order(self, node, arr):             # simple in order traverse. nothing to explain here (append is O(1))
        if node.get_key() is not None:
            self.in_order(node.get_left(), arr)
            arr.append((node.get_key(), node.get_value()))
            self.in_order(node.get_right(), arr)
        return arr




    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        if self.root is None:
            return 0
        return self.get_root().get_size()

    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):  # O(log(n))

        T1 = AVLTree()
        T2 = AVLTree()
        T = AVLTree()

        if node.get_left().get_key() is not None:  # node has a left child

            T1.root = node.get_left()
            T1.tree_size = node.get_left().get_size()
            T1.get_root().set_parent(None)

        if node.get_right().get_key() is not None:  # node has a right child

            T2.root = node.get_right()
            T2.tree_size = node.get_right().get_size()
            T2.get_root().set_parent(None)

        while node != self.get_root():

            parent = node.get_parent()

            if parent.get_right() == node:  # node is the left child of its parent

                T.root = parent.get_left()
                T.tree_size = parent.get_left().get_size()
                T.get_root().set_parent(None)
                T1.join(T, parent.get_key(), parent.get_value())

            else:  # node is the right child of its parent

                T.root = parent.get_right()
                T.tree_size = parent.get_right().get_size()
                T.get_root().set_parent(None)
                T2.join(T, parent.get_key(), parent.get_value())

            node = node.get_parent()

        return [T1, T2]

    """joins self with key and another AVLTree

    @type tree: AVLTree 
    @param tree: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree are larger than key,
    or the other way around.
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree, key, val):               # O(height(higher tree)-height(lower tree) +1)
        if self.root is None and tree.get_root() is None:
            self.insert(key, val)
            return 0
        if self.root is None:                     # if the original tree is empty
            self.root = tree.get_root()
            self.tree_size = tree.tree_size
            self.insert(key, val)
            return tree.get_root().get_height()
        if tree.get_root() is None:               # if the added tree is empty
            self.insert(key, val)
            return self.root.get_height()
        h_original = self.root.get_height()       # height of first tree
        h_added = tree.get_root().get_height()    # height of second tree
        new_node = AVLNode(key, val)
        node = tree.get_root()                    # root of second tree
        orig_node = self.root                     # root of first tree
        node2 = tree.get_root()                   # again root of second tree for updating the self.root later
        orig_node2 = self.root                    # again root of first tree for updating the self.root later
        if node.get_key() > orig_node.get_key():        # we are gonna check two conditions, and in each one of this conditions we are going two check three conditions. this is the first condition from the two, checking which tree got the bigger keys.
            if h_added > h_original:                    # first condition of the three. checking which tree is higher
                while node.get_height() > h_original:   # getting to the first subtree with high equal or less by 1 to the high of shorter tree
                    node = node.get_left()
                parent = node.get_parent()              # next lines are performing the join algorithm learn in class
                new_node.set_right(node)
                node.set_parent(new_node)
                new_node.set_left(orig_node)
                orig_node.set_parent(new_node)
                new_node.set_parent(parent)
                if parent is not None:
                    parent.set_left(new_node)
                self.root = node2
                new_node.set_height(max(new_node.get_left().get_height(), new_node.get_right().get_height()) + 1)  # next two lines are updating size and height of connective new node
                new_node.set_size(new_node.get_left().get_size() + new_node.get_right().get_size() + 1)
                while parent is not None:                                                   # next lines are exactly the same algorithm for rebalancing and rotations from insert. were doing this from the new node and up
                    bf = parent.get_left().get_height() - parent.get_right().get_height()
                    parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)  # setting the new parent high and size
                    parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
                    if bf == -2:
                        right_bf = parent.get_right().get_left().get_height() - parent.get_right().get_right().get_height()  # checking balance factor for right child
                        if right_bf == -1 or right_bf == 0:
                            self.left_rotation(parent)  # rotate left on the parent!
                        else:
                            self.right_rotation(parent.get_right())  # rotate right on the right child and then left on parent
                            self.left_rotation(parent)
                    elif bf == 2:
                        left_bf = parent.get_left().get_left().get_height() - parent.get_left().get_right().get_height()  # checking balance factor for left child
                        if left_bf == 1 or left_bf == 0:
                            self.right_rotation(parent)  # rotate right on the parent!
                        else:
                            self.left_rotation(parent.get_left())  # rotate left on the left child and then right on parent
                            self.right_rotation(parent)
                    else:
                        parent = parent.get_parent()     # keep going up!
                self.tree_size = self.root.get_size()      # updating size of tree
                return h_added - h_original + 1

            elif h_added < h_original:                   # the original tree is higher this time
                while orig_node.get_height() > h_added:  # getting to the first subtree with high equal or less by 1 to the high of shorter tree
                    orig_node = orig_node.get_right()
                parent = orig_node.get_parent()          # next lines are performing the join algorithm learn in class
                new_node.set_left(orig_node)
                orig_node.set_parent(new_node)
                new_node.set_right(node)
                node.set_parent(new_node)
                new_node.set_parent(parent)
                if parent is not None:
                    parent.set_right(new_node)
                self.root = orig_node2
                new_node.set_height(max(new_node.get_left().get_height(), new_node.get_right().get_height()) + 1)  # next two lines are updating size and height of connective new node
                new_node.set_size(new_node.get_left().get_size() + new_node.get_right().get_size() + 1)
                while parent is not None:                                    # next lines are exactly the same algorithm for rebalancing and rotations from insert. were doing this from the new node and up
                    bf = parent.get_left().get_height() - parent.get_right().get_height()
                    parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)  # setting the new parent high and size
                    parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
                    if bf == -2:
                        right_bf = parent.get_right().get_left().get_height() - parent.get_right().get_right().get_height()  # checking balance factor for right child
                        if right_bf == -1 or right_bf == 0:
                            self.left_rotation(parent)  # rotate left on the parent!
                        else:
                            self.right_rotation(parent.get_right())  # rotate right on the right child and then left on parent
                            self.left_rotation(parent)
                    elif bf == 2:
                        left_bf = parent.get_left().get_left().get_height() - parent.get_left().get_right().get_height()  # checking balance factor for left child
                        if left_bf == 1 or left_bf == 0:
                            self.right_rotation(parent)  # rotate right on the parent!
                        else:
                            self.left_rotation(parent.get_left())  # rotate left on the left child and then right on parent
                            self.right_rotation(parent)
                    else:
                        parent = parent.get_parent()       # keep going up!
                self.tree_size = self.root.get_size()      # updating size of tree
                return h_original - h_added + 1


            elif h_added == h_original:                 # trees are same height, no need to rebalance
                new_node.set_right(node)                # joining the trees, its simpler in this condition
                node.set_parent(new_node)
                new_node.set_left(orig_node)
                orig_node.set_parent(new_node)
                self.root = new_node
                new_node.set_height(max(new_node.get_left().get_height(), new_node.get_right().get_height()) + 1)   # next two lines are updating size and height of connective new node
                new_node.set_size(new_node.get_left().get_size() + new_node.get_right().get_size() + 1)
                self.tree_size = self.root.get_size()      # updating size of tree
                return 1

        else:                                              # now the original tree has bigger keys
            if h_added > h_original:                       # first condition of the three. checking which tree is higher
                while node.get_height() > h_original:      # getting to the first subtree with high equal or less by 1 to the high of shorter tree
                    node = node.get_right()
                parent = node.get_parent()                 # next lines are performing the join algorithm learn in class
                new_node.set_left(node)
                node.set_parent(new_node)
                new_node.set_right(orig_node)
                orig_node.set_parent(new_node)
                new_node.set_parent(parent)
                if parent is not None:
                    parent.set_right(new_node)
                self.root = node2
                new_node.set_height(max(new_node.get_left().get_height(), new_node.get_right().get_height()) + 1)  # next two lines are updating size and height of connective new node
                new_node.set_size(new_node.get_left().get_size() + new_node.get_right().get_size() + 1)
                while parent is not None:                        # next lines are exactly the same algorithm for rebalancing and rotations from insert. were doing this from the new node and up
                    bf = parent.get_left().get_height() - parent.get_right().get_height()
                    parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)  # setting the new parent high and size
                    parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
                    if bf == -2:
                        right_bf = parent.get_right().get_left().get_height() - parent.get_right().get_right().get_height()  # checking balance factor for right child
                        if right_bf == -1 or right_bf == 0:
                            self.left_rotation(parent)  # rotate left on the parent!
                        else:
                            self.right_rotation(parent.get_right())  # rotate right on the right child and then left on parent
                            self.left_rotation(parent)
                    elif bf == 2:
                        left_bf = parent.get_left().get_left().get_height() - parent.get_left().get_right().get_height()  # checking balance factor for left child
                        if left_bf == 1 or left_bf == 0:
                            self.right_rotation(parent)  # rotate right on the parent!
                        else:
                            self.left_rotation(parent.get_left())  # rotate left on the left child and then right on parent
                            self.right_rotation(parent)
                    else:
                        parent = parent.get_parent()               # keep going up!
                self.tree_size = self.root.get_size()      # updating size of tree
                return h_added - h_original + 1

            elif h_added < h_original:                             # the original tree is higher this time
                while orig_node.get_height() > h_added:            # getting to the first subtree with high equal or less by 1 to the high of shorter tree
                    orig_node = orig_node.get_left()
                parent = orig_node.get_parent()                    # next lines are performing the join algorithm learn in class
                new_node.set_right(orig_node)
                orig_node.set_parent(new_node)
                new_node.set_left(node)
                node.set_parent(new_node)
                new_node.set_parent(parent)
                if parent is not None:
                    parent.set_left(new_node)
                self.root = orig_node2
                new_node.set_height(max(new_node.get_left().get_height(), new_node.get_right().get_height()) + 1)   # next two lines are updating size and height of connective new node
                new_node.set_size(new_node.get_left().get_size() + new_node.get_right().get_size() + 1)
                while parent is not None:                                # next lines are exactly the same algorithm for rebalancing and rotations from insert. were doing this from the new node and up
                    bf = parent.get_left().get_height() - parent.get_right().get_height()
                    parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)  # setting the new parent high and size
                    parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
                    if bf == -2:
                        right_bf = parent.get_right().get_left().get_height() - parent.get_right().get_right().get_height()  # checking balance factor for right child
                        if right_bf == -1 or right_bf == 0:
                            self.left_rotation(parent)  # rotate left on the parent!
                        else:
                            self.right_rotation(parent.get_right())  # rotate right on the right child and then left on parent
                            self.left_rotation(parent)
                    elif bf == 2:
                        left_bf = parent.get_left().get_left().get_height() - parent.get_left().get_right().get_height()  # checking balance factor for left child
                        if left_bf == 1 or left_bf == 0:
                            self.right_rotation(parent)  # rotate right on the parent!
                        else:
                            self.left_rotation(parent.get_left())  # rotate left on the left child and then right on parent
                            self.right_rotation(parent)
                    else:
                        parent = parent.get_parent()               # keep going up!
                self.tree_size = self.root.get_size()      # updating size of tree
                return h_original - h_added + 1

            elif h_added == h_original:             # trees are same height, no need to rebalance
                new_node.set_right(orig_node)       # joining the trees, its simpler in this condition
                orig_node.set_parent(new_node)
                new_node.set_left(node)
                node.set_parent(new_node)
                self.root = new_node
                new_node.set_height(max(new_node.get_left().get_height(), new_node.get_right().get_height()) + 1)   # next two lines are updating size and height of connective new node
                new_node.set_size(new_node.get_left().get_size() + new_node.get_right().get_size() + 1)
                self.tree_size = self.root.get_size()      # updating size of tree
                return 1

    """compute the rank of node in the self

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    """

    def rank(self, node):                  # O(log(n))
        if self.root is None:              # special case tree is empty
            return None
        r = node.get_left().get_size() + 1     # the further lines are the algorithm from class, no need further explanations
        y = node
        while y != self.root:
            if y.get_parent().get_right() == y:
                r = r + y.get_parent().get_left().get_size() +1
            y = y.get_parent()
        return r


    """finds the i'th smallest item (according to keys) in self

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: int
    @returns: the item of rank i in self
    """

    def select(self, i):                        # O(log(n))
        return self.select_rec(self.root, i)    # calling the recursive method

    def select_rec(self, root, i):              # the recursive method
        if root is None:                        # special case if tree is empty
            return None
        r = root.get_left().get_size() + 1      # the next lines performs the recursion for select as learnt in class
        if i == r:
            return root
        elif i < r:
            return self.select_rec(root.get_left(), i)
        else:
            return self.select_rec(root.get_right(), i-r)


    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root