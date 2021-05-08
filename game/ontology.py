from panda3d.core import Vec3

import wecs
from wecs.aspects import Aspect

from .ships import ship


third_person = Aspect(
    [
        wecs.panda3d.camera.Camera,
        wecs.panda3d.camera.ObjectCentricCameraMode,
    ],
    overrides={
        wecs.panda3d.camera.ObjectCentricCameraMode: dict(
            focus_height=0,
            distance=250.0*7.5,
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
                'weapons',
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
            move=Vec3(0, 0.05, 0),
            heading=0.3,
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
