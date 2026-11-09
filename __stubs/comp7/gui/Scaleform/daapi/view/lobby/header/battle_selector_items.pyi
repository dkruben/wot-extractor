# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/header/battle_selector_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.comp7_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from comp7.gui.prb_control.entities import comp7_prb_helpers as comp7_prb_helpers
from comp7_common.comp7_constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import SelectorItem as SelectorItem, SpecialSquadItem as SpecialSquadItem, _getSeasonInfoStr as _getSeasonInfoStr
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class _Comp7Item(SelectorItem):
    __comp7Controller: Any
    _isSelected: Any
    _isVisible: Any
    _isDisabled: Any
    def isRandomBattle(self):
        ...
    def select(self):
        ...
    def getFormattedLabel(self):
        ...
    def getSmallIcon(self):
        ...
    def getLargerIcon(self):
        ...
    def getSpecialBGIcon(self):
        ...
    def _update(self, state):
        ...
    @classmethod
    def __getScheduleStr(cls):
        ...

class _Comp7SquadItem(SpecialSquadItem):
    __controller: Any
    _prebattleType: Any
    _isVisible: Any
    _isDisabled: Any
    _isSelected: Any
    def __init__(self, label, data, order, selectorType=None, isVisible=True):
        ...
    def getSmallIcon(self):
        ...
    def _update(self, state):
        ...

def addComp7BattleType(items):
    ...
def addComp7SquadType(items):
    ...
