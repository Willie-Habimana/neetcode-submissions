class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        sources = []

        for i in range(numCourses):
            if indegree[i] == 0:
                sources.append(i)
        
        stack = sources
        visited = set()
        ans = []
        while stack:
            course = stack.pop()
            ans.append(course)
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    stack.append(next_course)
        
        return ans if len(ans) == numCourses else []
                
            

