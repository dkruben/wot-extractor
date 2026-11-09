# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/postmortem_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.daapi.view.battle.shared.postmortem_panel import _ALLOWED_EQUIPMENT_DEATH_CODES as _ALLOWED_EQUIPMENT_DEATH_CODES
from gui.Scaleform.daapi.view.meta.BattleRoyalePostmortemPanelMeta import BattleRoyalePostmortemPanelMeta as BattleRoyalePostmortemPanelMeta
from gui.shared.gui_items import Vehicle as Vehicle
from items import vehicles as vehicles

class BattleRoyalePostmortemPanel(BattleRoyalePostmortemPanelMeta):
    __isBattleRoyaleTournament: Any
    __isObserver: Any
    _maxHealth: Any
    _isPlayerVehicle: Any
    _deathAlreadySet: Any
    _deathInfo: Any
    def __init__(self):
        ...
    def _onShowVehicleMessageByCode(self, code, postfix, entityID, extra, equipmentID, ignoreMessages):
        ...
    def _populate(self):
        ...
    def __updatePostmortemTipsVisibility(self):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
    def _showOwnDeathInfo(self):
        ...
    def _prepareMessage(self, code, killerVehID, device=None):
        ...
    def _updateVehicleInfo(self):
        ...
    def __isBattleRoyaleBotVehicle(self, vehicleID):
        ...
