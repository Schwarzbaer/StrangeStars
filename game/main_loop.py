from panda3d.core import Point3
from panda3d.core import Vec3
from panda3d.core import CollisionSphere

# from wecs import cefconsole
import wecs
from wecs.core import ProxyType
from wecs.aspects import Aspect
from wecs.aspects import factory
# from wecs.panda3d import debug

from wecs.panda3d.constants import FALLING_MASK
from wecs.panda3d.constants import BUMPING_MASK
from wecs.panda3d.constants import CAMERA_MASK

from stageflow.wecs import WECSStage


ship = Aspect(
    [
        wecs.mechanics.clock.Clock,
        wecs.panda3d.prototype.Model,
        wecs.panda3d.character.CharacterController,
        wecs.panda3d.prototype.Geometry,
        wecs.panda3d.character.WalkingMovement,
        wecs.panda3d.character.InertialMovement,
        wecs.panda3d.character.BumpingMovement,
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
        ),
    },
)


third_person = Aspect(
    [
        wecs.panda3d.camera.Camera,
        wecs.panda3d.camera.ObjectCentricCameraMode,
    ],
    overrides={
        wecs.panda3d.camera.ObjectCentricCameraMode: dict(
            focus_height=0,
            distance=150.0,
            pitch=-90.0,
            min_pitch=-90.0,
            max_pitch=-90.0,
        ),
    },
)


pc_mind = Aspect(
    [
        wecs.panda3d.input.Input,
    ],
    overrides={
        wecs.panda3d.input.Input: dict(
            contexts=[
                'character_movement',
                'camera_movement',
            ],
        ),
    },
)


npc_mind_constant = Aspect(
    [
        wecs.panda3d.ai.BehaviorAI,
        wecs.panda3d.ai.ConstantCharacterAI,
    ],
    overrides={
        wecs.panda3d.ai.ConstantCharacterAI: dict(
            move=Vec3(0, 0.2, 0),
            heading=1.0,
        ),
        wecs.panda3d.ai.BehaviorAI: dict(
            behavior=['constant'],
        ),
    },
)


player = Aspect(
    [
        ship,
        third_person,
        pc_mind,
    ],
)

non_player = Aspect(
    [
        ship,
        npc_mind_constant,
    ],
)


def default_ship_bumper():
    return {
        'bumper': dict(
            shape=CollisionSphere,
            center=Vec3(0.0, 0.0, 1.0),
            radius=0.7,
        ),
    }


ship_arrowhead = {
    wecs.panda3d.prototype.Geometry: dict(
        file='ship_arrowhead.bam',
    ),
    wecs.panda3d.character.BumpingMovement: dict(
        solids=factory(default_ship_bumper),
    ),
}


ship_trident = {
    wecs.panda3d.prototype.Geometry: dict(
        file='ship_trident.bam',
    ),
    wecs.panda3d.character.BumpingMovement: dict(
        solids=factory(default_ship_bumper),
    ),
}


spawn_point_1 = {
    wecs.panda3d.prototype.Model: dict(
        post_attach=lambda: wecs.panda3d.prototype.transform(
            pos=Vec3(0, 0, 0),
        ),
    ),
}


spawn_point_2 = {
    wecs.panda3d.prototype.Model: dict(
        post_attach=lambda: wecs.panda3d.prototype.transform(
            pos=Vec3(0, 10, 0),
        ),
    ),
}


class MainGameStage(WECSStage):
    system_specs = [
        # Set up newly added models/camera, tear down removed ones
        (0, 0, wecs.panda3d.prototype.ManageModels),
        (0, -1, wecs.panda3d.camera.PrepareCameras),
        # Update clocks
        (0, -2, wecs.mechanics.clock.DetermineTimestep),
        # Character AI
        (0, -3, wecs.panda3d.ai.Think),
        # Character controller
        (0, -4, wecs.panda3d.character.UpdateCharacter),
        (0, -5, wecs.panda3d.character.Floating),
        (0, -6, wecs.panda3d.character.Walking),
        (0, -7, wecs.panda3d.character.Inertiing),
        (0, -8, wecs.panda3d.character.Bumping),
        (0, -11, wecs.panda3d.character.TurningBackToCamera),
        (0, -12, wecs.panda3d.character.ExecuteMovement),
        # Camera
        (0, -15, wecs.panda3d.camera.ReorientObjectCentricCamera),
        (0, -16, wecs.panda3d.camera.CollideCamerasWithTerrain),
        # WECS subconsoles
        # wecs.panda3d.cefconsole.UpdateWecsSubconsole,
        # wecs.panda3d.cefconsole.WatchEntitiesInSubconsole,
        # Debug keys (`escape` to close, etc.)
        (0, -17, wecs.panda3d.debug.DebugTools),
    ]

    def setup(self, data):
        """
        Set up the star field and the ship.

        data
            Data passed to this stage will be ignored.
        """
        base.win.set_clear_color((0, 0, 0, 1))
        base.loader.load_model('star_field.bam').reparent_to(base.render)

        player.add(
            base.ecs_world.create_entity(name="Player ship"),
            overrides={**ship_arrowhead, **spawn_point_1},
        )

        non_player.add(
            base.ecs_world.create_entity(name="NPC ship"),
            overrides={**ship_trident, **spawn_point_2},
        )

    def teardown(self, data):
        """
        Tear down the game.

        data
            Data passed to :class:`Stage.exit`, should be None for now.

        :returns:
            None
        """
        return data
