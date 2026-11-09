# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_loading.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_loading.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class FrontlineEpicBattleLoading(BattleLoading):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def _getBattlesCount(self):
        return self.lobbyContext.getEpicBattlesCount()
