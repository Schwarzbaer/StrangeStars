"""Boilerplate setup for a WECS-based game.
"""

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

setup(
    name='wecs-null-project',
    version='0.0.1a',
    description='A boilerplate for WECS-based games',
    url='https://github.com/TheCheapestPixels/wecs-null-project',
    author='TheCheapestPixels',
    author_email='TheCheapestPixels@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='wecs',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.7, <3.8',
    install_requires=['wecs', 'panda3d', 'panda3d-cefconsole', 'panda3d-keybindings'],
    entry_points={
        'console_scripts': [
            'wecs_null_game=main:run_game',
        ],
    },
    # Deployment
    options = {
        'build_apps': {
            'include_patterns': [
                '**/*.png',
                '**/*.jpg',
                '**/*.bam',
                '**/*.toml',
                '**/*.html',
            ],
            'include_modules': {
                '*': [
                    'keybindings',
                    # 'cefconsole',
                    'urllib.request',  # Maybe hidden import in cefpython
                ],
            },
            'gui_apps': {
                'WECS null game': 'main.py',
            },
            'log_filename': '$USER_APPDATA/wecs_null_game/output.log',
            'log_append': False,
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
            'platforms': [
                'manylinux1_x86_64',
                #'macosx_10_6_x86_64',
                #'win_amd64',
            ],
        },
    },
)
