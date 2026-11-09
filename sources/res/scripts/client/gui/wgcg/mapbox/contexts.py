# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/mapbox/contexts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/mapbox/contexts.py
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class MapboxProgressionCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.MAPBOX_PROGRESSION

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False


class MapboxCompleteSurveyCtx(CommonWebRequestCtx):

    def __init__(self, surveyData, waitingID=''):
        super(MapboxCompleteSurveyCtx, self).__init__(waitingID=waitingID)
        self.__surveyData = surveyData

    def getSurveyData(self):
        return self.__surveyData

    def getRequestType(self):
        return WebRequestDataType.MAPBOX_SURVEY_COMPLETE

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False


class MapboxRequestAuthorizedURLCtx(CommonWebRequestCtx):

    def __init__(self, mapURL, waitingID=''):
        super(MapboxRequestAuthorizedURLCtx, self).__init__(waitingID=waitingID)
        self.__mapURL = mapURL

    def getMapURL(self):
        return self.__mapURL

    def getRequestType(self):
        return WebRequestDataType.MAPBOX_SURVEY_URL

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False
