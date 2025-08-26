class Node:
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 1


class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.
    
    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        self.root = None
        if entries:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        self.root = self._insert(self.root, word, meaning)

    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """
        return self._search(self.root, word)

    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        result = []
        self._in_order(self.root, result)
        return result

    # Feel free to implement other helper and private methods

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        return y

    def _insert(self, node, word, meaning):
        if not node:
            return Node(word, meaning)

        if word < node.word:
            node.left = self._insert(node.left, word, meaning)
        elif word > node.word:
            node.right = self._insert(node.right, word, meaning)
        else:
            node.meaning = meaning
            return node

        node.height = max(self._height(node.left), self._height(node.right)) + 1

        balance = self._balance_factor(node)

        if balance > 1:
            if word < node.left.word:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if word > node.right.word:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _search(self, node, word):
        if not node:
            return None
        if word == node.word:
            return node.meaning
        elif word < node.word:
            return self._search(node.left, word)
        else:
            return self._search(node.right, word)

    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append((node.word, node.meaning))
            self._in_order(node.right, result)