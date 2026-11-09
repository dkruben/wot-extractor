# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/buffs_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import TOOLTIP_FORMAT as TOOLTIP_FORMAT
from gui.impl.gen import R as R
from gui.impl import backport as backport
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from helpers import dependency as dependency
from HWBuffPanelComponent import HWBuffPanelComponent as HWBuffPanelComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from halloween.gui.scaleform.daapi.view.battle.anomalies_utils import anomalyHeader as anomalyHeader, anomalyBody as anomalyBody
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.gui.scaleform.daapi.view.meta.BuffsPanelMeta import BuffsPanelMeta as BuffsPanelMeta

class BuffsPanel(BuffsPanelMeta):
    guiSessionProvider: Any
    hwAnomaliesCtrl: Any
    ICONS_PATH = R.images.halloween.gui.maps.icons.anomalies.s_36x36
    _buffs: Any
    _buffsState: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __init(self):
        ...
    def __onAvatarReady(self):
        ...
    def __handleBuffUnApply(self, ctx):
        ...
    def __addBuffToPanel(self, buffKey):
        ...
    def __handleBuffApply(self, ctx):
        ...
    def __handleBuffStateChanged(self, ctx):
        ...

def findBuffsPanelComponents():
    ...
