class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}  # maps key -> Node
        
        # Use dummy head and tail nodes to avoid edge cases (like empty lists)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Removes a node from its current position in the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node):
        """Always inserts a node right before the dummy tail (most recently used)."""
        prev_node = self.tail.prev
        
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add_to_tail(node)  # Move to tail because it was just accessed
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            # Update existing key
            node = self.dic[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            # Create new key
            if len(self.dic) == self.capacity:
                # Evict least recently used (the node right after dummy head)
                lru_node = self.head.next
                self._remove(lru_node)
                del self.dic[lru_node.key]
                
            new_node = Node(key, value)
            self.dic[key] = new_node
            self._add_to_tail(new_node)