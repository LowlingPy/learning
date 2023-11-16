# Mahdi Mohammadi kha 982011056

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def delete_node(self, node):
        self.nodes.remove(node)

    def get_nodes(self):
        for node in self.nodes:
            print(str(node.value) + ' ---> ' + str([i.value for i in node.neighbors]))


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)
        node.neighbors.append(self)
    def delete_node(self, node):
        self.neighbors.remove(node)


graph = Graph()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.add_neighbor(node2)
node2.add_neighbor(node3)
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)

graph.get_nodes()