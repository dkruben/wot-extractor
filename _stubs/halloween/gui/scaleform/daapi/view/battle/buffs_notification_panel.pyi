# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/buffs_notification_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from halloween_common.halloween_constants import AnomalyType as AnomalyType
from helpers import dependency as dependency
from gui import makeHtmlString as makeHtmlString
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent as BattleHintComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, HALLOWEEN_BATTLE_HINTS_QUEUE_ID as HALLOWEEN_BATTLE_HINTS_QUEUE_ID
from halloween.gui.scaleform.daapi.view.battle.anomalies_utils import anomalyTitle as anomalyTitle, anomalyDescriptionList as anomalyDescriptionList
from halloween.gui.scaleform.daapi.view.meta.BuffNotificationSystemMeta import BuffNotificationSystemMeta as BuffNotificationSystemMeta

class BuffsNotificationSystem(BattleHintComponent, BuffNotificationSystemMeta):
    sessionProvider: Any
    hwAnomaliesCtrl: Any
    ICONS_PATH = R.images.halloween.gui.maps.icons.anomalies.s_58x58
    BATTLE_HINT_TEMPLATE = 'halloween.buffNotification'
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _showHint(self, model, params):
        ...
    def _hideHint(self):
        ...
    def _cancelFadeOut(self):
        ...
    def __makeHtmlFormat(self, text, format):
        ...
