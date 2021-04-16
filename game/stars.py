from panda3d.core import LineSegs 

from panda3d.core import Geom
from panda3d.core import GeomNode
from panda3d.core import GeomVertexFormat
from panda3d.core import GeomVertexData
from panda3d.core import GeomTriangles
from panda3d.core import GeomVertexWriter
from panda3d.core import GeomVertexReader
from panda3d.core import GeomVertexArrayFormat

from panda3d.core import Vec2
from panda3d.core import Vec3
from panda3d.core import Vec4


class GridSquareSampler:
    array = GeomVertexArrayFormat()
    array.addColumn('position', 3, Geom.NTFloat32, Geom.CPoint)
    array.addColumn('color', 4, Geom.NTFloat32, Geom.CPoint)

    vformat = GeomVertexFormat()
    vformat.addArray(array)
    vformat = GeomVertexFormat.registerFormat(vformat)
    vdata = GeomVertexData("Data", vformat, Geom.UHDynamic)

    position_writer = GeomVertexWriter(vdata, 'position')
    color_writer = GeomVertexWriter(vdata, 'color')

    geom = Geom(vdata)

    # Vertices
    for layer in range(4):
        for star in range(10000):
            position_writer.addData3f(
                random.gauss(0, 1),
                random.gauss(0, 1),
                layer,
            )
            color_writer.addData4f(
                1./layer,
                1./layer,
                1./layer,
                1,
            )

    # Triangles
    tris = GeomTriangles(Geom.UHStatic)
    for x in range(x_segs):
            tris.addVertices(v_0, v_2, v_3)
    tris.closePrimitive()
    geom.addPrimitive(tris)

    node = GeomNode('geom_node')
    node.addGeom(geom)
    return node
