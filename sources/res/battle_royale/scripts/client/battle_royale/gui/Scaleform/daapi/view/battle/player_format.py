# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/player_format.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/player_format.py
from __future__ import absolute_import
import logging, BigWorld
from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO
from gui.battle_control.arena_info.player_format import PlayerFullNameFormatter
from helpers import dependency
from items.battle_royale import isSpawnedBot
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class BattleRoyalePlayerFullNameFormatter(PlayerFullNameFormatter):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def format(self, vInfoVO, playerName=None):
        if isSpawnedBot(vInfoVO.vehicleType.tags):
            botVehID = vInfoVO.vehicleID
            botVehicle = BigWorld.entities.get(botVehID)
            if botVehicle:
                masterVehId = botVehicle.masterVehID
                for vI in self.__sessionProvider.getArenaDP().getVehiclesInfoIterator():
                    if vI.vehicleID == masterVehId:
                        vInfoVO = vI
                        break
                else:
                    defBotName = ' '
                    _logger.warning('The Master vehicle of a bot (id=%s) has not been found, use default name %s', botVehID, defBotName)
                    vInfoVO = VehicleArenaInfoVO(botVehID)
                    return super(BattleRoyalePlayerFullNameFormatter, self).format(vInfoVO, playerName=defBotName)

            else:
                defBotName = ' '
                _logger.warning('Bot vehicle (id=%s) has not been found, use default name %s', botVehID, defBotName)
                vInfoVO = VehicleArenaInfoVO(botVehID)
                return super(BattleRoyalePlayerFullNameFormatter, self).format(vInfoVO, playerName=defBotName)
        selfFormat = super(BattleRoyalePlayerFullNameFormatter, self).format(vInfoVO, playerName)
        return selfFormat
