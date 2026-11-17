# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/shared/status_notifications/panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from comp7_core.gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items as comp7_sn_items
from comp7_core.gui.Scaleform.daapi.view.battle.shared.status_notifications import components as components
from gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items as sn_items
from gui.Scaleform.daapi.view.battle.shared.status_notifications.panel import StatusNotificationTimerPanel as StatusNotificationTimerPanel
from gui.Scaleform.daapi.view.battle.shared.status_notifications.poi_sn_items import PoiNotificationsGroup as PoiNotificationsGroup
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as _COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as _LINKS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as _TYPES
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as INGAME_GUI
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_logger: Any

class Comp7BattleHighPriorityGroup(components.StatusNotificationsGroup):
    def __init__(self, updateCallback):
        ...

class Comp7StatusNotificationTimerPanel(StatusNotificationTimerPanel):
    _settingsCore: Any
    def _getComponentClass(self):
        ...
    def _generateItems(self):
        ...
    def _generateNotificationTimerSettings(self):
        ...
    def __genPoiTimersSettings(self, data):
        ...
    def __gerRoleSkillsTimersSettings(self, data):
        ...
