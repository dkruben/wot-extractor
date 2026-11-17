# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_modification_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from frontline.gui.Scaleform.daapi.view.meta.FrontlineModificationPanelMeta import FrontlineModificationPanelMeta as FrontlineModificationPanelMeta
from frontline.gui.frontline_helpers import FLBattleTypeDescription as FLBattleTypeDescription
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class FrontlineBattleModificationPanel(FrontlineModificationPanelMeta, IArenaVehiclesController):
    __slots__: tuple
    __sessionProvider: Any
    _isVisible: Any
    _lastPeriod: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __animationStart(self):
        ...
    def __animationHide(self):
        ...
    def _onBattleLoading(self, event):
        ...
    def _onRoundStarted(self, period, *_):
        ...
    def __getData(self):
        ...
