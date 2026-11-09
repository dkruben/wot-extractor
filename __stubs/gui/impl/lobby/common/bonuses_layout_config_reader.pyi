# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/bonuses_layout_config_reader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import ResMgr as ResMgr
from items import _xml as _xml
from gui.impl.lobby.common.bonuses_layout_helpers import BonusesLayoutHelper as BonusesLayoutHelper, BonusesLayoutAttrs as BonusesLayoutAttrs
_LEAST_PRIORITY_VALUE = 0
_DEFAULT_VISIBILITY = True

class BonusesLayout(object):
    __configFile: Any
    __subTypeGetter: Any
    __valueGetter: Any
    __storage: Any
    def __init__(self, configFile, subTypeGetter=None, valueGetter=None):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def getPriority(self, bonus=None):
        ...
    def getIsVisible(self, bonus=None):
        ...
    def _parseSections(self, section, name):
        ...
    def _parseSectionValues(self, storage, name, section):
        ...
    def _parseOverride(self, storage, section):
        ...
    def __loadLayout(self):
        ...
    def __getParameter(self, parameterType, default, bonus):
        ...
