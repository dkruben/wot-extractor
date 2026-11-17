# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/header/battle_selector_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from constants import QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE
from fun_random.gui.feature.fun_constants import FunSubModesState as FunSubModesState
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.fun_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import SelectorItem as SelectorItem, SpecialSquadItem as SpecialSquadItem
from gui.shared.utils.functions import makeTooltip as makeTooltip

class _FunRandomItem(SelectorItem, FunAssetPacksMixin, FunSubModesWatcher):
    _HIDDEN_STATES: tuple
    _isVisible: Any
    _isDisabled: Any
    _isSelected: Any
    def __init__(self, data, order, selectorType=None, isVisible=True):
        ...
    def isShowEventIndication(self):
        ...
    def getLabel(self):
        ...
    def getLargerIcon(self):
        ...
    def getSmallIcon(self):
        ...
    def _update(self, state):
        ...
    # decorador original: @adisp_process
    def _doSelect(self, dispatcher):
        ...
    def __getIsVisible(self):
        ...

class _FunRandomSquadItem(SpecialSquadItem, FunAssetPacksMixin, FunSubModesWatcher):
    _RES_SHORTCUT = R.strings.fun_random.headerButtons
    _isVisible: Any
    _prebattleType: Any
    _isSelected: Any
    def __init__(self, label, data, order, selectorType=None, isVisible=True):
        ...
    def getFormattedLabel(self):
        ...
    def getSmallIcon(self):
        ...
    def _createTooltip(self):
        ...
    def _update(self, state):
        ...

def addFunRandomBattleType(items):
    ...
def addFunRandomSquadType(items):
    ...
