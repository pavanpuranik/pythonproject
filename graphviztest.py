from graphviz import *
import os
os.environ["PATH"] += os.pathsep + 'C:/Users/Pavan Puranik/Downloads/graphviz-2.38/release/bin/'

dot=Digraph(comment="Recursion Visualization")
dot.node('A')
dot.node('B')
dot.node('C')
dot.node('D')
dot.node('E')

dot.edges(['BA', 'BC'])
dot.edges(['AD', 'AE'])


print(dot.source)

dot.render(format='png',view=True)  
