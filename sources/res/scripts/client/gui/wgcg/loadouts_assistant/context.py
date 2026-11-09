# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/loadouts_assistant/context.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/loadouts_assistant/context.py
from typing import List, Set
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType
from gui.game_control.wotlda.constants import SupportedWotldaLoadoutType

class LoadoutsAssistantCtx(CommonWebRequestCtx):
    _LOADOUT_TYPES = set()

    def __init__(self, clientCacheUpdatedAt):
        super(LoadoutsAssistantCtx, self).__init__()
        self._clientCacheUpdatedAt = clientCacheUpdatedAt

    def getRequestType(self):
        return WebRequestDataType.WOTLDA_GET_LOADOUTS

    def getClientCacheUpdatedAt(self):
        return self._clientCacheUpdatedAt

    def getLoadoutTypes(self):
        return [type_.value for type_ in self._LOADOUT_TYPES]

    def getLoadoutTypesForRequest(self):
        return (',').join([type_.value for type_ in self._LOADOUT_TYPES])

    def isAuthorizationRequired(self):
        return True


class EasyTankEquipCtx(LoadoutsAssistantCtx):
    _LOADOUT_TYPES = {
     SupportedWotldaLoadoutType.EASY_TANK_EQUIP}


class GenericLoadoutAssistanceCtx(LoadoutsAssistantCtx):

    def addLoadoutTypes(self, types):
        self._LOADOUT_TYPES.update(types)
