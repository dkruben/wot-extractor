# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/status_notifications/panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from frontline.gui.Scaleform.daapi.view.battle.status_notifications import sn_items as frontline_sn_items
from gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items as sn_items
from gui.Scaleform.daapi.view.battle.shared.status_notifications import components as components
from gui.Scaleform.daapi.view.battle.shared.status_notifications.panel import StatusNotificationTimerPanel as StatusNotificationTimerPanel
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as _COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as _LINKS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as _TYPES
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as INGAME_GUI
_logger: Any

class _FrontlineBattleHighPriorityGroup(components.StatusNotificationsGroup):
    def __init__(self, updateCallback):
        ...

class FrontlineStatusNotificationTimerPanel(StatusNotificationTimerPanel):
    def _generateItems(self):
        ...
    def _generateNotificationTimerSettings(self):
        ...
