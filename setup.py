"""Boilerplate setup for a WECS-based game.
"""

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

setup(
    name='strange-stars',
    version='0.0.1a',
    description='An arcady space game',
    url='https://github.com/Schwarzbaer/StrangeStars/',
    author='TheCheapestPixels',
    author_email='TheCheapestPixels@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.7',
    install_requires=[
        'toml',
        'panda3d',
        'panda3d-keybindings',
        'panda3d-logos',
        'panda3d-stageflow',
        'wecs',
    ],
    entry_points={
        'console_scripts': [
            'StrangeStars=main:run_game',
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
            ],
            'include_modules': {
                '*': [
                    'keybindings',
                    'game',
                ],
            },
            'gui_apps': {
                'Strange Stars': 'main.py',
            },
            'log_filename': '$USER_APPDATA/StrangeStars/output.log',
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
