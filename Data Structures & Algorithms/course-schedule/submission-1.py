class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(set)
        post_map = defaultdict(list)
        sources = []
        for p in prerequisites:
            pre_map[p[0]].add(p[1])
            post_map[p[1]].append(p[0])
        for i in range(numCourses):
            if i not in pre_map:
                sources.append(i)
        
        stack = sources
        visited = set()
        while stack:
            course = stack.pop()
            visited.add(course)
            for p in post_map[course]:
                pre_map[p].remove(course)
                if len(pre_map[p]) == 0:
                    stack.append(p)
        
        return len(visited) == numCourses
         

        