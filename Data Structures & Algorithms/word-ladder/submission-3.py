class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Make a dict that stores patterns that can be made from each word(Ex. {*at: [bat, cat]})
        # Add begin word to a deque. Pop each word & look for neighbors.

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        nei = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        # wordList.append(beginWord)
        q = collections.deque()
        q.append(beginWord)

        visited = set()
        visited.add(beginWord)

        steps = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

            steps += 1

        return 0