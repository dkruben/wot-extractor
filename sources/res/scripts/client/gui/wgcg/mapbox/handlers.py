# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/mapbox/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/mapbox/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class MapboxRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.MAPBOX_PROGRESSION): (self.__getMapboxProgression), 
           (WebRequestDataType.MAPBOX_SURVEY_COMPLETE): (self.__completeSurvey), 
           (WebRequestDataType.MAPBOX_SURVEY_URL): (self.__requestAuthorizedSurveyURL)}
        return handlers

    def __getMapboxProgression(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('mapbox', 'get_mapbox_progression'))

    def __completeSurvey(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('mapbox', 'complete_survey'), ctx.getSurveyData())

    def __requestAuthorizedSurveyURL(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('mapbox', 'request_authorized_survey_url'), ctx.getMapURL())
