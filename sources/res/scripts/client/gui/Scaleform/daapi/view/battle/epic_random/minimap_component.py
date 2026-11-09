# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/epic_random/minimap_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/minimap_component.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent
from gui.Scaleform.daapi.view.battle.classic.minimap import TeamsOrControlsPointsPlugin
_SCALE_FAC = 2.0 / 3.0

class EpicRandomMinimapComponent(ClassicMinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(EpicRandomMinimapComponent, self)._setupPlugins(arenaVisitor)
        setup['points'] = EpicRandomTeamsOrControlsPointsPlugin
        return setup


class EpicRandomTeamsOrControlsPointsPlugin(TeamsOrControlsPointsPlugin):

    def _addPointEntry(self, symbol, position, number):
        entryID = super(EpicRandomTeamsOrControlsPointsPlugin, self)._addPointEntry(symbol, position, number)
        self._invoke(entryID, 'setScale', _SCALE_FAC)
        return entryID
