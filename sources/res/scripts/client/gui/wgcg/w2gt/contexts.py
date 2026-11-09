# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/w2gt/contexts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/w2gt/contexts.py
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class W2gtCtx(CommonWebRequestCtx):

    def __init__(self, clientVersion, eTag, geometryName, gameplayType, vehRole, vehLevel, team, waitingID=''):
        self.__eTag = eTag
        vehicleRole = self.normalizeVehicleRole(vehRole)
        self.__params = {'client_version': clientVersion, 
           'map_name': geometryName, 
           'gameplay_type': gameplayType, 
           'vehicle_role': vehicleRole, 
           'level': vehLevel, 
           'team': team}
        super(W2gtCtx, self).__init__(waitingID=waitingID)

    @staticmethod
    def normalizeVehicleRole(vehRole):
        if vehRole.startswith('role_'):
            return vehRole.split('_', 1)[-1]
        return vehRole

    def getRequestType(self):
        return WebRequestDataType.W2GT_DATA

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getParams(self):
        return self.__params

    def getHeaders(self):
        if self.__eTag:
            return {'If-None-Match': (self.__eTag)}
        return {}
