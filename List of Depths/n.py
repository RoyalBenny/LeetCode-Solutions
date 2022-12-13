'''
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes 
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 
Hints: #107, #123, #135

'''

#Time :O(n)
# Space : O(n)

def BstToDepthLinkList(root):
    if not root:
        return []
    depth = []
    parent  = [root]
    addDepthList(depth,parent)
    return depth

def addDepthList(depth,parent):
    if not parent:
        return
    child = []
    tail = Node(parent[0],child)
    head = tail
    append(parent[0],child)
    for i in parent[1:]:
        tail.next = Node(i.val)
        tail = tail.next
        append(i,child)
    depth.append(head)
    addDepthList(depth,child)

def append(node,list):
    if node.left:
        list.append(node.left)
    if node.right:
        list.append(node.right)



    
