class TreeNode:

    def __init__(self, char = None):
        self.char = char
        self.children = {}
        self.EOW = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode(c)
            curr = curr.children[c]
        curr.EOW = True
        

    def search(self, word: str) -> bool:
        #print(word)
        return self.search_helper(self.root, word)

        
    
    def search_helper(self, node, word):
        curr = node
        for i in range(len(word)):
            if word[i] == ".":
                for child_node in curr.children.values():
                    #print(child_node.char)
                    if self.search_helper(child_node, word[i+1:]):
                        return True
                return False
            elif word[i] not in curr.children:
                return False
            else:
                #print(word[i])
                curr = curr.children[word[i]]

        #print(curr.EOW)
        return curr.EOW

