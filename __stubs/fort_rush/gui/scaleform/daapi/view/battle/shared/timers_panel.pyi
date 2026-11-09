# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/shared/timers_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fort_rush.gui.battle_control.fort_rush_battle_constants import FR_VEHICLE_VIEW_STATE as FR_VEHICLE_VIEW_STATE
from gui.Scaleform.daapi.view.battle.shared.timers_panel import TimersPanel as TimersPanel, _TIMERS_PRIORITY as _TIMERS_PRIORITY
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as BATTLE_NOTIFICATIONS_TIMER_COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as BATTLE_NOTIFICATIONS_TIMER_LINKAGES
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as _TIMER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.impl import backport as backport
from gui.impl.gen import R as R
_INVULNERABLE = 'invulnerable'
_INVULNERABLE_PRIORITY: tuple

class FortRushTimersPanel(TimersPanel):
    def __init__(self, mapping=None):
        ...
    def _dispose(self):
        ...
    def _generateMainTimersData(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
