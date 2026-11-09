# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/frontline/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/frontline/__init__.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from web.web_client_api import w2c, w2capi, W2CSchema

@w2capi(name='frontline', key='action')
class FrontLineWebApi(W2CSchema):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    @w2c(W2CSchema, name='get_player_discount')
    def handleGetPlayerDiscount(self, _):
        return self.__epicController.getStoredEpicDiscount()

    @w2c(W2CSchema, name='get_calendar_info')
    def handleGetCalendarInfo(self, _):
        calendarData = {}
        seasons = (
         self.__epicController.getCurrentSeason(),
         self.__epicController.getNextSeason(),
         self.__epicController.getPreviousSeason())
        for season in seasons:
            if season is not None:
                calendarData['season'] = {'id': (season.getSeasonID()), 'start': (season.getStartDate()), 
                   'end': (season.getEndDate())}
                calendarData['cycles'] = [{'id': (cycle.ID), 'start': (cycle.startDate), 'end': (cycle.endDate), 'announce_only': (cycle.announceOnly)} for cycle in season.getAllCycles().values()]
                break

        return calendarData
