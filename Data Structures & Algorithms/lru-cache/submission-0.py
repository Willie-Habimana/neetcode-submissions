class Node:
    def __init__(self, key: int=0, val: int=0, next: Node=None, prev:Node=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node(self, node:Node) -> None:
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove_node(node)
            self.add_node(node)
            node.val = value
        else:
            self.hmap[key] = Node(key, value)
            self.add_node(self.hmap[key])
            if len(self.hmap) > self.capacity:
                node = self.tail.prev
                del self.hmap[node.key]
                self.tail.prev = node.prev
                node.prev.next = self.tail
        
        
