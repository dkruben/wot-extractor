# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/header/battle_selector_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from last_stand_common.last_stand_constants import QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE
from last_stand.gui.ls_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings
from last_stand.skeletons.ls_controller import ILSController as ILSController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency

class _LSItem(battle_selector_items.SelectorItem):
    lsCtrl: Any
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

class LSSquadItem(battle_selector_items.SpecialSquadItem):
    lsCtrl: Any
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

def addLastStandType(items):
    ...
def addLastStandSquadType(items):
    ...
