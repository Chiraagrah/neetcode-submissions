from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Precompute pattern map: pattern -> list of words
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                patterns[word[:i] + '*' + word[i+1:]].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps
            
            # Query patterns directly during BFS
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                for neighbor in patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
                # Clear visited patterns to avoid re-checking identical buckets
                patterns[pattern] = []
                
        return 0