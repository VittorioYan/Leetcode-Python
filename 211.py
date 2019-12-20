class WordDictionary:
    class Treenode:
        def __init__(self):
            self.son = {}
            self.end_flag = False

        def change_flag(self):
            self.end_flag = True

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = self.Treenode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        pointer = self.tree
        for char in word:
            if char in pointer.son:
                pointer = pointer.son[char]
            else:
                pointer.son[char] = self.Treenode()
                pointer = pointer.son[char]
        pointer.change_flag()

    def _search(self, cur_word: str, cur_tree: Treenode) -> bool:
        pointer = cur_tree
        for i in range(len(cur_word)):
            if cur_word[i] in pointer.son:
                pointer = pointer.son[cur_word[i]]
            elif cur_word[i] == '.':
                for son in pointer.son:
                    if self._search(cur_word[i+1:], pointer.son[son]):
                        return True
                return False
            else:
                return False
        return pointer.end_flag

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(word, self.tree)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("pad")
obj.addWord("mad")
print(obj.search("..d"))
print(obj.search("pa.a"))
print(obj.search("aa"))
print(obj.search(".a"))
print(obj.search("a."))
