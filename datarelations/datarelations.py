#%%
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import StringIO
from IPython.display import SVG
import pydot

dot_graph = pydot.Dot(graph_type='digraph')

amp_node = pydot.Node(' Asphalt mixing plant (1) ')
amp_node.set_shape('box3d')
dot_graph.add_node(amp_node)

mdl_node = pydot.Node(' Material delivery logistics (2) ')
mdl_node.set_shape('box3d')
dot_graph.add_node(mdl_node)

ap_node = pydot.Node(' Asphalt paving (3) ')
ap_node.set_shape('box3d')
dot_graph.add_node(ap_node)

cmp_node = pydot.Node(' Compaction (4) ')
cmp_node.set_shape('box3d')
dot_graph.add_node(cmp_node)



mqa_node = pydot.Node('Material quality\nanalysis')
mqa_node.set_shape('triangle')
dot_graph.add_node(mqa_node)

irg_node = pydot.Node(' Road Geometry ')
#riq_node.set_shape('box3d')
dot_graph.add_node(irg_node)

la_node = pydot.Node('Logistics\nanalysis')
la_node.set_shape('triangle')
dot_graph.add_node(la_node)


iedge = pydot.Edge(ap_node,irg_node)
iedge.set_label(' Geometric\ninference')
dot_graph.add_edge(iedge)

iedge = pydot.Edge(amp_node,mdl_node)
iedge.set_penwidth(1)
iedge.set_label('Interdependency (A)')
iedge.set_style('dashed')
dot_graph.add_edge(iedge)
iedge = pydot.Edge(mdl_node,amp_node)
iedge.set_penwidth(1)
# iedge.set_label('(A)')
iedge.set_style('dashed')
dot_graph.add_edge(iedge)

iedge = pydot.Edge(mdl_node,ap_node)
iedge.set_penwidth(1)
iedge.set_label('(A)')
iedge.set_style('dashed')
dot_graph.add_edge(iedge)
iedge = pydot.Edge(ap_node,mdl_node)
iedge.set_penwidth(1)
# iedge.set_label('(A)')
iedge.set_style('dashed')
dot_graph.add_edge(iedge)

iedge = pydot.Edge(cmp_node,ap_node)
iedge.set_penwidth(1)
# iedge.set_label('(A)')
iedge.set_style('dashed')
dot_graph.add_edge(iedge)
iedge = pydot.Edge(ap_node,cmp_node)
iedge.set_penwidth(1)
iedge.set_label('(A)')
iedge.set_style('dashed')
dot_graph.add_edge(iedge)


iedge = pydot.Edge(amp_node,mqa_node)
iedge.set_penwidth(1)
iedge.set_label(' Direct influence (B)')
dot_graph.add_edge(iedge)

iedge = pydot.Edge(ap_node,mqa_node)
iedge.set_penwidth(1)
# iedge.set_label('(B)')
dot_graph.add_edge(iedge)

iedge = pydot.Edge(cmp_node,mqa_node)
iedge.set_penwidth(1)
iedge.set_label('  (B)')
dot_graph.add_edge(iedge)

iedge = pydot.Edge(mdl_node,la_node)
iedge.set_penwidth(1)
# iedge.set_label('(B)')
dot_graph.add_edge(iedge)

iedge = pydot.Edge(ap_node,la_node)
iedge.set_penwidth(1)
iedge.set_label('      (B)')
dot_graph.add_edge(iedge)

dot_graph.write_png('figure6_asphalt_components.png')


# %%
