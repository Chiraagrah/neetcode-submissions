class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        head = self.root
        for char in word:
            if char not in head.children:
                head.children[char] = TrieNode()
            head = head.children[char]
        head.end = True

    
    def search(self, word: str) -> bool:

        def dfs(node: TrieNode(),index):
            if index == len(word):
                return node.end

            elif word[index] != '.' and (word[index] not in node.children):
                return False

            elif word[index]=='.':
                for value in node.children.values():
                    if dfs(value,index+1):
                        return True
                return False
            else:
                return dfs(node.children[word[index]],index+1)
        return dfs(self.root,0)

            
