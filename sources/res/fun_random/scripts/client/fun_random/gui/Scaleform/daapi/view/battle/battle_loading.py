# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/battle/battle_loading.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/battle/battle_loading.py
from __future__ import absolute_import
from account_helpers.settings_core.options import BattleLoadingTipSetting
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading

class FepBattleLoading(BattleLoading):

    def _getSettingsID(self, loadingInfo, tip):
        if tip is not None and tip.isValid():
            return self.settingsCore.options.getSetting(loadingInfo).getSettingID(isVisualOnly=True)
        else:
            return BattleLoadingTipSetting.OPTIONS.MINIMAP
