#!/usr/bin/env python

import os

from panda3d.core import loadPrcFileData

from wecs import boilerplate


def run_game():
    boilerplate.run_game(
        module_name='game',     # Name of module to use to set up game
        console=False,          # panda3d-cefconsole
        keybindings=True,       # panda3d-keybindings
        debug_keys=False,       # Esc/F9-12 via accept()
        simplepbr=False,        # calls simplepbr.init(simplepbr_kwargs)
        simplepbr_kwargs=None,  # default: {}
    )


if __name__ == '__main__':
    # loadPrcFileData('', 'fullscreen true')
    loadPrcFileData('', 'framebuffer-multisample true')
    loadPrcFileData('', 'multisamples 16')
    run_game()
