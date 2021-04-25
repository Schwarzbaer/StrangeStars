from panda3d.core import Point3
from panda3d.core import Vec3
from panda3d.core import CollisionSphere

import wecs

from stageflow.wecs import WECSStage

from .ontology import third_person
from .ontology import pc_mind
from .ontology import npc_mind_constant
from .ontology import player
from .ontology import non_player
from .stars import game_map
from .ships import ship
from .ships import ship_arrowhead
from .ships import ship_trident


from wecs.core import System, and_filter
from wecs.panda3d.prototype import Model
from wecs.panda3d.input import Input


class FireWeapons(System):
    entity_filters = {
        'ship': and_filter([
            Model,
        ]),
        'input': and_filter([
            Model,
            Input,
        ]),
    }
    input_context = 'weapons'

    def update(self, entities_by_filter):
        for entity in entities_by_filter['input']:
            input = entity[Input]
            if self.input_context in input.contexts:
                context = base.device_listener.read_context(self.input_context)
                self.process_input(entity, context)

    def process_input(self, entity, context):
        if 'primary' in context and context['primary']:
            print("Pew pew!")



class MainGameStage(WECSStage):
    system_specs = [
        # Set up newly added models/camera, tear down removed ones
        (0, 0, wecs.panda3d.prototype.ManageModels),
        (0, -5, wecs.panda3d.spawnpoints.Spawn),
        (0, -10, wecs.panda3d.camera.PrepareCameras),
        # Update clocks
        (0, -20, wecs.mechanics.clock.DetermineTimestep),
        # Character AI
        (0, -30, wecs.panda3d.ai.Think),
        # Character controller
        (0, -40, wecs.panda3d.character.UpdateCharacter),
        (0, -50, wecs.panda3d.character.Floating),
        (0, -60, wecs.panda3d.character.Walking),
        (0, -70, wecs.panda3d.character.Inertiing),
        (0, -80, wecs.panda3d.character.Bumping),
        (0, -110, wecs.panda3d.character.TurningBackToCamera),
        (0, -120, wecs.panda3d.character.ExecuteMovement),
        # Weapons
        (0, -130, FireWeapons),
        # Camera
        (0, -150, wecs.panda3d.camera.ReorientObjectCentricCamera),
        (0, -160, wecs.panda3d.camera.CollideCamerasWithTerrain),
        # WECS subconsoles
        # wecs.panda3d.cefconsole.UpdateWecsSubconsole,
        # wecs.panda3d.cefconsole.WatchEntitiesInSubconsole,
        # Debug keys (`escape` to close, etc.)
        (0, -170, wecs.panda3d.debug.DebugTools),
    ]

    def setup(self, data):
        """
        Set up the star field and the ship.

        data
            Data passed to this stage will be ignored.
        """
        base.win.set_clear_color((0, 0, 0, 1))
        base.loader.load_model('star_field.bam').reparent_to(base.render)

        map_entity = base.ecs_world.create_entity(name="Map")
        game_map.add(map_entity)

        player.add(
            base.ecs_world.create_entity(name="Player ship"),
            overrides={
                wecs.panda3d.spawnpoints.SpawnAt: dict(
                    name='spawn_player_ship',
                ),
                **ship_arrowhead,
            },
        )

        non_player.add(
            base.ecs_world.create_entity(name="NPC ship"),
            overrides={
                wecs.panda3d.spawnpoints.SpawnAt: dict(
                    name='spawn_drone_ship',
                ),
                **ship_trident,
            },
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
