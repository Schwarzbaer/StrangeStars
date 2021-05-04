from dataclasses import field

from panda3d.core import Point3
from panda3d.core import Vec3
from panda3d.core import CollisionSphere

import wecs
from wecs.core import Component
from wecs.aspects import Aspect
from wecs.aspects import factory


@Component()
class FireableWeapons:
    weapons: dict = field(default_factory=dict) # mount -> weapon?


ship = Aspect(
    [
        wecs.mechanics.clock.Clock,
        wecs.panda3d.prototype.Model,
        wecs.panda3d.character.CharacterController,
        wecs.panda3d.prototype.Geometry,
        wecs.panda3d.character.WalkingMovement,
        wecs.panda3d.character.InertialMovement,
        wecs.panda3d.character.FrictionalMovement,
        wecs.panda3d.character.BumpingMovement,
        wecs.panda3d.spawnpoints.SpawnAt,
    ],
    overrides={
        wecs.mechanics.clock.Clock: dict(
            clock=lambda: factory(
                wecs.mechanics.clock.panda3d_clock,
            ),
        ),
        wecs.panda3d.character.WalkingMovement: dict(
            speed=120.0,
            backwards_multiplier=1.0,
            turning_speed=90.0,
        ),
        wecs.panda3d.character.InertialMovement: dict(
            acceleration=30.0,
            rotated_inertia=0.0,
            delta_inputs=True,
        ),
    },
)


def arrowhead_bumper():
    return {
        'bumper': dict(
            shape=CollisionSphere,
            center=Vec3(0.0, 0.0, 0.0),
            radius=1.0,
        ),
    }


ship_arrowhead = {
    wecs.panda3d.prototype.Geometry: dict(
        file='ship_arrowhead.bam',
    ),
    wecs.panda3d.character.BumpingMovement: dict(
        solids=factory(arrowhead_bumper),
    ),
    wecs.panda3d.character.WalkingMovement: dict(
        speed=60.0,
        backwards_multiplier=1.0,
        turning_speed=90.0,
    ),
}


def trident_bumper():
    return {
        'bumper': dict(
            shape=CollisionSphere,
            center=Vec3(0.0, 0.0, 0.0),
            radius=2.0,
        ),
    }


ship_trident = {
    wecs.panda3d.prototype.Geometry: dict(
        file='ship_trident.bam',
    ),
    wecs.panda3d.character.BumpingMovement: dict(
        solids=factory(trident_bumper),
    ),
    wecs.panda3d.character.WalkingMovement: dict(
        speed=30.0,
        backwards_multiplier=1.0,
        turning_speed=90.0,
    ),
}
