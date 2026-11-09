# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/status_notifications/sn_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.battle.shared.status_notifications.sn_items import TimerSN as TimerSN
from gui.impl import backport as backport
from story_mode.gui.battle_control.battle_constant import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from story_mode.gui.scaleform.genConsts.STORY_MODE_NOTIFICATIONS_TIMER_TYPES import STORY_MODE_NOTIFICATIONS_TIMER_TYPES as STORY_MODE_NOTIFICATIONS_TIMER_TYPES
from story_mode_common.story_mode_constants import RECON_ABILITY as RECON_ABILITY

class ReconAbilitySN(TimerSN):
    def _getEquipmentName(self):
        ...
    def getItemID(self):
        ...
    def getViewTypeID(self):
        ...
    def _getDescription(self, value):
        ...
    def _update(self, value):
        ...

class DisableShotSN(TimerSN):
    def start(self):
        ...
    def getItemID(self):
        ...
    def getViewTypeID(self):
        ...
    def _update(self, value):
        ...
