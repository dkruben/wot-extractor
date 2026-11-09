# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/active_vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/active_vehicle.py
from __future__ import absolute_import
import logging
from typing import TYPE_CHECKING
import BigWorld, AccountCommands
from items.components.c11n_constants import SeasonType
from soft_exception import SoftException
if TYPE_CHECKING:
    from typing import Any as TAny
_logger = logging.getLogger(__name__)

class ActiveVehicleSeasonType(object):

    def __init__(self):
        self._vehTypeDescrToSeason = {'customizationDisplayType': {}}

    def get(self, vehTypeDescr, defaultSeasonType):
        season = self._vehTypeDescrToSeason.get(vehTypeDescr, defaultSeasonType)
        if season == SeasonType.UNDEFINED:
            return defaultSeasonType
        return season

    def __setitem__(self, vehTypeDescr, seasonType):
        if seasonType not in SeasonType.RANGE and seasonType != SeasonType.UNDEFINED:
            raise SoftException(("Invalid SeasonType '{}'").format(seasonType))
        if self.get(vehTypeDescr, SeasonType.UNDEFINED) != seasonType:
            self._vehTypeDescrToSeason[vehTypeDescr] = seasonType
            self.__updateServer(vehTypeDescr, seasonType)

    def __getitem__(self, vehTypeDescr):
        return self._vehTypeDescrToSeason[vehTypeDescr]

    def __contains__(self, vehTypeDescr):
        return vehTypeDescr in self._vehTypeDescrToSeason

    def __updateServer(self, vehTypeDescr, seasonType):
        player = BigWorld.player()
        if player is not None and hasattr(player, '_doCmdInt2'):
            player._doCmdInt2(AccountCommands.CMD_SET_ACTIVE_VEH_SEASON, vehTypeDescr, seasonType, self.__onSetActiveVehSeason)
        return

    def __onSetActiveVehSeason(self, requestID, resultID, errorStr, ext=None):
        logFunc = _logger.debug
        if isinstance(ext, dict) and ext.get('exception_message'):
            logFunc = _logger.error
        logFunc('__onSetActiveVehSeason requestID=%s resultID=%s, errorStr=%s, ext=%s', requestID, resultID, errorStr, ext)
