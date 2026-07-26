class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        hmap = defaultdict(list)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                p1 = 0
                p2 = 0
                count = 0
                while p1 < len(wordList[i]) and p2 < len(wordList[j]):
                    if wordList[i][p1] != wordList[j][p2]:
                        count += 1
                        if count > 1:
                            break
                    p1 += 1
                    p2 += 1
                if count == 1:
                    hmap[wordList[i]].append(wordList[j])
                    hmap[wordList[j]].append(wordList[i])
        

        q = deque([beginWord])
        level = 1
        size = len(q)
        visited = set()
        found = False
        while q:
            node = q.popleft()
            if node == endWord:
                found = True
                break
            visited.add(node)
            for child in hmap[node]:
                if child not in visited:
                    q.append(child)
            size -= 1
            if size == 0:
                size = len(q)
                level += 1
        
        return level if found else 0



                    
                    


        
        