import random

from panda3d.core import NodePath
from panda3d.core import GeomVertexFormat
from panda3d.core import GeomVertexData
from panda3d.core import GeomVertexWriter
from panda3d.core import Geom
from panda3d.core import GeomNode
from panda3d.core import GeomPoints
from panda3d.core import GeomLines
from panda3d.core import GeomTriangles
from panda3d.core import Vec3
from panda3d.core import VBase4


def create_arcade_star_field(num_stars=10000, layers=4, layer_exp=1.2,
                             seed=0):
    # Set up the vertex arrays
    vformat = GeomVertexFormat.getV3c4()
    vdata = GeomVertexData("Stars", vformat, Geom.UHDynamic)
    col_vertex = GeomVertexWriter(vdata, 'vertex')
    col_color = GeomVertexWriter(vdata, 'color')
    geom = Geom(vdata)

    # Write vertex data for positions
    rng = random.Random(seed)
    for layer in range(layers):
        for idx in range(0, num_stars):
            x = rng.gauss(0, 2000)
            y = rng.gauss(0, 2000)
            z = ((2 ** layer) - 1) * -500
            v = Vec3(x, y, z)
            col_vertex.addData3f(v)

    # Write vertex data for color
    rng = random.Random(seed)
    for layer in range(layers):
        for idx in range(0, num_stars):
            l = 0.8 / ((layer + 1.) ** layer_exp)
            c = VBase4(l, l, l, 1)
            col_color.addData4f(c)

    # Make a point for each star
    point = GeomPoints(Geom.UHStatic)
    for idx in range(0, num_stars * layers):
        point.add_vertex(idx)
    point.closePrimitive()
    geom.addPrimitive(point)

    # Create the actual node
    node = GeomNode('geom_node')
    node.addGeom(geom)
    return node


stars = NodePath(create_arcade_star_field(num_stars=40000))
spawn_1 = stars.attach_new_node("spawn_player_ship")
spawn_1.set_pos(0, 0, 0)
spawn_2 = stars.attach_new_node("spawn_drone_ship")
spawn_2.set_pos(0, 10, 0)
stars.write_bam_file('star_field.bam')
