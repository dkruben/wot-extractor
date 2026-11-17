# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/bonuses_layout.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import functools as functools
import logging as logging
import ResMgr as ResMgr
from gui.impl.gen.view_models.views.lobby.lootbox_system.bonus_model import BonusRarity as BonusRarity
from gui.lootbox_system.base.bonuses_layout_helpers import BonusesHelper as BonusesHelper
from gui.lootbox_system.base.common import BonusesLayoutAttrs as BonusesLayoutAttrs, DEFAULT_EVENT_NAME as DEFAULT_EVENT_NAME
from helpers import dependency as dependency
from items import _xml as _xml
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
_logger: Any
_CONFIG_FILENAME = 'gui/lootbox_system_bonuses_layout.xml'
_MAIN_SECTION_NAME = 'core'
_DEFAULT_SECTION_NAME = 'default'
_LEAST_PRIORITY = 0
_DEFAULT_RARITY = BonusRarity.COMMON
_DEFAULT_VISIBILITY = True

class BonusesLayout(object):
    __lootBoxes: Any
    __storage: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def updateStorage(self):
        ...
    def getPriority(self, eventName, bonus=None):
        ...
    def getRarity(self, eventName, bonus=None):
        ...
    def getIsVisible(self, eventName, bonus=None):
        ...
    def __getParameter(self, eventName, parameterType, default, bonus):
        ...
    def __loadLayout(self):
        ...

def mergeDicts(destination, first, second=None):
    ...
def _parseSections(section, name):
    ...
def _parseSectionValues(storage, name, section):
    ...
def _parseOverride(storage, section):
    ...
def _mergeDicts(destination, source):
    ...
