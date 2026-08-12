class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        heap = [-x for x in cnt.values()]
        heapq.heapify(heap)
        time = 0
        queue = deque([])
        while queue or heap:
            time+=1
            if heap:
                item = heapq.heappop(heap)
                item +=1
                if item<0:
                    queue.append([item,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(heap,queue.popleft()[0])
        return time