class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        route = []

        def dfs(src: str):
            while adj[src]:
                next_dest = adj[src].pop()
                dfs(next_dest)
            route.append(src)

        dfs("JFK")
        return route[::-1]