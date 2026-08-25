class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = defaultdict(int)
        preMap = defaultdict(list)

        for crs , pre in prerequisites:
            
            inDegree[crs]+=1
            preMap[pre].append(crs)

        queue = deque()
        completed = set()

        for crs in range(numCourses):
            if inDegree[crs] == 0:
                queue.append(crs)
                completed.add(crs)
        
        while queue:
            crs = queue.popleft()
            
            for pcrs in preMap[crs]:
                inDegree[pcrs] -= 1
                if inDegree[pcrs] == 0 and pcrs not in completed:
                    queue.append(pcrs)
                    completed.add(pcrs)

        return len(completed) == numCourses