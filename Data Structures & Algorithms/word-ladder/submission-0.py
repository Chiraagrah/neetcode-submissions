class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        dic = defaultdict(list)
        word_graph = defaultdict(list)
        for word in wordList:
            for x in range(0,len(word)):
                newword = word[:x] + '*' + word[x+1:]
                for neighbour in dic[newword]:
                    word_graph[neighbour].append(word)
                    word_graph[word].append(neighbour)
                dic[newword].append(word)
        level = 1
        queue = deque([beginWord])
        visited = {beginWord}
        while queue:
            start = len(queue)
            for _ in range(start):
                curWord = queue.popleft()
                print(curWord)
                if curWord == endWord:
                    return level
                for neighbour in word_graph[curWord]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            level += 1
        return 0