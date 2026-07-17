class Node:

    def __init__(self, char: str = None):
        self.char = char
        self.children = {}




class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        i = 0
        curr = self.root
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        while i < len(word):
            new_node = Node(word[i])
            curr.children[word[i]] = new_node
            curr = new_node
            i += 1
        
        curr.children["EOW"] = Node()


    def search(self, word: str) -> bool:
        i = 0
        curr = self.root
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        return True if i == len(word) and "EOW" in curr.children else False
        

    def startsWith(self, prefix: str) -> bool:
        i = 0
        curr = self.root
        while i < len(prefix) and prefix[i] in curr.children:
            curr = curr.children[prefix[i]]
            i += 1
        
        return True if i == len(prefix) else False


        
        