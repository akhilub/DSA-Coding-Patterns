# Algorithm

"""
Using a basic Trie (pronounced as “try”), which is a type of search tree used to efficiently store a dynamic set or associative array where the keys are usually strings. Tries are well-suited for solving problems related to word searches, auto-completions, and prefix matching.
"""

"""
`TrieNode` Class:
Purpose: Represents a single node in the Trie.
`child` Attribute: Uses a defaultdict from the collections module to automatically create a new TrieNode when accessing a missing key. This eliminates the need for explicit checks if a child node exists, streamlining node creation during word insertion.
`is_word` Attribute: A boolean flag indicating whether the node marks the end of a word in the Trie. It is initialized as `False` and set to `True` when a word is fully inserted.

"""

"""
`Trie` Class:
Initialization: The `Trie` constructor initializes the Trie with a root `TrieNode`.

`insert` Method: Inserts a word into the Trie.

 - Iterates through each letter in the word.
 - For each letter, it moves down to the corresponding child node, creating new nodes as necessary due to the use of `defaultdict`.
 - After all letters are inserted, sets the `is_word` flag of the last node to `True` to mark the end of a word.
 
`search` Method: Searches for a word in the Trie.
- Iterates through each letter in the word, navigating through the child nodes.
- If a letter does not exist as a key in the current node’s children (i.e., `cur.child.get(letter)` returns `None`), returns `False` immediately.
- If all letters are found in sequence, checks the is_word flag of the last node. Returns `True` if it’s set (meaning the word exists in the Trie), otherwise `False`.

`startsWith` Method: Checks if there is any word in the Trie that starts with the given prefix.
- Similar to `search`, but returns `True` as soon as all letters of the prefix are found in sequence, without checking the `is_word` flag. This is because the presence of the prefix nodes alone is sufficient to confirm that at least one word with that prefix exists in the Trie.
"""

"""
Usage and Functionality:
This Trie implementation allows for efficient insertion and search operations for words and prefixes. The `defaultdict` significantly simplifies the code by automatically handling missing children. This Trie can be used in various applications such as implementing an autocomplete feature, spell checker, or for efficiently solving word search puzzles.

Note: The comment in the `search` and `startsWith` methods about `cur = cur.child[letter]` potentially creating a default node is crucial. Using `cur.child.get(letter)` instead avoids unintended Trie modifications during search operations, ensuring that the Trie structure only changes during explicit insertions.
"""

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            cur = cur.child[letter]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            # cur = cur.child[letter] ==> will not work, it will create a default node for this letter
            cur = cur.child.get(letter)
            if not cur:
                return False
        return True

    def startWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in word:
            # cur = cur.child[letter] ==> will not work, it will create a default node for this letter
            cur = cur.child.get(letter)
            if not cur:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


"""
Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary.
The defaultdict in contrast will simply create any items that you try to access

https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
"""
