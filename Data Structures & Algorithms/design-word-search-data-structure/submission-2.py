class Node:

    def __init__(self, char: str = None):
        self.char = char
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node()
        # self.level = defaultdict(list)
        

    def addWord(self, word: str) -> None:
        i = 0
        curr = self.root 
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        while i < len(word):
            new_node = Node(word[i])
            curr.children[word[i]] = new_node
            curr = new_node
            # self.level[i].append(new_node)
            i += 1
        
        curr.children["EOW"] = Node()
        

    def search(self, word: str) -> bool:
        def dfs(root, i):
            curr = root
            while i < len(word) and (word[i] == '.' or word[i] in curr.children):
                if word[i] == '.':
                    for node in curr.children.values():
                        if dfs(node, i+1):
                            return True
                    return False
                else:
                    curr = curr.children[word[i]]
                    i += 1
            return True if i == len(word) and "EOW" in curr.children else False
        
        return dfs(self.root, 0)