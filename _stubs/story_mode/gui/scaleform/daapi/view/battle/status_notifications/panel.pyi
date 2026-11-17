# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/status_notifications/panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.daapi.view.battle.pve_base.status_notifications.panel import PveStatusNotificationTimerPanel as PveStatusNotificationTimerPanel
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as _COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as _LINKAGES
from story_mode.gui.scaleform.daapi.view.battle.status_notifications.sn_items import ReconAbilitySN as ReconAbilitySN, DisableShotSN as DisableShotSN
from story_mode.gui.scaleform.genConsts.STORY_MODE_NOTIFICATIONS_TIMER_TYPES import STORY_MODE_NOTIFICATIONS_TIMER_TYPES as _SM_TYPES
_ENGINE_ICON = 'reconTimerEngineUI'
_DESTROY_TIMER_LINKAGE = 'StoryModeDestroyTimerUI'

class StoryModeStatusNotificationTimerPanel(PveStatusNotificationTimerPanel):
    def _generateItems(self):
        ...
    def _generateNotificationTimerSettings(self):
        ...
