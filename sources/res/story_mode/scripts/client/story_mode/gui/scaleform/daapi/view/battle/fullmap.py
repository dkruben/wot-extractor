# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/fullmap.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/fullmap.py
from __future__ import absolute_import
import BattleReplay
from gui.Scaleform.daapi.view.battle.pve_base.fullmap import PveFullMapComponent
from story_mode.gui.scaleform.daapi.view.battle.minimap import BunkersPlugin, adjustBoundingBox, StoryModeMinimapPingPlugin, StoryModeArenaVehiclesPlugin

class StoryModeFullMapComponent(PveFullMapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(StoryModeFullMapComponent, self)._setupPlugins(arenaVisitor)
        setup['bunkers'] = BunkersPlugin
        setup['vehicles'] = StoryModeArenaVehiclesPlugin
        if not BattleReplay.g_replayCtrl.isPlaying:
            setup['pinging'] = StoryModeMinimapPingPlugin
        return setup

    def getBoundingBox(self):
        arenaVisitor = self.sessionProvider.arenaVisitor
        return adjustBoundingBox(*arenaVisitor.type.getBoundingBox())
