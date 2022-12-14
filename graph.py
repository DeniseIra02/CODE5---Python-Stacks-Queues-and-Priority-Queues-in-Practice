import networkx as nx
#directory path for graphviz
import os
os.add_dll_directory("C:/Program Files/Graphviz/bin")

#Test:
#use pygraphviz to read the sample DOT file
#print(nx.nx_agraph.read_dot("roadmap.dot"))

#reading DOT file
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])