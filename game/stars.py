import wecs
from wecs.aspects import Aspect


game_map = Aspect(
    [
        wecs.panda3d.prototype.Model,
        wecs.panda3d.prototype.Geometry,
        wecs.panda3d.spawnpoints.SpawnMap,
    ],
    overrides={
        wecs.panda3d.prototype.Geometry: dict(
            file='star_field.bam',
        ),
    },
)
