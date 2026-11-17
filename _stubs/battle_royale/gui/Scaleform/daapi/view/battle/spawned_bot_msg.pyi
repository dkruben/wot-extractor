# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/spawned_bot_msg.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import canVehicleSpawnBot as canVehicleSpawnBot
from battle_royale.gui.battle_control.controllers.progression_ctrl import IProgressionListener as IProgressionListener
from gui.battle_control.view_components import IViewComponentsCtrlListener as IViewComponentsCtrlListener
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class SpawnedBotMsgPlayerMsgs(IProgressionListener, IViewComponentsCtrlListener):
    SPAWNED_BOT_DESTROYED_ID = 'SPAWNED_BOT_DESTROYED'
    __sessionProvider: Any
    __initialized: Any
    __started: Any
    def __init__(self):
        ...
    def setVehicleChanged(self, _, newModuleIntCD, vehicleRecreated):
        ...
    def detachedFromCtrl(self, ctrlID):
        ...
    def __onArenaVehicleKilled(self, targetID, attackerID, equipmentID, reason, numVehiclesAffected):
        ...
