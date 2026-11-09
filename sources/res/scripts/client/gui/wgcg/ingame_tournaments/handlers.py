# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/ingame_tournaments/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/ingame_tournaments/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class IngameTournamentHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.INGAME_TOURNAMENT_GET_DATA): (self.__getTournamentData)}
        return handlers

    def __getTournamentData(self, ctx, callback):
        self._requester.doRequestEx(ctx, callback, ('tournaments', 'get_ingame_tournament'))
