# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/battle_loading.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/battle_loading.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
from account_helpers.settings_core.options import BattleLoadingTipSetting

class Comp7BattleLoading(BattleLoading):

    def _getViewSettingByID(self, settingID):
        result = super(Comp7BattleLoading, self)._getViewSettingByID(settingID)
        result.update({'leftTeamTitleLeft': (-483), 
           'rightTeamTitleLeft': 275})
        return result

    def _makeVisualTipVO(self, arenaDP, tip=None):
        settingID = BattleLoadingTipSetting.OPTIONS.MINIMAP
        vo = {'settingID': settingID, 
           'tipIcon': None, 
           'arenaTypeID': (self._arenaVisitor.type.getID()), 
           'minimapTeam': (arenaDP.getNumberOfTeam()), 
           'showMinimap': True, 
           'showTipsBackground': True}
        vo.update(self._getViewSettingByID(settingID))
        return vo
