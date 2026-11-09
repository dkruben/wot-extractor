# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/battle_session/legacy/ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/ctx.py
from CurrentVehicle import g_currentVehicle
from constants import OBSERVER_VEH_INVENTORY_ID, OBSERVER_VEH_NAME, ARENA_BONUS_TYPE
from gui.prb_control.entities.base.legacy.ctx import JoinLegacyCtx, SetPlayerStateCtx
from gui.prb_control.prb_getters import getPrebattleSettings
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getID', 'prbID'), ('getPrbTypeName', 'type'), ('getPrbClusterId',
                                                                          'prbClusterID'), ('getWaitingID',
                                                                                            'waitingID'))
class JoinBattleSessionCtx(JoinLegacyCtx):
    __slots__ = ()

    def __init__(self, prbID, prbType, prbClusterID, waitingID='', flags=FUNCTIONAL_FLAG.UNDEFINED):
        super(JoinBattleSessionCtx, self).__init__(prbID, prbType, prbClusterID, waitingID=waitingID, flags=flags)


class BattleSessionSetPlayerStateCtx(SetPlayerStateCtx):

    def getVehicleInventoryID(self):
        bonusType = getPrebattleSettings()['bonusType']
        if g_currentVehicle.item.name == OBSERVER_VEH_NAME and bonusType == ARENA_BONUS_TYPE.TOURNAMENT_COMP7:
            return OBSERVER_VEH_INVENTORY_ID
        return super(BattleSessionSetPlayerStateCtx, self).getVehicleInventoryID()
