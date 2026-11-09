# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/__init__.py
from __future__ import absolute_import
from gui.shared.utils.functions import getArenaGeometryName
from gui.impl import backport
from gui.impl.gen import R
MAX_MEMBERS_IN_CLAN = 100

def getI18ArenaById(arenaId):
    mapName = getArenaGeometryName(arenaId)
    dynAccessor = R.strings.arenas.dyn(('c_{}').format(mapName))
    if dynAccessor.isValid():
        return backport.text(dynAccessor.name())
    return mapName
