# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/hint_panel/component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import SoundGroups as SoundGroups
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.shared.hint_panel import plugins as plugins
from gui.Scaleform.daapi.view.meta.BattleHintPanelMeta import BattleHintPanelMeta as BattleHintPanelMeta
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.shared.utils.plugins import PluginsCollection as PluginsCollection
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gameplay import IGameplayLogic as IGameplayLogic, GameplayStateID as GameplayStateID

class BattleHintPanel(BattleHintPanelMeta, IAbstractPeriodView):
    __gameplayLogic: Any
    _hints: Any
    _plugins: Any
    __isBattleLoaded: Any
    __invalidateCallbackID: Any
    def __init__(self):
        ...
    def setBtnHint(self, btnID, hintData):
        ...
    def removeBtnHint(self, btnID):
        ...
    def setPeriod(self, period):
        ...
    def getActiveHint(self):
        ...
    def onPlaySound(self, soundType):
        ...
    def onHideComplete(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _initPlugins(self):
        ...
    def _finiPlugins(self):
        ...
    def _createPlugins(self):
        ...
    def __getActiveHintData(self):
        ...
    def __invalidateBtnHint(self, isRemoved=False):
        ...
    def __prepareAndShowHint(self, isRemoved):
        ...
    def _onPrebattleEnter(self, _=None, __=None):
        ...
    def __makeHotKey(self, hint):
        ...

class HintPluginsCollection(PluginsCollection):
    def start(self):
        ...
    def stop(self):
        ...
    def setPeriod(self, period):
        ...
    def __onMappingChanged(self, *args):
        ...
