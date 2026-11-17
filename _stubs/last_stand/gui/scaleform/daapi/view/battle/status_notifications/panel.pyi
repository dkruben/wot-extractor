# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/status_notifications/panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items as sn_items
from gui.Scaleform.daapi.view.battle.shared.status_notifications import components as components
from gui.Scaleform.daapi.view.battle.shared.status_notifications.panel import StatusNotificationTimerPanel as StatusNotificationTimerPanel
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as _COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as _LINKS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as _TYPES
from last_stand.gui.scaleform.genConsts.LS_BATTLE_NOTIFICATIONS_TIMER_TYPES import LS_BATTLE_NOTIFICATIONS_TIMER_TYPES as _LSTYPES
from last_stand.gui.scaleform.genConsts.LS_NOTIFICATION_TIMER_ALIASES import LS_NOTIFICATION_TIMER_ALIASES as _LSLINKS
from last_stand.gui.scaleform.daapi.view.battle.status_notifications import sn_items as _LS_SW_ITEMS
_logger: Any

class _LSHighPriorityGroup(components.StatusNotificationsGroup):
    def __init__(self, updateCallback):
        ...

class LSStatusNotificationTimerPanel(StatusNotificationTimerPanel):
    def _generateItems(self):
        ...
    def _generateNotificationTimerSettings(self):
        ...
