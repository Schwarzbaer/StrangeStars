import random

from panda3d.core import NodePath
from panda3d.core import AntialiasAttrib
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


def create_arcade_star_field(num_stars=10000, layers=4, layer_exp=0.8,
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
            x = rng.gauss(0, 2000 * 7.5)
            y = rng.gauss(0, 2000 * 7.5)
            z = ((2 ** layer) - 0) * -250
            # z = ((2 ** layer) - 1) * -500
            v = Vec3(x, y, z)
            col_vertex.addData3f(v)

    # Write vertex data for color
    rng = random.Random(seed)
    for layer in range(layers):
        for idx in range(0, num_stars):
            l = 0.8 * (1 - layer / layers)
            # l = 0.8 / ((layer + 1.) ** layer_exp)
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


def create_line_grid(seed=0, size=200, hlines=2):
    # The grid spans the area from -1 to 1, with `lines` indicating the
    # number of lines on either side of 0. It then gets scaled up to its
    # size.
    line_distance = 1.0 / hlines
    line_offset = line_distance / 2.0
    
    # Set up the vertex arrays
    vformat = GeomVertexFormat.getV3c4()
    vdata = GeomVertexData("Gridlines", vformat, Geom.UHDynamic)
    col_vertex = GeomVertexWriter(vdata, 'vertex')
    col_color = GeomVertexWriter(vdata, 'color')
    geom = Geom(vdata)

    # Write vertex data for positions
    for idx in range(hlines * 2):
        x = -size
        y = (-1 + line_offset + line_distance * idx) * size
        z = 0
        v = Vec3(x, y, z)
        col_vertex.addData3f(v)
    for idx in range(hlines * 2):
        x = size
        y = (-1 + line_offset + line_distance * idx) * size
        z = 0
        v = Vec3(x, y, z)
        col_vertex.addData3f(v)
    for idx in range(hlines * 2):
        x = (-1 + line_offset + line_distance * idx) * size
        y = -size
        z = 0
        v = Vec3(x, y, z)
        col_vertex.addData3f(v)
    for idx in range(hlines * 2):
        x = (-1 + line_offset + line_distance * idx) * size
        y = size
        z = 0
        v = Vec3(x, y, z)
        col_vertex.addData3f(v)

    # Write vertex data for color
    for idx in range(hlines * 8):
        c = VBase4(0, 0, 0.5, 1)
        col_color.addData4f(c)

    # Make a point for each star
    lines = GeomLines(Geom.UHStatic)
    for idx in range(hlines * 2):
        lines.add_vertex(idx)
        lines.add_vertex(idx + hlines * 2)
        lines.add_vertex(idx + hlines * 4)
        lines.add_vertex(idx + hlines * 6)
    lines.closePrimitive()
    geom.addPrimitive(lines)

    # Create the actual node
    node = GeomNode('geom_node')
    node.addGeom(geom)
    return node


if __name__ == '__main__':
    level = NodePath("Level geometry")

    stars = level.attach_new_node(
        create_arcade_star_field(num_stars=40000),
    )
    stars.set_antialias(AntialiasAttrib.MPoint)

    grid = level.attach_new_node(
        create_line_grid(size=100000, hlines=400),
    )
    stars.set_antialias(AntialiasAttrib.MLine)

    spawn_1 = level.attach_new_node("spawn_player_ship")
    spawn_1.set_pos(0, 0, 0)
    spawn_2 = level.attach_new_node("spawn_drone_ship")
    spawn_2.set_pos(0, 50, 0)
    level.write_bam_file('star_field.bam')
else:
    print("What are you doing? This is meant to be a standalone program.")
