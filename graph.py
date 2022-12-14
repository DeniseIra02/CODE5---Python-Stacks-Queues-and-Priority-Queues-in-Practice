import networkx as nx

from collections import deque
from math import inf as infinity
from typing import NamedTuple

from queues import MutableMinHeap, Queue, Stack


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


def breadth_first_traverse(graph, source, order_by=None):
    queue = Queue(source)
    visited = {source}
    while queue:
        yield (node := queue.dequeue())
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

def breadth_first_search(graph, source, predicate, order_by=None):
    return search(breadth_first_traverse, graph, source, predicate, order_by)

def shortest_path(graph, source, destination, order_by=None):
    queue = Queue(source)
    visited = {source}
    previous = {}
    while queue:
        node = queue.dequeue()
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                previous[neighbor] = node
                if neighbor == destination:
                    return retrace(previous, source, destination)

def retrace(previous, source, destination):
    path = deque()

    current = destination
    while current != source:
        path.appendleft(current)
        current = previous.get(current)
        if current is None:
            return None

    path.appendleft(source)
    return list(path)

def connected(graph, source, destination):
    return shortest_path(graph, source, destination) is not None

def depth_first_traverse(graph, source, order_by=None):
    stack = Stack(source)
    visited = set()
    while stack:
        if (node := stack.dequeue()) not in visited:
            yield node
            visited.add(node)
            neighbors = list(graph.neighbors(node))
            if order_by:
                neighbors.sort(key=order_by)
            for neighbor in reversed(neighbors):
                stack.enqueue(neighbor)

def recursive_depth_first_traverse(graph, source, order_by=None):
    visited = set()

    def visit(node):
        yield node
        visited.add(node)
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                yield from visit(neighbor)

    return visit(source)

def depth_first_search(graph, source, predicate, order_by=None):
    return search(depth_first_traverse, graph, source, predicate, order_by)

def search(traverse, graph, source, predicate, order_by=None):
    for node in traverse(graph, source, order_by):
        if predicate(node):
            return node

def dijkstra_shortest_path(graph, source, destination, weight_factory):
    previous = {}
    visited = set()

    unvisited = MutableMinHeap()
    for node in graph.nodes:
        unvisited[node] = infinity
    unvisited[source] = 0

    while unvisited:
        visited.add(node := unvisited.dequeue())
        for neighbor, weights in graph[node].items():
            if neighbor not in visited:
                weight = weight_factory(weights)
                new_distance = unvisited[node] + weight
                if new_distance < unvisited[neighbor]:
                    unvisited[neighbor] = new_distance
                    previous[neighbor] = node

    return retrace(previous, source, destination)


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
# def is_twentieth_century(year):
#     return year and 1901 <= year <= 2000

# nodes, graph = load_graph("roadmap.dot", City.from_dict)

# for node in nx.bfs_tree(graph, nodes["edinburgh"]):
#     print("📍", node.name)
#     if is_twentieth_century(node.year):
#         print("Found:", node.name, node.year)
#         break
# else:
#     print("Not Found")

#sort the neighbors according to some criteria(latitude)
# def is_twentieth_century(year):
#     return year and 1901 <= year <= 2000

# nodes, graph = load_graph("roadmap.dot", City.from_dict)

# def order(neighbors):
#     def by_latitude(city):
#         return city.latitude
#     return iter(sorted(neighbors, key=by_latitude, reverse=True))

# for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
#     print("📍", node.name)
#     if is_twentieth_century(node.year):
#         print("Found:", node.name, node.year)
#         break
# else:
#     print("Not Found")

#test breadth-first transversal and search implementation
# from graph import (
#     City,
#     load_graph,
#     breadth_first_traverse,
#     breadth_first_search as bfs,
# )

# def is_twentieth_century(city):
#     return city.year and 1901 <= city.year <= 2000

# nodes, graph = load_graph("roadmap.dot", City.from_dict)

# city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
# print(city.name)

# for city in breadth_first_traverse(graph, nodes["edinburgh"]):
#     print(city.name)

#Shortest Path Using Breadth-First Traversal
# nodes, graph = load_graph("roadmap.dot", City.from_dict)

# city1 = nodes["aberdeen"]
# city2 = nodes["perth"]

# for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
#     print(f"{i}.", " → ".join(city.name for city in path))

# #Natural Order of Neighbors
# nodes, graph = load_graph("roadmap.dot", City.from_dict)

# city1 = nodes["aberdeen"]
# city2 = nodes["perth"]

# print(" → ".join(city.name for city in shortest_path(graph, city1, city2)))

# def by_latitude(city):
#     return -city.latitude

# print(" → ".join(
#     city.name
#     for city in shortest_path(graph, city1, city2, by_latitude)
# ))

#Connected or not
# nodes, graph = load_graph("roadmap.dot", City.from_dict)

# print(connected(graph, nodes["belfast"], nodes["glasgow"]))
# print(connected(graph, nodes["belfast"], nodes["derry"]))

#Depth-First Search using a LIFO Queue
# def is_twentieth_century(year):
#     return year and 1901 <= year <= 2000

# nodes, graph = load_graph("roadmap.dot", City.from_dict)
# for node in nx.dfs_tree(graph, nodes["edinburgh"]):
#     print("📍", node.name)
#     if is_twentieth_century(node.year):
#         print("Found:", node.name, node.year)
#         break

# else:
#     print("Not Found")

# breadth_first_search and depth_first_search
# from graph import (
#     City,
#     load_graph,
#     depth_first_traverse,
#     depth_first_search as dfs,
# )

# def is_twentieth_century(city):
#     return city.year and 1901 <= city.year <= 2000

# nodes, graph = load_graph("roadmap.dot", City.from_dict)

# city = dfs(graph, nodes["edinburgh"], is_twentieth_century)

# print(city.name)
    
# for city in depth_first_traverse(graph, nodes["edinburgh"]):
#     print(city.name)
