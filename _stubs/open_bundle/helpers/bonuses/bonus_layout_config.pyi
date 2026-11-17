# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/helpers/bonuses/bonus_layout_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
from future.utils import viewitems as viewitems
from items import _xml as _xml
from open_bundle.helpers.bonuses.bonuses_constants import BonusesLayoutAttrs as BonusesLayoutAttrs
from open_bundle.helpers.bonuses.bonuses_layout_helper import BonusesHelper as BonusesHelper
_PRIORITY_CONFIG_FILE = 'open_bundle/gui/bonuses_layout.xml'
_LEAST_PRIORITY_VALUE = 0
_DEFAULT_VISIBILITY = True

class BonusLayoutConfig(object):
    __storage: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def clear(self):
        ...
    def getPriority(self, bonus=None):
        ...
    def getIsVisible(self, bonus=None):
        ...
    def __getParameter(self, parameterType, default, bonus):
        ...
    def __loadLayout(self):
        ...

def _parseSections(section, name):
    ...
def _parseSectionValues(storage, name, section):
    ...
def _parseOverride(storage, section):
    ...
