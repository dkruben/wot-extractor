# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/battle_loading.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/battle_loading.py
from __future__ import absolute_import
import random
from account_helpers.settings_core.options import BattleLoadingTipSetting
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
_FORT_RUSH_TIP_ICONS = tuple(backport.image(R.images.fort_rush.gui.maps.icons.battle_loading.dyn(('tip_{:02d}').format(index))()) for index in range(1, 4))
_FORT_RUSH_TIP_TEXT = (
 (
  R.strings.fort_rush.battleLoading.tips.tip01.title(), R.strings.fort_rush.battleLoading.tips.tip01.description()),
 (
  R.strings.fort_rush.battleLoading.tips.tip02.title(), R.strings.fort_rush.battleLoading.tips.tip02.description()),
 (
  R.strings.fort_rush.battleLoading.tips.tip03.title(), R.strings.fort_rush.battleLoading.tips.tip03.description()))

class FortRushBattleLoading(BattleLoading):

    def __init__(self):
        super(FortRushBattleLoading, self).__init__()
        self.__tipIndex = random.randrange(len(_FORT_RUSH_TIP_ICONS))
        self.__tipIcon = _FORT_RUSH_TIP_ICONS[self.__tipIndex]

    def _setTipsInfo(self):
        super(FortRushBattleLoading, self)._setTipsInfo()
        titleRes, descriptionRes = _FORT_RUSH_TIP_TEXT[self.__tipIndex]
        self.as_setTipTitleS(self._formatTipTitle(backport.text(titleRes)))
        self.as_setTipS(self._formatTipBody(backport.text(descriptionRes)))

    def _makeVisualTipVO(self, arenaDP, tip=None):
        vo = super(FortRushBattleLoading, self)._makeVisualTipVO(arenaDP, tip)
        settingID = BattleLoadingTipSetting.OPTIONS.VISUAL
        vo.update({'settingID': settingID, 
           'tipIcon': (self.__tipIcon), 
           'showMinimap': False, 
           'showTableBackground': False, 
           'showTipsBackground': True})
        vo.update(self._getViewSettingByID(settingID))
        return vo
