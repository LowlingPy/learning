# Mahdi Mohammadi kha 982011056
# in graph vazn dare ghablesh bedone dar nazar gereftane vazn ferestadam ino badesh ezafe kardam

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def delete_node(self, node):
        self.nodes.remove(node)

    def get_nodes(self):
        for node in self.nodes:
            node_neighbors = []
            for i in node.neighbors:
                node_neighbors.append(str(i['node'].value) + ':' + str(i['weight']))
            print(str(node.value) + ' ---> ' + str(node_neighbors))


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node, weight=1):
        self.neighbors.append(dict(node=node, weight=weight))
        node.neighbors.append(dict(node=self, weight=weight))

    def delete_node(self, node, weight):
        self.neighbors.remove(dict(node=node, weight=weight))


graph = Graph()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.add_neighbor(node2, 4)
node2.add_neighbor(node3, 3)
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)

graph.get_nodes()