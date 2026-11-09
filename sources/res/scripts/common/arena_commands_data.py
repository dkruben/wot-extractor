# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/arena_commands_data.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/arena_commands_data.py
from __future__ import absolute_import, division
from collections import namedtuple
HESH_MAP_SIZE = 1000
HESH_GRID_STEP = 6
MAX_POSE_SIZE = HESH_MAP_SIZE // HESH_GRID_STEP

def getHashCode(pose):
    return sum([int(coord + HESH_MAP_SIZE * 0.5 + 0.5) // HESH_GRID_STEP * MAX_POSE_SIZE ** i for i, coord in enumerate(pose)])


class ArenaCommandData(namedtuple('ArenaCommandData', [
 'commandName', 
 'position', 
 'owner', 
 'name', 
 'state'])):

    @staticmethod
    def getCommandData(*args, **kwargs):
        if kwargs:
            data = ArenaCommandData(kwargs.get('commandName', 'PREBATTLE_WAYPOINT'), kwargs.get('position', (0.0,
                                                                                                             0.0,
                                                                                                             0.0)), kwargs.get('team', '') or kwargs.get('teams', 'both'), kwargs.get('name', '') or kwargs.get('locationName', 'ERROR'), kwargs.get('state', 'IDLE'))
            return (
             getHashCode(kwargs['position']), data)
        else:
            return


ArenaCommandData.__new__.__defaults__ = (None, ) * len(ArenaCommandData._fields)
