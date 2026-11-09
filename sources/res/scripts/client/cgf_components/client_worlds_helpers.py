# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/client_worlds_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/client_worlds_helpers.py
from __future__ import absolute_import
import enum, BattleReplay
from constants import IS_UE_EDITOR
from helpers import isPlayerAccount, isPlayerAvatar

class ClientWorld(enum.IntEnum):
    NONE = 0
    BATTLE = 1
    HANGAR = 2
    EDITOR = 4
    AllWorlds = BATTLE | HANGAR | EDITOR


def getClientWorld():
    if IS_UE_EDITOR:
        clientWorld = ClientWorld.EDITOR
    elif isPlayerAccount():
        clientWorld = ClientWorld.HANGAR
    elif isPlayerAvatar() or BattleReplay.isPlaying() or BattleReplay.isServerSideReplay():
        clientWorld = ClientWorld.BATTLE
    else:
        clientWorld = ClientWorld.NONE
    return clientWorld


def clientWorldsPredicate(clientWorlds):

    def predicate(_):
        return bool(getClientWorld() & clientWorlds)

    return predicate
