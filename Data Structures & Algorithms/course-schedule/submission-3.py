class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = defaultdict(int)
        preMap = defaultdict(list)

        for crs , pre in prerequisites:
            
            inDegree[crs]+=1
            preMap[pre].append(crs)

        queue = deque()
        completed = 0

        for crs in range(numCourses):
            if inDegree[crs] == 0:
                queue.append(crs)
        
        while queue:
            crs = queue.popleft()
            completed += 1
            for pcrs in preMap[crs]:
                inDegree[pcrs] -= 1
                if inDegree[pcrs] == 0:
                    queue.append(pcrs)

        return completed == numCourses