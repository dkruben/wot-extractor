# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/BattleXP.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/BattleXP.py
from __future__ import absolute_import
import BigWorld

class BattleXP(BigWorld.DynamicScriptComponent):

    def onEnterWorld(self, *args):
        pass

    def onLeaveWorld(self, *args):
        pass

    def set_battleXP(self, _=None):
        if self.battleXP < 0:
            return
        else:
            ctrl = self.entity.guiSessionProvider.dynamic.progression
            if ctrl is not None:
                ctrl.updateXP(self.battleXP, self.entity.id)
            return

    def set_battleXpLvlData(self, _=None):
        pass
