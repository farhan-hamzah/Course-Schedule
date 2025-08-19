from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Bangun graph adjacency list + in-degree
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # Queue untuk node dengan indegree = 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return visited == numCourses
