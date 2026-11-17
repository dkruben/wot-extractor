# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/bonuses_layout_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
import ResMgr as ResMgr
from items import _xml as _xml
from gui.battle_pass.battle_pass_bonuses_helper import BonusesHelper as BonusesHelper
from gui.battle_pass.battle_pass_constants import BonusesLayoutConsts as BonusesLayoutConsts
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
_PRIORITY_CONFIG_FILE = 'gui/battle_pass_bonuses_layout.xml'
_LEAST_PRIORITY_VALUE = 0
_DEFAULT_VISIBILITY = True
_DEFAULT_BIG_ICON = 'None'

class BonusesLayoutController(object):
    __storage: Any
    __defaultPriority: Any
    __defaultVisibility: Any
    __defaultBigIcon: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def getPriority(self, bonus=None):
        ...
    def getIsVisible(self, bonus=None):
        ...
    def getBigIcon(self, bonus=None):
        ...
    def __loadLayout(self):
        ...
    @classmethod
    def __parseSection(cls, storage, name, section):
        ...
    @classmethod
    def __parseOverride(cls, storage, section):
        ...
