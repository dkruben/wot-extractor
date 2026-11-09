# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/epic_random/page.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/page.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage, COMMON_CLASSIC_CONFIG, EXTENDED_CLASSIC_CONFIG
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
_EPIC_RANDOM_CLASSICS_COMPONENTS = COMMON_CLASSIC_CONFIG
_EPIC_RANDOM_EXTENDED_COMPONENTS = EXTENDED_CLASSIC_CONFIG

class EpicRandomPage(ClassicPage):

    def __init__(self, components=None, external=None, fullStatsAlias=BATTLE_VIEW_ALIASES.FULL_STATS, **kwargs):
        if components is None:
            components = _EPIC_RANDOM_CLASSICS_COMPONENTS if self.sessionProvider.isReplayPlaying else _EPIC_RANDOM_EXTENDED_COMPONENTS
        super(EpicRandomPage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
        return

    def _onBattleLoadingStart(self):
        super(EpicRandomPage, self)._onBattleLoadingStart()
        if not self.sessionProvider.isReplayPlaying:
            self.app.enterGuiControlMode(BATTLE_VIEW_ALIASES.BATTLE_LOADING)

    def _onBattleLoadingFinish(self):
        super(EpicRandomPage, self)._onBattleLoadingFinish()
        if not self.sessionProvider.isReplayPlaying:
            self.app.leaveGuiControlMode(BATTLE_VIEW_ALIASES.BATTLE_LOADING)
