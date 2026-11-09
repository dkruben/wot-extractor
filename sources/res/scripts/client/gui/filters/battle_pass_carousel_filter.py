# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/filters/battle_pass_carousel_filter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/filters/battle_pass_carousel_filter.py
from account_helpers.AccountSettings import CAROUSEL_FILTER_1, CAROUSEL_FILTER_2, CAROUSEL_FILTER_3, CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1
from gui.filters.carousel_filter import CarouselFilter, CustomizationCriteriesGroup, EventCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass import BattlePassFilterConsts

class BattlePassCarouselFilter(CarouselFilter):
    __battlePassController = dependency.descriptor(IBattlePassController)

    def __init__(self):
        super(BattlePassCarouselFilter, self).__init__()
        self._serverSections = (CAROUSEL_FILTER_1, CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1,
         CAROUSEL_FILTER_3)
        self._clientSections = (CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)
        self._criteriesGroups = (
         EventCriteriesGroup(), BattlePassCriteriesGroup())
        self.currentSeasonID = 0

    def save(self):
        self.currentSeasonID = self.__battlePassController.getSeasonID()
        self._filters[BattlePassFilterConsts.FILTER_KEY_SEASON] = self.currentSeasonID
        super(BattlePassCarouselFilter, self).save()
        self.reset(keys=[BattlePassFilterConsts.FILTER_KEY_SEASON], save=False)

    def load(self):
        super(BattlePassCarouselFilter, self).load()
        currentSeason = self.__battlePassController.getSeasonID()
        lastSeason = self._filters.get(BattlePassFilterConsts.FILTER_KEY_SEASON, currentSeason)
        if lastSeason != currentSeason:
            self.reset(keys=BattlePassFilterConsts.FILTERS_KEYS, save=False)
        self.reset(keys=[BattlePassFilterConsts.FILTER_KEY_SEASON], save=False)
        self.currentSeasonID = currentSeason


class BattlePassCriteriesGroup(CustomizationCriteriesGroup):
    __battlePassController = dependency.descriptor(IBattlePassController)

    def update(self, filters):
        super(BattlePassCriteriesGroup, self).update(filters)
        if filters[BattlePassFilterConsts.FILTER_KEY_COMMON]:
            self.__addGeneralBattlePassCriteria()
            self._criteria |= REQ_CRITERIA.CUSTOM(self.__isCommonProgression)

    @classmethod
    def __isCommonProgression(cls, vehicle):
        progress, cap = cls.__battlePassController.getVehicleProgression(vehicle.intCD)
        return cap > 0 and progress < cap

    def __addGeneralBattlePassCriteria(self):
        self._criteria |= ~REQ_CRITERIA.VEHICLE.EPIC_BATTLE
