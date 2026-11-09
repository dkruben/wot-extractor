# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/game_control/__init__.py
from __future__ import absolute_import
from battle_royale.gui.game_control.awards_controller import BRProgressionStageHandler
from battle_royale.gui.game_control.progression_controller import BRProgressionController
from battle_royale.gui.game_control.battle_royale_controller import BattleRoyaleController as _BattleRoyale
from battle_royale.gui.game_control.battle_royale_tournament_controller import BattleRoyaleTournamentController as _BRTournament
import skeletons.gui.game_control as _interface
from gui.shared.system_factory import registerAwardControllerHandler, registerGameControllers
from chat_shared import SYS_MESSAGE_TYPE
from soft_exception import SoftException

def registerBRGameControllers():
    from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController
    registerGameControllers([
     (
      _interface.IBattleRoyaleController, _BattleRoyale, False),
     (
      _interface.IBattleRoyaleTournamentController, _BRTournament, False),
     (
      IBRProgressionOnTokensController, BRProgressionController, False)])


def registerBRProgressionAwardControllers():
    try:
        SYS_MESSAGE_TYPE.BRProgressionNotification.index()
    except AttributeError:
        raise SoftException('No index for {attr} found. Use registerSystemMessagesTypes before')

    registerAwardControllerHandler(BRProgressionStageHandler)
