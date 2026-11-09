# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/header/battle_selector_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from halloween_common.halloween_constants import QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE
from halloween.gui.halloween_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency

class _HalloweenItem(battle_selector_items.SelectorItem):
    __halloweenCtrl: Any
    _isDisabled: Any
    _isSelected: Any
    _isVisible: Any
    def isShowEventIndication(self):
        ...
    def hasSparksAnimation(self, isNewbie, hasEventIndication):
        ...
    def getSmallIcon(self):
        ...
    def getLargerIcon(self):
        ...
    def isRandomBattle(self):
        ...
    @property
    def squadIcon(self):
        ...
    def _update(self, state):
        ...
    def _isKnownBattleType(self):
        ...

class HalloweenSquadItem(battle_selector_items.SpecialSquadItem):
    __halloweenCtrl: Any
    _prebattleType: Any
    _isVisible: Any
    _isSpecialBgIcon: Any
    _isDescription: Any
    _isSelected: Any
    def __init__(self, label, data, order, selectorType=None, isVisible=True):
        ...
    def getSmallIcon(self):
        ...
    def isShowEventIndication(self):
        ...
    def hasSparksAnimation(self, isNewbie, hasEventIndication):
        ...
    def _update(self, state):
        ...
    def _isKnownBattleType(self):
        ...

def addHalloweenType(items):
    ...
def addHalloweenSquadType(items):
    ...
