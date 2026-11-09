# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trainings/formatters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/trainings/formatters.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.utils.functions import getArenaSubTypeName

def getRoundLenString(roundLength):
    return backport.text(R.strings.menu.training.info.timeout.value(), roundLength=roundLength // 60)


def getTrainingRoomTitle(arenaType):
    return backport.text(R.strings.menu.training.info.title(), arenaName=arenaType.name)


def getArenaSubTypeString(arenaTypeID):
    arenaSubTypeName = getArenaSubTypeName(arenaTypeID)
    return backport.text(R.strings.arenas.type.dyn(arenaSubTypeName).name())


def getPlayerStateString(state):
    stateStr = ('state{}').format(state)
    return backport.text(R.strings.menu.training.info.states.dyn(stateStr)())
