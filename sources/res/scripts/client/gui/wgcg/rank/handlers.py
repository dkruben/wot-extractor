# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/rank/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/rank/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class RankRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.RANKED_LEAGUE_POSITION): (self.__getRankedPosition), 
           (WebRequestDataType.RANKED_YEAR_POSITION): (self.__getRankedYearPosition)}
        return handlers

    def __getRankedPosition(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('rblb', 'user_ranked_position'))

    def __getRankedYearPosition(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('rblb', 'user_ranked_year_position'))
