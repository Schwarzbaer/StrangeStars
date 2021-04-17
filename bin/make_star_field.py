from panda3d.core import NodePath

from sky.stars import create_arcade_star_field


stars = NodePath(create_arcade_star_field(num_stars=40000))
stars.write_bam_file('star_field.bam')
