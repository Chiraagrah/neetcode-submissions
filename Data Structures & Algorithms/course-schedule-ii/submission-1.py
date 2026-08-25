class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        inDegree = defaultdict(int)
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            inDegree[crs] += 1
            preMap[pre].append(crs)
        queue = deque()
        for crs in range(numCourses):
            if inDegree[crs] == 0:
                result.append(crs)
                queue.append(crs)

        completed = len(queue)
        if completed == 0:
            return []

        while queue:
            current_crs = queue.popleft()
            for crs in preMap[current_crs]:
                inDegree[crs] -= 1
                if inDegree[crs] == 0:
                    queue.append(crs)
                    completed += 1
                    result.append(crs)

        return result if completed== numCourses else []