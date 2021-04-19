from panda3d.core import NodePath

from sky.stars import create_arcade_star_field


stars = NodePath(create_arcade_star_field(num_stars=40000))
spawn_1 = stars.attach_new_node("spawn_player_ship")
spawn_1.set_pos(0, 0, 0)
spawn_2 = stars.attach_new_node("spawn_drone_ship")
spawn_2.set_pos(0, 10, 0)
stars.write_bam_file('star_field.bam')
