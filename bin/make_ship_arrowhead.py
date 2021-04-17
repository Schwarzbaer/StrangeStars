from panda3d.core import NodePath

from panda3d.core import GeomVertexWriter
from panda3d.core import GeomVertexFormat
from panda3d.core import GeomVertexData
from panda3d.core import Geom
from panda3d.core import Vec3
from panda3d.core import Vec4
from panda3d.core import GeomPoints
from panda3d.core import GeomLines
from panda3d.core import GeomTriangles
from panda3d.core import GeomNode


# Set up the vertex arrays
vformat = GeomVertexFormat.getV3c4()
vdata = GeomVertexData("Stars", vformat, Geom.UHDynamic)
col_vertex = GeomVertexWriter(vdata, 'vertex')
col_color = GeomVertexWriter(vdata, 'color')
geom = Geom(vdata)

# Write vertex data

# White vertices
col_vertex.addData3f(Vec3(0, 1, 0))
col_color.addData4f(Vec4(1, 1, 1, 1))

col_vertex.addData3f(Vec3(1, -1, 0))
col_color.addData4f(Vec4(1, 1, 1, 1))

col_vertex.addData3f(Vec3(0, -0.5, 0))
col_color.addData4f(Vec4(1, 1, 1, 1))

col_vertex.addData3f(Vec3(-1, -1, 0))
col_color.addData4f(Vec4(1, 1, 1, 1))

# Colored vertices
col_vertex.addData3f(Vec3(0, 1, 0))
col_color.addData4f(Vec4(1, 0, 0, 1))

col_vertex.addData3f(Vec3(1, -1, 0))
col_color.addData4f(Vec4(0, 1, 0, 1))

col_vertex.addData3f(Vec3(0, -0.5, 0))
col_color.addData4f(Vec4(0, 0.5, 0.5, 1))

col_vertex.addData3f(Vec3(-1, -1, 0))
col_color.addData4f(Vec4(0, 0, 1, 1))

# Make a point for each star
# point = GeomPoints(Geom.UHStatic)
# 
# point.add_vertex(i)
# point.closePrimitive()
# geom.addPrimitive(point)

line = GeomLines(Geom.UHStatic)

line.add_vertices(0, 1)
line.add_vertices(1, 2)
line.add_vertices(2, 3)
line.add_vertices(3, 0)
line.closePrimitive()

geom.addPrimitive(line)

# tri = GeomTriangles(Geom.UHStatic)
# tri.add_vertices(0, 1, 2)
# tri.add_vertices(0, 3, 2)
# tri.closePrimitive()
# 
# geom.addPrimitive(tri)


# Create the actual node
node = GeomNode('geom_node')
node.addGeom(geom)

# Write
nodepath = NodePath(node)
nodepath.write_bam_file('ship_arrowhead.bam')
