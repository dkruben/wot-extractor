# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/stronghold_action_button_state_vo.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.rally.action_button_state_vo import ActionButtonStateVO as ActionButtonStateVO
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT as CYBERSPORT
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS

class StrongholdActionButtonStateVO(ActionButtonStateVO):
    __unitIsValid: Any
    __restrictionType: Any
    __isInPlayersMatching: Any
    __isFirstBattle: Any
    __isSortie: Any
    __hasFreeSlots: Any
    __playersMatchingAvailable: Any
    def __init__(self, unitEntity):
        ...
    def _getArenaStateStr(self):
        ...
    def _getLabel(self):
        ...
    def _notInSlotMessage(self):
        ...
    def _getUnitReadyMessage(self):
        ...
