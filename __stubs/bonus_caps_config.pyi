# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/bonus_caps_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Dict as Dict, Optional as Optional, FrozenSet as FrozenSet
from future.utils import viewitems as viewitems
from arena_bonus_type_caps import ALLOWED_ARENA_BONUS_TYPE_CAPS as ALLOWED_ARENA_BONUS_TYPE_CAPS
from constants import ARENA_BONUS_TYPE_NAMES as ARENA_BONUS_TYPE_NAMES
from soft_exception import SoftException as SoftException
from extension_utils import ResMgr as ResMgr
_CONFIG_FILE = 'scripts/item_defs/bonus_caps_config.xml'
_XML_NAMESPACE = 'xmlns:xmlref'

def readConfig(verbose=False):
    ...
def _readArenaTypes(section):
    ...
def _readBonuses(data):
    ...
