# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/lobby/header/battle_selector_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from fort_rush_common.fort_rush_constants import QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE
from fort_rush.gui.fort_rush_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
_logger: Any
_HIGHLIGHT_LOBBY_VIOLET_LINKAGE = 'BgAnimVioletUI'
_HIGHLIGHT_FIGHT_VIOLET_LINKAGE = 'BGFightHighlightUI'

class _FortRushBattlesItem(battle_selector_items.SelectorItem):
    __systemMessages: Any
    _isSelected: Any
    _isDisabled: Any
    _isVisible: Any
    def isRandomBattle(self):
        ...
    def isShowEventIndication(self):
        ...
    def hasSparksAnimation(self, isNewbie, hasEventIndication):
        ...
    def getSmallIcon(self):
        ...
    def getLargerIcon(self):
        ...
    def getHighlightLinkage(self, isNewbie, defaultLinkage=''):
        ...
    def getFightButtonHighlight(self, isNewbie):
        ...
    def _update(self, state):
        ...

class FortRushSquadItem(battle_selector_items.SpecialSquadItem):
    _prebattleType: Any
    _isVisible: Any
    _isSpecialBgIcon: Any
    _isDescription: Any
    _isSelected: Any
    _isDisabled: Any
    def __init__(self, label, data, order, selectorType=None, isVisible=True):
        ...
    def isShowEventIndication(self):
        ...
    def getHighlightLinkage(self, isNewbie, defaultLinkage=''):
        ...
    def getSmallIcon(self):
        ...
    def _update(self, state):
        ...

def addFortRushBattlesType(items):
    ...
def addFortRushSquadType(items):
    ...
