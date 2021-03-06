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


scale = 30.0 # Length of ship in meters
s = scale / 2.0  # Scale factor on unit ship

node = GeomNode('geom_node')

# Set up the vertex arrays
vformat = GeomVertexFormat.getV3c4()

# Triangle Art
vdata = GeomVertexData("Ship_tri", vformat, Geom.UHDynamic)
geom = Geom(vdata)
col_vertex = GeomVertexWriter(vdata, 'vertex')
col_color = GeomVertexWriter(vdata, 'color')

col_vertex.addData3f(Vec3( 0 * s,  2 * s, 0.5))
col_vertex.addData3f(Vec3( 2 * s, -2 * s, 0.5))
col_vertex.addData3f(Vec3( 1 * s, -1 * s, 0.5))
col_vertex.addData3f(Vec3( 0 * s, -2 * s, 0.5))
col_vertex.addData3f(Vec3(-1 * s, -1 * s, 0.5))
col_vertex.addData3f(Vec3(-2 * s, -2 * s, 0.5))
col_color.addData4f(Vec4(0, 0, 0, 1))
col_color.addData4f(Vec4(0, 0, 0, 1))
col_color.addData4f(Vec4(0, 0, 0, 1))
col_color.addData4f(Vec4(0, 0, 0, 1))
col_color.addData4f(Vec4(0, 0, 0, 1))
col_color.addData4f(Vec4(0, 0, 0, 1))

tri = GeomTriangles(Geom.UHStatic)

tri.add_vertices(0, 2, 1)
tri.add_vertices(0, 3, 2)
tri.add_vertices(0, 4, 3)
tri.add_vertices(0, 5, 4)
tri.closePrimitive()

geom.addPrimitive(tri)

node.addGeom(geom)

# Line art
vdata = GeomVertexData("Ship_line", vformat, Geom.UHDynamic)
geom = Geom(vdata)
col_vertex = GeomVertexWriter(vdata, 'vertex')
col_color = GeomVertexWriter(vdata, 'color')

col_vertex.addData3f(Vec3( 0 * s,  2 * s, 1))
col_vertex.addData3f(Vec3( 2 * s, -2 * s, 1))
col_vertex.addData3f(Vec3( 1 * s, -1 * s, 1))
col_vertex.addData3f(Vec3( 0 * s, -2 * s, 1))
col_vertex.addData3f(Vec3(-1 * s, -1 * s, 1))
col_vertex.addData3f(Vec3(-2 * s, -2 * s, 1))
col_color.addData4f(Vec4(1, 1, 1, 1))
col_color.addData4f(Vec4(1, 1, 1, 1))
col_color.addData4f(Vec4(1, 1, 1, 1))
col_color.addData4f(Vec4(1, 1, 1, 1))
col_color.addData4f(Vec4(1, 1, 1, 1))
col_color.addData4f(Vec4(1, 1, 1, 1))

line = GeomLines(Geom.UHStatic)

line.add_vertices(0, 1)
line.add_vertices(1, 2)
line.add_vertices(2, 3)
line.add_vertices(3, 4)
line.add_vertices(4, 5)
line.add_vertices(5, 0)
line.closePrimitive()

geom.addPrimitive(line)

node.addGeom(geom)


# Write
nodepath = NodePath(node)
nodepath.write_bam_file('ship_trident.bam')
