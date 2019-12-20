class Trie:
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

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pointer = self.tree
        for char in word:
            if char in pointer.son:
                pointer = pointer.son[char]
            else:
                pointer.son[char] = self.Treenode()
                pointer = pointer.son[char]
        pointer.change_flag()


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pointer = self.tree
        for char in word:
            if char in pointer.son:
                pointer = pointer.son[char]
            else:
                return False
        if pointer.end_flag:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pointer = self.tree
        for char in prefix:
            if char in pointer.son:
                pointer = pointer.son[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()

trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))




