import collections
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = collections.defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, child):
        # Insert the node as before
        self.children[child] = RouteTrieNode(child)

class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler
        # this is the root path or home page node
        self.root = RouteTrieNode(handler=handler)

    def insert(self, path_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for level in path_parts:
            current_node = current_node.children[level]
        current_node.handler = handler

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for level in path_parts:
            if level == '':
                continue
            if level in current_node.children:
                current_node = current_node.children[level]
            else:
                current_node = None
                break
        return current_node
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(root_handler)
        self.not_found = RouteTrie(not_found_handler)

    def add_handler(self, path, name):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.root.insert(path_parts, name)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_parts = self.split_path(path)
        node = self.root.find(path_parts)
        if node:
            if node.handler:
                return node.handler
        return self.not_found.root.handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')[1:]


# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

# some lookups with the expected output
print(router.lookup("/")) # 'root handler'
print(router.lookup("/home")) # 'not found handler'
print(router.lookup("/home/about")) # 'about handler'
print(router.lookup("/home/about/")) # 'about handler'
print(router.lookup("/home/about/me")) # 'not found handler'