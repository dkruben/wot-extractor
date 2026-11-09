# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/br_helpers/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/br_helpers/utils.py
from __future__ import absolute_import
from battle_royale.gui.impl.gen.view_models.views.lobby.enums import SubMode, CoinType
from battle_royale.gui.impl.lobby.views.states import BattleRoyaleBattleResultsState
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController

def isBattleResultsStateEntered():
    state = getLobbyStateMachine().getStateByCls(BattleRoyaleBattleResultsState)
    return state and state.isEntered()


@dependency.replace_none_kwargs(battleRoyaleController=IBattleRoyaleController)
def setEventInfo(model, battleRoyaleController=None):
    if battleRoyaleController.isStPatrick():
        subMode = SubMode.STPATRICK
        coinType = CoinType.STPCOIN
    else:
        subMode = SubMode.DEFAULT
        coinType = CoinType.BRCOIN
    model.setSubMode(subMode)
    model.setCoinType(coinType)
