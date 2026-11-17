# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/damage_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.battle.shared.damage_panel import DamagePanel as DamagePanel, STATUS_ID as STATUS_ID, ConcurrentStatusManager as ConcurrentStatusManager
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
_logger: Any
_STATUS_EFFECTS_PRIORITY: tuple

class Comp7DamagePanel(DamagePanel):
    def _getConcurrentStatusManager(self):
        ...
    def _updateStun(self, stunInfo):
        ...
    def _updateCrewBuff(self, buffName, isActive, duration):
        ...
    def __updateCrewStun(self, buffName, isActive, duration):
        ...
    def __updateEffect(self, buffName, isActive, duration, animationPlayer):
        ...

class _Comp7ConcurrentStatusManager(ConcurrentStatusManager):
    _exposedStatusEndTime: Any
    _exposedStatus: Any
    _animationPlayer: Any
    def setStatus(self, statusName, endTime, animationPlayer=None):
        ...
    def deleteStatus(self, statusName):
        ...
    def _getEffectsPriority(self, effect):
        ...
    def _updateBuffAnimation(self):
        ...
