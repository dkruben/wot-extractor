# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/stronghold/timers_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.battle.shared.timers_panel import TimersPanel as TimersPanel
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as BATTLE_NOTIFICATIONS_TIMER_COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as BATTLE_NOTIFICATIONS_TIMER_LINKAGES
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as BATTLE_NOTIFICATIONS_TIMER_TYPES
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
_logger: Any
_INSPIRE_TIMERS: tuple
_INSPIRE_TIMERS_MAP: dict

class StrongholdTimersPanel(TimersPanel):
    def _generateSecondaryTimersData(self):
        ...
    def _updateInspireTimer(self, isSourceVehicle, isInactivation, endTime, duration, primary=True, equipmentID=None):
        ...
    def _getInspireSecondaryTimerText(self, isSourceVehicle=False):
        ...
