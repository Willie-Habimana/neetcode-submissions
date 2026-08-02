class TreeNode:

    def __init__(self, char = None, children = None):
        self.char = char
        self.children = children if children else {}


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        i = 0
        curr = self.root
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i+=1
        while i < len(word):
            new_node = TreeNode(word[i])
            curr.children[word[i]] = new_node
            curr = new_node
            i+=1
        curr.children["EOW"] = TreeNode()

    def search(self, word: str) -> bool:
        i = 0
        curr = self.root
        while i < len(word):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                i += 1
            else:
                return False
        return True if "EOW" in curr.children else False
        

    def startsWith(self, prefix: str) -> bool:
        i = 0
        curr = self.root
        while i < len(prefix):
            if prefix[i] in curr.children:
                curr = curr.children[prefix[i]]
                i += 1
            else:
                return False
        return True
        
        