# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/seasons_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/seasons_controller.py
from __future__ import absolute_import
from constants import GameSeasonType
from soft_exception import SoftException
from helpers import dependency
from skeletons.gui.game_control import ISeasonsController, IRankedBattlesController, IEpicBattleMetaGameController, IMapboxController, IEventBattlesController
from gui.shared.system_factory import registerSeasonProviderHandler, collectSeasonProviderHandler
registerSeasonProviderHandler(GameSeasonType.RANKED, (lambda *args, **kwargs: dependency.instance(IRankedBattlesController)))
registerSeasonProviderHandler(GameSeasonType.EPIC, (lambda *args, **kwargs: dependency.instance(IEpicBattleMetaGameController)))
registerSeasonProviderHandler(GameSeasonType.MAPBOX, (lambda *args, **kwargs: dependency.instance(IMapboxController)))
registerSeasonProviderHandler(GameSeasonType.EVENT_BATTLES, (lambda *args, **kwargs: dependency.instance(IEventBattlesController)))

class SeasonsController(ISeasonsController):

    def hasAnySeason(self, seasonType):
        return self.__getSeasonProviderChecked(seasonType).hasAnySeason()

    def getCurrentSeason(self, seasonType):
        return self.__getSeasonProviderChecked(seasonType).getCurrentSeason()

    def getCurrentCycleID(self, seasonType):
        return self.__getSeasonProviderChecked(seasonType).getCurrentCycleID()

    def getSeason(self, seasonType, seasonID):
        return self.__getSeasonProviderChecked(seasonType).getSeason(seasonID)

    def isSeasonActive(self, seasonID, seasonType):
        season = self.getCurrentSeason(seasonType)
        return season is not None and season.getSeasonID() == seasonID

    def isWithinSeasonTime(self, seasonID, seasonType):
        return self.__getSeasonProviderChecked(seasonType).isWithinSeasonTime(seasonID)

    def isSeasonCycleActive(self, cycleID, seasonType):
        return self.getCurrentCycleID(seasonType) == cycleID

    def __getSeasonProviderChecked(self, seasonType):
        handler = collectSeasonProviderHandler(seasonType)
        if handler is None:
            raise SoftException(('Invalid seasonType [{}]! No suitable season provider found.').format(seasonType))
        return handler()
