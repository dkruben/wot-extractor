# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/clans/cache_providers/stronghold_event_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/clans/cache_providers/stronghold_event_provider.py
import weakref, typing
from constants import CLAN_ROLES
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getStrongholdEventEnabled
from gui.clans.cache_providers.base_provider import BaseProvider, RequestSettings, UpdatePeriodType
from gui.wgcg.clan.contexts import StrongholdEventSettingsCtx
from helpers import time_utils
from shared_utils import CONST_CONTAINER
if typing.TYPE_CHECKING:
    from typing import Optional, Dict
    from gui.clans.data_wrapper.stronghold_event import StrongholdEventSettingsData

class _DataNames(CONST_CONTAINER):
    SETTINGS = 'SETTINGS'


class StrongholdEventProvider(BaseProvider):

    def __init__(self, clanCache):
        self.__clanCache = weakref.proxy(clanCache)
        super(StrongholdEventProvider, self).__init__()

    def start(self):
        super(StrongholdEventProvider, self).start()
        self._requestData(_DataNames.SETTINGS)

    def getSettings(self):
        return self._getData(_DataNames.SETTINGS).data

    def isRunning(self):
        settings = self.getSettings()
        if settings is None:
            return False
        else:
            return settings.getStartDate() < time_utils.getServerUTCTime() < settings.getEndDate()

    def canUnfreezeVehicles(self):
        settings = self.getSettings()
        if settings is None:
            return False
        else:
            role = CLAN_ROLES.getRole(self.__clanCache.clanRole)
            unfreezeRoles = settings.getEventConfig().getUnfreezeVehicleRoles()
            if unfreezeRoles:
                return role in unfreezeRoles
            return False

    @property
    def _dataNameContainer(self):
        return _DataNames

    @property
    def _isEnabled(self):
        return getStrongholdEventEnabled()

    def _getSettings(self):
        return {(_DataNames.SETTINGS): (RequestSettings(context=StrongholdEventSettingsCtx(), isCached=True, updatePeriodType=UpdatePeriodType.AFTER_BATTLE, updateKwargs=None))}
