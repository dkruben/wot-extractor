# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_damage_pannel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_damage_pannel.py
from __future__ import absolute_import
import BigWorld
from frontline.gui.Scaleform.daapi.view.meta.FrontlineDamagePanelMeta import FrontlineDamagePanelMeta
from gui.Scaleform.daapi.view.battle.shared.damage_panel import DamagePanel

class FrontlineDamagePanel(DamagePanel, FrontlineDamagePanelMeta):

    def _populate(self):
        super(FrontlineDamagePanel, self)._populate()
        BigWorld.player().arena.componentSystem.playerDataComponent.onCrewRolesFactorUpdated += self.__setGeneralBonus

    def _dispose(self):
        super(FrontlineDamagePanel, self)._dispose()
        arena = BigWorld.player().arena if hasattr(BigWorld.player(), 'arena') else None
        if arena and hasattr(arena, 'componentSystem'):
            componentSystem = BigWorld.player().arena.componentSystem
            if componentSystem:
                componentSystem.playerDataComponent.onCrewRolesFactorUpdated -= self.__setGeneralBonus
        return

    def __setGeneralBonus(self, newFactor, allyVehID=None, allyNewRank=None):
        self.as_setGeneralBonusS(newFactor)
