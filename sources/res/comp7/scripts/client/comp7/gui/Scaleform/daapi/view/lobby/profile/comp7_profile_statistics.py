# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/comp7_profile_statistics.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/comp7_profile_statistics.py
from __future__ import absolute_import
from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_helper import getBattleHandlers
from comp7.gui.Scaleform.daapi.view.lobby.profile.profile_statistics_vos import getComp7StatisticsVO
from comp7.gui.Scaleform.daapi.view.lobby.profile.seasons_manager import getComp7SeasonManagers
from gui.Scaleform.daapi.view.lobby.profile.ProfileStatistics import ProfileStatistics
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS

class Comp7ProfileStatistics(ProfileStatistics):

    def __init__(self, *args):
        super(Comp7ProfileStatistics, self).__init__(*args)
        self._battleTypeHandlers.update(getBattleHandlers())
        self._seasonsManagers.update(getComp7SeasonManagers())

    @classmethod
    def _makeBattleTypesDropDown(cls, accountDossier, forVehiclesPage=False):
        result = super(Comp7ProfileStatistics, cls)._makeBattleTypesDropDown(accountDossier, forVehiclesPage)
        result.addByKey(PROFILE_DROPDOWN_KEYS.COMP7)
        return result

    def _setStatisticsVO(self, targetData, accountDossier):
        if self._battlesType == PROFILE_DROPDOWN_KEYS.COMP7:
            vo = getComp7StatisticsVO(self._battlesType, targetData, accountDossier, self._userID is None)
            self._seasonsManagers.addSeasonsDropdown(vo)
            self.as_responseDossierS(self._battlesType, vo, 'comp7', '')
        else:
            super(Comp7ProfileStatistics, self)._setStatisticsVO(targetData, accountDossier)
        return
