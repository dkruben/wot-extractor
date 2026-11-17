# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/header/battle_selector_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light_constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from comp7_light.gui.comp7_light_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from comp7_light.gui.prb_control.entities import comp7_light_prb_helpers as comp7_light_prb_helpers
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import SelectorItem as SelectorItem, SpecialSquadItem as SpecialSquadItem
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class _Comp7LightItem(SelectorItem):
    __comp7LightController: Any
    _isSelected: Any
    _isVisible: Any
    _isDisabled: Any
    def isRandomBattle(self):
        ...
    def select(self):
        ...
    def _update(self, state):
        ...

class _Comp7LightSquadItem(SpecialSquadItem):
    __comp7LightController: Any
    _prebattleType: Any
    _isVisible: Any
    _isDisabled: Any
    _isSelected: Any
    def __init__(self, label, data, order, selectorType=None, isVisible=True):
        ...
    def _update(self, state):
        ...

def addComp7LightBattleType(items):
    ...
def addComp7LightSquadType(items):
    ...
