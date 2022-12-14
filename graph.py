import networkx as nx

from typing import NamedTuple

#directory path for graphviz
import os
os.add_dll_directory("C:/Program Files/Graphviz/bin")

class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )

def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )
        
#Test:

#use pygraphviz to read the sample DOT file
#print(nx.nx_agraph.read_dot("roadmap.dot"))

#reading DOT file (nodes)
# graph = nx.nx_agraph.read_dot("roadmap.dot")
# print(graph.nodes["london"])

#to identify the graph and node
# nodes, graph = load_graph("roadmap.dot", City.from_dict)
# print(nodes["london"])
# print(graph)

#to identify the neighbors of a given city 
# nodes, graph = load_graph("roadmap.dot", City.from_dict)
# for neighbor in graph.neighbors(nodes["london"]):
#     print(neighbor.name)

#to identify the neighbors with weights of the connecting edges
# nodes, graph = load_graph("roadmap.dot", City.from_dict)
# for neighbor, weights in graph[nodes["london"]].items():
#     print(weights["distance"], neighbor.name)

#sorting the weights of the neighbors in accending order
# nodes, graph = load_graph("roadmap.dot", City.from_dict)
# def sort_by(neighbors, strategy):
#     return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

# def by_distance(weights):
#     return float(weights["distance"])

# for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
#     print(f"{weights['distance']:>3} miles, {neighbor.name}")

#Breadth-First Search Using a FIFO Queue
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)

for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not Found")