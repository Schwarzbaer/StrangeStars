from direct.gui.DirectGui import DirectButton

from panda3d_logos.splashes import Colors
from panda3d_logos.splashes import Pattern

from stageflow import Flow
from stageflow import Stage
from stageflow.prefab import Quit
from stageflow.panda3d import Panda3DSplash

from .main_loop import MainGameStage


base.flow = Flow(
    stages=dict(
        splashes=Panda3DSplash(
            exit_stage='main_game_stage',
            splash_args=dict(
                pattern=Pattern.WHEEL,
                colors=Colors.RAINBOW,
                pattern_freq=1,
                cycle_freq=5,
            ),
        ),
        main_game_stage=MainGameStage(),
        quit=Quit(),
    ),
    #initial_stage='splashes',
    initial_stage='main_game_stage',
)

