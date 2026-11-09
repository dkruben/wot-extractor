# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/shared/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/shared/utils.py
from __future__ import absolute_import
import BigWorld
from helpers import isPlayerAvatar

def getScoreComponent():
    player = BigWorld.player()
    if not (player and isPlayerAvatar() and player.arena and player.arena.arenaInfo):
        return None
    else:
        return player.arena.arenaInfo.dynamicComponents.get('FortRushScoreComponent')
