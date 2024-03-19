def calc_size_of_subtree_rooted_at_u(u):
    u.sub_size = 1
    for w in u.children():
        u.sub_size = u.sub_size + calc_size_of_subtree_rooted_at_u(w)
    return u.sub_size

def visit_nodes_at_level(tree, k):
    if k == 0:
        print(tree.data)
    else:
        visit_nodes_at_level(tree.left, k - 1)
        visit_nodes_at_level(tree.right, k - 1)

def find_next_node_pre_order_traversal(u):
    if u.left is not None:
        return u.left
    elif u.right is not None:
        return u.right
    else:
        # Search for a node v, such that v is an ancestor of u
        # But v.right is not an ancestor or equal to u and v.right
        # is not None. If v is not found u is the last node in
        # the traversal
        pass

def find_next_node_in_order_traversal(u):
    if u.right is not None:
        # Next node is leftmost descendent of u.right
        return u.right.leftmost_descendent()
    else:
        v = u.parent
        # If we arrive at v from its left subtree then v is the next node
        if v.left == u:
            return v
        
        # Otherwise we keep updating v (v = v.parent) until v.right is not
        # an ancestor or equal to u then this final value of v is the next node
        else:
            while v.right is u.ancestor():
                v = v.parent
            return v

def find_next_node_post_order_traversal(u):
    if u.parent is None:
        # Then u is the root and this is the last node in the traversal
        return None
    else:
        v = u.parent
        if v.right == u:
            return v
        else:
            if v.right is None:
                # If v.right is None then v is the next node
                return v
            else:
                # If u is the left child of v then the next node is the leftmost
                # descendent of v.right
                return v.right.leftmost_descendent()
            

            
