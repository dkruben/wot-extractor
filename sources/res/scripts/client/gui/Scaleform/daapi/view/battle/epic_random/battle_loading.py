# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/epic_random/battle_loading.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/battle_loading.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading, BattleLoadingTipSetting

class EpicRandomBattleLoading(BattleLoading):

    def _getViewSettingByID(self, settingID):
        result = {}
        if settingID == BattleLoadingTipSetting.OPTIONS.TEXT:
            result.update({'leftTeamTitleLeft': (-418), 
               'rightTeamTitleLeft': 200, 
               'tipTitleTop': 536, 
               'tipBodyTop': 562, 
               'showTableBackground': True, 
               'showTipsBackground': False})
        else:
            result.update({'leftTeamTitleLeft': (-468), 
               'rightTeamTitleLeft': 255, 
               'tipTitleTop': 366, 
               'tipBodyTop': 397, 
               'showTableBackground': False, 
               'showTipsBackground': True})
        return result
