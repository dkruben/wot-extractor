# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/squad/ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/entities/squad/ctx.py
from __future__ import absolute_import
from constants import PREBATTLE_TYPE
from fun_random.gui.fun_gui_constants import REQUEST_TYPE, FUNCTIONAL_FLAG
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getDesiredSubModeID', 'desiredSubModeID'))
class FunSquadSettingsCtx(SquadSettingsCtx):
    __slots__ = ('__desiredSubModeID', )

    def __init__(self, desiredSubModeID, flags=FUNCTIONAL_FLAG.UNDEFINED, accountsToInvite=None, isForced=False):
        prebattleType, waitingID = PREBATTLE_TYPE.FUN_RANDOM, 'prebattle/create'
        flags |= FUNCTIONAL_FLAG.FUN_RANDOM
        super(FunSquadSettingsCtx, self).__init__(prebattleType, waitingID, flags, accountsToInvite, isForced)
        self.__desiredSubModeID = desiredSubModeID

    def getDesiredSubModeID(self):
        return self.__desiredSubModeID


@ReprInjector.withParent(('getDesiredSubModeID', 'desiredSubModeID'))
class FunSquadChangeSubModeCtx(UnitRequestCtx):
    __slots__ = ('__desiredSubModeID', )

    def __init__(self, desiredSubModeID):
        super(FunSquadChangeSubModeCtx, self).__init__()
        self.__desiredSubModeID = desiredSubModeID

    def getCooldown(self):
        return 2.0

    def getDesiredSubModeID(self):
        return self.__desiredSubModeID

    def getRequestType(self):
        return REQUEST_TYPE.CHANGE_FUN_SUB_MODE
