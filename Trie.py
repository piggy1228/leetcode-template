#Trie
import collections
class Node:
    def __init__(self):
        self.val = None
        self.child = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.head = Node()
    def insert(self,vals):
        node = self.head
        for i,v in enumerate(vals[:-1]):
            node = node.child.get(v)
            if not node:
                return False
        node = node.child[vals[-1]]
        node.val = vals
        return True

        
