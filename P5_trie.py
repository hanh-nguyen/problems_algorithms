## Represents a single node in the Trie
import collections
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        results = []
        for child in self.children:
            suffix_child = suffix + child
            if self.children[child].is_word: 
                results.append(suffix_child)
            sub_results = self.children[child].suffixes(suffix_child)
            results += sub_results
        return results


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            current_node = current_node.children[char]
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

node = MyTrie.find('ant')
results = node.suffixes()
print(results) 
# ['hology', 'agonist', 'onym']

node = MyTrie.find('f')
results = node.suffixes()
print(results) 
# ['un', 'unction', 'actory']

node = MyTrie.find('tr')
results = node.suffixes()
print(results) 
# ['ie', 'igger', 'igonometry', 'ipod']
