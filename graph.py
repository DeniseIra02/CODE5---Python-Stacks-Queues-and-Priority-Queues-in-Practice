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
            name = attrs["xlabel"],
            country = attrs["country"]
            year = int(attrs["year"]) or None,
            latitute = float(attrs["latitude"]),
            longitude = float(attrs["longitude"]),
        )
    
#Test:
#use pygraphviz to read the sample DOT file
#print(nx.nx_agraph.read_dot("roadmap.dot"))

#reading DOT file (nodes)
# graph = nx.nx_agraph.read_dot("roadmap.dot")
# print(graph.nodes["london"])