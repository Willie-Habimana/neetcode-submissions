class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        prereq_map = defaultdict(int)
        sources = []
        for pre in prerequisites:
            prereq_map[pre[0]] += 1
            course_map[pre[1]].append(pre[0])
        for i in range(numCourses):
            if i not in prereq_map:
                sources.append(i)
        
        q = deque(sources)
        visited = set()
        while q:
            course = q.popleft()
            visited.add(course)
            if course in course_map:
                for next_course in course_map[course]:
                    prereq_map[next_course] -= 1
                    if prereq_map[next_course] == 0:
                        q.append(next_course)
        
        return len(visited) == numCourses

            


         

        